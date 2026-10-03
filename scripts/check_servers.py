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
import os
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
# A year of daily raven entries is ~1 MB of JSON at most.
RAVEN_HISTORY_DAYS = 365

# Gannet writes a daily health report (owlshell/gannet_health.sh) to its own
# public web root: latest.txt plus a dated gannet_health_YYYY-MM-DD.txt copy.
# The dated copies are what the dashboard's history charts are built from.
GANNET_REPORT_DIR = "https://gannet.fish.washington.edu/v1_web/owlshell/"
GANNET_LATEST_URL = GANNET_REPORT_DIR + "latest.txt"
GANNET_HISTORY_DAYS = 30

# A scrontab job on klone runs `hyakalloc` at 06:00 Pacific and copies the
# output here, under a "Generated: ..." line. Klone itself needs Duo for SSH,
# so nothing outside it can run hyakalloc -- see scripts/README.md.
HYAK_ALLOC_URL = GANNET_REPORT_DIR + "hyakalloc.txt"
_DATED_HYAK = re.compile(r'href="(hyakalloc_(\d{4}-\d{2}-\d{2})\.txt)"')

_SECTION = re.compile(r"^==== (.+?) ====$")
_DATED_REPORT = re.compile(r'href="(gannet_health_(\d{4}-\d{2}-\d{2})\.txt)"')
# "/dev/md0  ext4  2.3G  1.7G  535M  76% /" -- df -hT, so there is a type column.
_DF_T_LINE = re.compile(r"^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)%\s+(\S+)$")
_INODE_LINE = re.compile(r"^(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)%\s+(\S+)$")
_LOAD = re.compile(r"load average:\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)")
_UPTIME = re.compile(r"\bup\s+(.+?),\s+\d+\s+users?,")
_RAID_HEAD = re.compile(r"^(md\d+)\s*:\s*(\S+)\s+(raid\w+)")
_RAID_STATE = re.compile(r"\[(\d+)/(\d+)\]\s+\[([U_]+)\]")
_ALERT = re.compile(r"^\*\s+(\S+)\s+(.*)$")
_TZ_OFFSETS = {"PDT": "-0700", "PST": "-0800", "UTC": "+0000", "GMT": "+0000"}

# Each disk line looks like "/dev/sdd1  7.3T  6.3T  602G  92%  /home/shared/...":
# filesystem, size, used, available, use%, mount point.
_DISK_LINE = re.compile(r"^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)%\s+(\S+)$")
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
            disks.append(
                {
                    "filesystem": match.group(1),
                    "size": match.group(2),
                    "used": match.group(3),
                    "available": match.group(4),
                    "use_percent": int(match.group(5)),
                    "mount": match.group(6),
                }
            )

    cpu_percent = _single_percent(_raven_block(lines, "Percent CPUs cranking?"))
    memory_percent = _single_percent(_raven_block(lines, "How much memory being used?"))

    # "user cpu mem%": %CPU and %MEM summed over that user's processes, top 5
    # by CPU. ps's own header line gets summed in as user "USER"; drop it.
    winners = []
    for line in _raven_block(lines, "Winners"):
        fields = line.split()
        if len(fields) != 3 or fields[0] == "USER":
            continue
        try:
            winners.append(
                {
                    "user": fields[0],
                    "cpu": float(fields[1]),
                    "mem_percent": float(fields[2].rstrip("%")),
                }
            )
        except ValueError:
            continue

    # "user<TAB>command<TAB>mem%", top 5 processes by memory.
    top_memory = []
    for line in _raven_block(lines, "Where is my Memory?"):
        fields = line.split("\t")
        if len(fields) != 3 or fields[0] == "USER":
            continue
        try:
            top_memory.append(
                {
                    "user": fields[0],
                    "command": fields[1],
                    "mem_percent": float(fields[2].rstrip("%")),
                }
            )
        except ValueError:
            continue

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

    return {
        "generated": generated,
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disks": disks,
        "winners": winners,
        "top_memory": top_memory,
    }


def _raven_block(lines, heading):
    """Non-blank lines after a ghr.log heading, up to the next blank line."""
    block = []
    for i, line in enumerate(lines):
        if line.strip() != heading:
            continue
        for candidate in lines[i + 1:]:
            if not candidate.strip():
                break
            block.append(candidate.strip())
        break
    return block


def _single_percent(block):
    if block:
        match = _PERCENT.match(block[0])
        if match:
            return float(match.group(1))
    return None


def update_raven_history(path, stats):
    """Append today's raven snapshot to a JSON history file and return it.

    Raven overwrites ghr.log each morning and keeps no dated copies, so the
    history has to be accumulated here. The file lives on the server-status
    branch next to the status documents; publish_status.sh checks out the
    branch before running us, so the previous run's copy is already on disk.
    One entry per snapshot date; a re-run on the same day replaces it.
    """
    history = []
    try:
        with open(path) as handle:
            history = json.load(handle)
    except (OSError, ValueError):
        history = []
    if not isinstance(history, list):
        history = []

    if stats.get("generated"):
        entry = {
            "date": stats["generated"][:10],
            "generated": stats["generated"],
            "cpu_percent": stats.get("cpu_percent"),
            "memory_percent": stats.get("memory_percent"),
            "disks": {d["mount"]: d["use_percent"] for d in stats.get("disks", [])},
            "winners": stats.get("winners", []),
        }
        history = [h for h in history if h.get("date") != entry["date"]]
        history.append(entry)
        history.sort(key=lambda h: h.get("date", ""))
        history = history[-RAVEN_HISTORY_DAYS:]

    with open(path, "w") as handle:
        json.dump(history, handle, indent=1, sort_keys=True)
        handle.write("\n")
    return history


def _fetch_text(url, timeout):
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "robertslab-handbook-status-check")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace"), response.headers.get(
            "Last-Modified"
        )


def _iso_utc(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _split_sections(body):
    """{section title: [lines]} for the '==== Title ====' blocks, plus the
    lines before the first one under ''."""
    sections = {"": []}
    current = ""
    for line in body.splitlines():
        match = _SECTION.match(line.strip())
        if match:
            current = match.group(1)
            sections[current] = []
        else:
            sections[current].append(line.rstrip())
    return sections


def _nonblank(lines):
    return [line.strip() for line in lines if line.strip()]


def _parse_generated(lines, last_modified=None):
    """ISO UTC time from a "Generated: 2026-10-03 05:38:45 PDT" line, falling
    back to the HTTP Last-Modified header."""
    for line in lines:
        if line.startswith("Generated:"):
            stamp = line.split(":", 1)[1].strip()
            parts = stamp.rsplit(" ", 1)
            if len(parts) == 2 and parts[1] in _TZ_OFFSETS:
                stamp = parts[0] + " " + _TZ_OFFSETS[parts[1]]
            try:
                return _iso_utc(datetime.strptime(stamp, "%Y-%m-%d %H:%M:%S %z"))
            except ValueError:
                break
    if last_modified:
        try:
            return _iso_utc(parsedate_to_datetime(last_modified))
        except (TypeError, ValueError):
            pass
    return None


def parse_gannet_report(body, last_modified=None):
    """Parse one gannet_health.sh report into a dict. Returns None if it does
    not look like a report at all.

    Every section is optional: the script skips some (SMART needs root) and
    may grow new ones, and a partial parse is more useful than none.
    """
    sections = _split_sections(body)
    if len(sections) < 2:
        return None

    generated = _parse_generated(sections[""], last_modified)

    report = {"generated": generated}

    uptime_lines = sections.get("Uptime and load", [])
    for line in uptime_lines:
        load = _LOAD.search(line)
        if load:
            report["load"] = [float(x) for x in load.groups()]
            up = _UPTIME.search(line)
            if up:
                report["uptime"] = up.group(1).strip()
        if line.startswith("CPU cores:"):
            try:
                report["cpu_cores"] = int(line.split(":", 1)[1])
            except ValueError:
                pass

    inodes = {}
    for line in sections.get("Inode usage", []):
        match = _INODE_LINE.match(line.strip())
        if match:
            inodes[match.group(6)] = int(match.group(5))

    # Skip loop devices and the Synology @appdata bind mounts: they re-list
    # /volume1 under other paths and would just duplicate its row.
    disks = []
    for line in sections.get("Disk usage", []):
        match = _DF_T_LINE.match(line.strip())
        if not match:
            continue
        filesystem, fstype, size, used, avail, pct, mount = match.groups()
        if filesystem.startswith("/dev/loop") or "/@" in mount:
            continue
        disks.append(
            {
                "filesystem": filesystem,
                "type": fstype,
                "size": size,
                "used": used,
                "available": avail,
                "use_percent": int(pct),
                "mount": mount,
                "inode_percent": inodes.get(mount),
            }
        )
    report["disks"] = disks

    memory = {}
    for line in sections.get("Memory", []):
        fields = line.split()
        if fields and fields[0] in ("Mem:", "Swap:") and len(fields) >= 4:
            key = fields[0].rstrip(":").lower()
            entry = {"total": fields[1], "used": fields[2], "free": fields[3]}
            if key == "mem" and len(fields) >= 7:
                entry["available"] = fields[6]
            memory[key] = entry
    report["memory"] = memory

    arrays = []
    for line in sections.get("RAID status", []):
        head = _RAID_HEAD.match(line.strip())
        if head:
            arrays.append(
                {"name": head.group(1), "state": head.group(2), "level": head.group(3)}
            )
            continue
        state = _RAID_STATE.search(line)
        if state and arrays and "members" not in arrays[-1]:
            arrays[-1]["members"] = int(state.group(1))
            arrays[-1]["active"] = int(state.group(2))
            arrays[-1]["healthy"] = (
                "_" not in state.group(3) and state.group(1) == state.group(2)
            )
    report["raid"] = arrays

    services, failed, in_failed = [], [], False
    for line in _nonblank(sections.get("Services", [])):
        if line.startswith("Failed units"):
            in_failed = True
            continue
        fields = line.split()
        if in_failed:
            # "unit.service loaded failed failed Description words..."
            failed.append(
                {"unit": fields[0], "description": " ".join(fields[4:]) or None}
            )
        elif len(fields) == 2:
            services.append({"name": fields[0], "state": fields[1]})
    report["services"] = services
    report["failed_units"] = failed

    kernel = _nonblank(sections.get("Recent kernel errors (last 24h)", []))
    report["kernel_errors"] = [] if kernel == ["None."] else kernel
    report["smart"] = _nonblank(sections.get("SMART drive health", []))
    report["shares"] = _nonblank(sections.get("Share connections", []))
    report["changes"] = _nonblank(sections.get("Change since last report", []))

    alerts = []
    for line in _nonblank(sections.get("Summary", [])):
        match = _ALERT.match(line)
        if match:
            alerts.append({"level": match.group(1).lower(), "message": match.group(2)})
    report["alerts"] = alerts
    return report


def _history_point(date, report):
    return {
        "date": date,
        "load": report.get("load"),
        "disks": {d["mount"]: d["use_percent"] for d in report.get("disks", [])},
        "alerts": len(report.get("alerts", [])),
    }


def fetch_gannet_stats(timeout):
    """Latest gannet health report, parsed, plus a short daily history built
    from the dated copies. Returns None if latest.txt is unavailable, for the
    same reason as fetch_raven_stats."""
    try:
        body, last_modified = _fetch_text(GANNET_LATEST_URL, timeout)
    except (urllib.error.URLError, socket.timeout, OSError):
        return None
    report = parse_gannet_report(body, last_modified)
    if not report:
        return None
    report["raw"] = body

    history = []
    try:
        index, _ = _fetch_text(GANNET_REPORT_DIR, timeout)
        dated = sorted(set(_DATED_REPORT.findall(index)), key=lambda x: x[1])
    except (urllib.error.URLError, socket.timeout, OSError):
        dated = []
    for name, date in dated[-GANNET_HISTORY_DAYS:]:
        try:
            text, _ = _fetch_text(GANNET_REPORT_DIR + name, timeout)
        except (urllib.error.URLError, socket.timeout, OSError):
            continue
        parsed = parse_gannet_report(text)
        if parsed:
            history.append(_history_point(date, parsed))
    report["history"] = history
    return report


def _gigabytes(value):
    """hyakalloc prints memory as e.g. "7305G"; return the number of GB."""
    match = re.match(r"^([\d.]+)([KMGT]?)$", value)
    if not match:
        return None
    scale = {"K": 1.0 / 1024 ** 2, "M": 1.0 / 1024, "G": 1, "T": 1024, "": 1}
    return float(match.group(1)) * scale[match.group(2)]


def parse_hyakalloc(body, last_modified=None):
    """Parse hyakalloc's box-drawn tables. Returns None if no partition rows
    were found.

    Each partition takes three rows -- TOTAL, USED, FREE -- and only the
    TOTAL row carries the account and partition names.
    """
    partitions = []
    checkpoint = None
    current = None
    for line in body.splitlines():
        cells = [c.strip() for c in line.split("\u2502")]
        if len(cells) < 3:
            continue
        cells = cells[1:-1]  # drop what lies outside the outer borders
        if len(cells) == 6 and cells[5] in ("TOTAL", "USED", "FREE"):
            account, partition, cpus, memory, gpus, kind = cells
            if kind == "TOTAL" or current is None:
                current = {"account": account, "partition": partition}
                partitions.append(current)
            try:
                current[kind.lower()] = {
                    "cpus": int(cpus),
                    "memory": memory,
                    "memory_gb": _gigabytes(memory),
                    "gpus": int(gpus),
                }
            except ValueError:
                continue
        elif len(cells) == 3 and cells[0] == "Idle:":
            try:
                checkpoint = {"idle_cpus": int(cells[1]), "idle_gpus": int(cells[2])}
            except ValueError:
                pass

    partitions = [p for p in partitions if "total" in p]
    if not partitions:
        return None
    user = re.search(r"available to user:\s*(\S+)", body)
    return {
        "generated": _parse_generated(body.splitlines(), last_modified),
        "user": user.group(1) if user else None,
        "partitions": partitions,
        "checkpoint": checkpoint,
    }


def fetch_hyak_stats(timeout):
    """Klone's daily hyakalloc snapshot, parsed. None if unavailable, for the
    same reason as fetch_raven_stats."""
    try:
        body, last_modified = _fetch_text(HYAK_ALLOC_URL, timeout)
    except (urllib.error.URLError, socket.timeout, OSError):
        return None
    stats = parse_hyakalloc(body, last_modified)
    if not stats:
        return None
    stats["raw"] = body

    # One small entry per dated copy, for the history charts. Same 30-day
    # window and directory-index approach as gannet's history.
    history = []
    try:
        index, _ = _fetch_text(GANNET_REPORT_DIR, timeout)
        dated = sorted(set(_DATED_HYAK.findall(index)), key=lambda x: x[1])
    except (urllib.error.URLError, socket.timeout, OSError):
        dated = []
    for name, date in dated[-GANNET_HISTORY_DAYS:]:
        try:
            text, _ = _fetch_text(GANNET_REPORT_DIR + name, timeout)
        except (urllib.error.URLError, socket.timeout, OSError):
            continue
        parsed = parse_hyakalloc(text)
        if parsed:
            history.append(_hyak_history_point(date, parsed))
    stats["history"] = history
    return stats


def _hyak_history_point(date, stats):
    partitions = {}
    for p in stats["partitions"]:
        total, used = p["total"], p.get("used", {})
        partitions[p["account"] + "/" + p["partition"]] = {
            "cpus": used.get("cpus"),
            "cpus_total": total["cpus"],
            "memory_gb": used.get("memory_gb"),
            "memory_total_gb": total["memory_gb"],
        }
    checkpoint = stats.get("checkpoint") or {}
    return {
        "date": date,
        "partitions": partitions,
        "checkpoint_idle_cpus": checkpoint.get("idle_cpus"),
    }


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
        # Only when publishing: the history file sits next to the --out file
        # on the server-status branch (see update_raven_history).
        if args.out:
            update_raven_history(
                os.path.join(os.path.dirname(args.out) or ".", "raven_history.json"),
                raven_stats,
            )

    # Same reasoning as raven_stats: a daily report, merged on its own
    # "generated" timestamp by the page, so it stays out of "hosts".
    gannet_stats = fetch_gannet_stats(args.timeout)
    if gannet_stats:
        document["gannet_stats"] = gannet_stats

    # Same again for klone's daily hyakalloc snapshot.
    hyak_stats = fetch_hyak_stats(args.timeout)
    if hyak_stats:
        document["hyak_stats"] = hyak_stats
    text = json.dumps(document, indent=2, sort_keys=True)

    if args.out:
        with open(args.out, "w") as handle:
            handle.write(text + "\n")
        print("wrote {}".format(args.out), file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
