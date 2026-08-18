#!/usr/bin/env python3
"""Probe Roberts Lab servers and emit a status JSON document.

Usage:
    check_servers.py --profile internal [--out FILE]
    check_servers.py --profile external [--out FILE]

Profiles exist because the three hosts are not reachable from the same place:

    raven   not in public DNS; only visible from inside the UW network
    gannet  public HTTPS
    klone   public, but SSH (22) only -- there is no web port to probe

"internal" runs on a machine inside the UW network and checks all three.
"external" runs on a GitHub Actions runner and checks the two public hosts, so
that a dead internal prober does not blind us on everything at once.

A green light means the port answered. It says nothing about whether Slurm is
healthy or anyone's jobs are actually running. Raven's disk space and CPU
load are reported separately, from a daily snapshot (see fetch_raven_stats).

Stdlib only, Python 3.6+.
"""

import argparse
import json
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

DEFAULT_TIMEOUT = 8.0

# Raven itself is not in public DNS, but a cron on raven drops a daily
# df/CPU snapshot on gannet's public web root -- see scripts/README.md. That
# makes it fetchable over plain HTTPS by both probers, unlike the live TCP
# check below, which only the internal one can reach.
RAVEN_STATS_URL = "https://gannet.fish.washington.edu/v1_web/owlshell/bu-github/ghr.log"

# Each disk line looks like "/dev/sdd1  7.3T  6.3T  602G  92%  /home/shared/...".
_DISK_LINE = re.compile(r"^(\S+)\s+\S+\s+\S+\s+\S+\s+(\d+)%\s+(\S+)$")
_PERCENT = re.compile(r"^([\d.]+)%$")


def tcp_check(host, port, timeout):
    """Plain TCP connect. Used for klone (SSH) and raven (RStudio Server)."""
    start = time.monotonic()
    try:
        # create_connection resolves and tries every address, which matters for
        # klone -- it has two A records.
        with socket.create_connection((host, port), timeout=timeout):
            pass
    except (socket.timeout, socket.gaierror, OSError) as exc:
        if isinstance(exc, socket.gaierror):
            detail = "DNS lookup failed (host is not resolvable from here)"
        elif isinstance(exc, socket.timeout):
            detail = "TCP {} did not answer within {:.0f}s".format(port, timeout)
        else:
            detail = "TCP {} refused: {}".format(port, exc.strerror or exc)
        return {"up": False, "detail": detail, "latency_ms": None}
    elapsed = int((time.monotonic() - start) * 1000)
    return {"up": True, "detail": "TCP {} open".format(port), "latency_ms": elapsed}


def http_check(url, timeout):
    """HTTP(S) check. Any 2xx/3xx counts as up."""
    start = time.monotonic()
    request = urllib.request.Request(url, method="HEAD")
    request.add_header("User-Agent", "robertslab-handbook-status-check")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            code = response.status
    except urllib.error.HTTPError as exc:
        code = exc.code  # server answered, just not with success
    except ssl.SSLError as exc:
        return {
            "up": False,
            "detail": "TLS error: {}".format(exc),
            "latency_ms": None,
        }
    except (urllib.error.URLError, socket.timeout, OSError) as exc:
        reason = getattr(exc, "reason", exc)
        return {
            "up": False,
            "detail": "no response within {:.0f}s ({})".format(timeout, reason),
            "latency_ms": None,
        }
    elapsed = int((time.monotonic() - start) * 1000)
    up = 200 <= code < 400
    return {
        "up": up,
        "detail": "HTTP {}".format(code),
        "latency_ms": elapsed if up else None,
    }


def check_raven(timeout):
    """RStudio Server is what people actually want from raven, so probe 8787
    rather than just SSH -- but distinguish 'whole box is down' from 'the box is
    up and RStudio isn't'."""
    result = tcp_check("raven.fish.washington.edu", 8787, timeout)
    if result["up"]:
        return result
    ssh = tcp_check("raven.fish.washington.edu", 22, timeout)
    if ssh["up"]:
        return {
            "up": False,
            "detail": "SSH is up but RStudio Server (8787) is not answering",
            "latency_ms": ssh["latency_ms"],
        }
    return result


def fetch_raven_stats(timeout):
    """Parse the daily df/CPU snapshot raven publishes on gannet.

    Returns None if the file cannot be fetched or does not parse -- a
    missing snapshot should not make the whole check fail, and the front
    end already treats missing/stale data as "unknown" rather than red.
    """
    request = urllib.request.Request(RAVEN_STATS_URL)
    request.add_header("User-Agent", "robertslab-handbook-status-check")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", "replace")
            last_modified = response.headers.get("Last-Modified")
    except (urllib.error.URLError, socket.timeout, OSError):
        return None

    lines = body.splitlines()

    disks = []
    for line in lines:
        match = _DISK_LINE.match(line.strip())
        if match:
            disks.append({"mount": match.group(3), "use_percent": int(match.group(2))})

    cpu_percent = None
    for i, line in enumerate(lines):
        if line.strip() != "Percent CPUs cranking?":
            continue
        for candidate in lines[i + 1:]:
            candidate = candidate.strip()
            if not candidate:
                continue
            match = _PERCENT.match(candidate)
            if match:
                cpu_percent = float(match.group(1))
            break
        break

    if not disks and cpu_percent is None:
        return None

    generated = None
    if last_modified:
        try:
            generated = (
                parsedate_to_datetime(last_modified)
                .astimezone(timezone.utc)
                .strftime("%Y-%m-%dT%H:%M:%SZ")
            )
        except (TypeError, ValueError):
            generated = None

    return {"generated": generated, "cpu_percent": cpu_percent, "disks": disks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, choices=["internal", "external"])
    parser.add_argument("--out", help="write JSON here instead of stdout")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    args = parser.parse_args()

    hosts = {}
    if args.profile == "internal":
        hosts["raven"] = check_raven(args.timeout)
    hosts["gannet"] = http_check("https://gannet.fish.washington.edu/", args.timeout)
    hosts["klone"] = tcp_check("klone.hyak.uw.edu", 22, args.timeout)

    document = {
        "checked": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": args.profile,
        "hosts": hosts,
    }

    # Fetched over public HTTPS (see fetch_raven_stats), so both profiles can
    # get it. Kept out of "hosts" on purpose: hosts are merged by picking the
    # freshest *document*, and the external prober can run more often than
    # the internal cron. If raven_stats lived under hosts["raven"] it would
    # periodically overwrite a live, accurate up/down reading with one that
    # carries no port-check result at all.
    raven_stats = fetch_raven_stats(args.timeout)
    if raven_stats:
        document["raven_stats"] = raven_stats
    text = json.dumps(document, indent=2, sort_keys=True)

    if args.out:
        with open(args.out, "w") as handle:
            handle.write(text + "\n")
        print("wrote {}".format(args.out), file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
