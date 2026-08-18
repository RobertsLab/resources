/*
 * Server status lights for the Computing Hardware page.
 *
 * Reads JSON written by the probers in scripts/ (see scripts/README.md) and
 * fills in the status table. Two sources are merged:
 *
 *   internal.json - cron on a machine inside the UW network. Only source that
 *                   can see raven, which is not in public DNS.
 *   external.json - scheduled GitHub Action. Sees gannet and klone from the
 *                   public internet. Acts as a backstop if the internal
 *                   prober host is itself down.
 *
 * For each host the most recent fresh reading wins. Anything older than
 * STALE_MS is reported as unknown rather than shown as a stale green light.
 *
 * Raven also gets a disk/CPU snapshot (doc.raven_stats) parsed by the
 * checker from a daily log raven drops on gannet's public web root -- see
 * scripts/README.md. It is generated once a day around 7am, so it is merged
 * separately from the up/down lights: the freshest *snapshot* wins by its
 * own "generated" timestamp, not by which prober ran most recently.
 */
(function () {
  "use strict";

  // Sized against what the probers actually deliver, not what they ask for.
  // The GitHub Action requests */15 but is scheduled best-effort: across 20
  // consecutive runs the observed gaps were 30-71 min (median 46), so every
  // single interval blew through the original 30 min threshold and the lights
  // sat at "unknown" most of each cycle. 90 min clears the worst observed gap
  // with headroom. Once the in-network cron is running every 10 min it becomes
  // the freshest source and this ceiling stops mattering in practice.
  var STALE_MS = 90 * 60 * 1000;

  // The snapshot regenerates roughly once a day. 30 hours clears a normal
  // day-to-day slip in when the raven cron fires while still catching a
  // genuinely stuck job within about a day of it stalling.
  var STATS_STALE_MS = 30 * 60 * 60 * 1000;

  var SOURCES = ["internal.json", "external.json"];

  function fetchSource(base, name) {
    // Cache-bust: raw.githubusercontent.com serves with max-age=300.
    var url = base + "/" + name + "?t=" + Date.now();
    return fetch(url, { cache: "no-store" })
      .then(function (res) {
        return res.ok ? res.json() : null;
      })
      .catch(function () {
        return null; // source may not exist yet, or network is down
      });
  }

  // Flatten both documents into { host: bestReading }.
  function mergeReadings(docs) {
    var best = {};
    docs.forEach(function (doc) {
      if (!doc || !doc.hosts) return;
      var checkedAt = Date.parse(doc.checked);
      if (isNaN(checkedAt)) return;
      Object.keys(doc.hosts).forEach(function (host) {
        var current = best[host];
        if (current && current.checkedAt >= checkedAt) return;
        best[host] = {
          up: doc.hosts[host].up === true,
          detail: doc.hosts[host].detail || "",
          latencyMs: doc.hosts[host].latency_ms,
          source: doc.source || "unknown",
          checkedAt: checkedAt
        };
      });
    });
    return best;
  }

  // Picks the newest raven_stats block across sources by its own
  // "generated" timestamp (when the snapshot was written on raven), not by
  // which document is freshest -- both probers just relay the same daily
  // file, so whichever last saw a newer copy of it wins.
  function mergeRavenStats(docs) {
    var best = null;
    docs.forEach(function (doc) {
      if (!doc || !doc.raven_stats) return;
      var generatedAt = Date.parse(doc.raven_stats.generated);
      if (isNaN(generatedAt)) return;
      if (best && best.generatedAt >= generatedAt) return;
      best = {
        cpuPercent: doc.raven_stats.cpu_percent,
        disks: doc.raven_stats.disks || [],
        generatedAt: generatedAt
      };
    });
    return best;
  }

  function relativeTime(then, now) {
    var mins = Math.round((now - then) / 60000);
    if (mins < 1) return "just now";
    if (mins === 1) return "1 min ago";
    if (mins < 60) return mins + " min ago";
    var hrs = Math.round(mins / 60);
    if (hrs === 1) return "1 hr ago";
    if (hrs < 24) return hrs + " hr ago";
    var days = Math.round(hrs / 24);
    return days === 1 ? "1 day ago" : days + " days ago";
  }

  function paintRow(row, reading, now) {
    var stateCell = row.querySelector(".ss-state");
    var timeCell = row.querySelector(".ss-time");
    if (!stateCell || !timeCell) return;

    var cls, label, title;

    if (!reading) {
      cls = "ss-unknown";
      label = "unknown";
      title = "No status data available for this host yet.";
      timeCell.textContent = "—";
    } else if (now - reading.checkedAt > STALE_MS) {
      cls = "ss-unknown";
      label = "unknown";
      title =
        "Last reading is stale (" +
        relativeTime(reading.checkedAt, now) +
        ") — the prober itself may be down.";
      timeCell.textContent = relativeTime(reading.checkedAt, now);
    } else {
      cls = reading.up ? "ss-up" : "ss-down";
      label = reading.up ? "up" : "not responding";
      title =
        reading.detail +
        (reading.latencyMs != null ? " (" + reading.latencyMs + " ms)" : "") +
        " — checked by " +
        reading.source +
        " prober";
      timeCell.textContent = relativeTime(reading.checkedAt, now);
    }

    stateCell.innerHTML = "";
    var dot = document.createElement("span");
    dot.className = "ss-dot " + cls;
    var text = document.createElement("span");
    text.className = "ss-label";
    text.textContent = label; // never color alone: the word carries the meaning
    stateCell.appendChild(dot);
    stateCell.appendChild(text);
    stateCell.title = title;
  }

  // Last path segment, e.g. "/home/shared/8TB_HDD_02" -> "8TB_HDD_02".
  function mountLabel(mount) {
    var parts = mount.split("/");
    return parts[parts.length - 1] || mount;
  }

  function paintStats(row, stats, now) {
    var cell = row.querySelector(".ss-stats");
    if (!cell) return;

    if (!stats) {
      cell.textContent = "—";
      cell.title = "No disk/CPU snapshot available yet.";
      return;
    }

    var worst = null;
    stats.disks.forEach(function (disk) {
      if (!worst || disk.use_percent > worst.use_percent) worst = disk;
    });

    var parts = [];
    if (stats.cpuPercent != null) parts.push("CPU " + stats.cpuPercent + "%");
    if (worst) parts.push("disk " + worst.use_percent + "% (" + mountLabel(worst.mount) + ")");

    var stale = now - stats.generatedAt > STATS_STALE_MS;
    cell.textContent = (parts.length ? parts.join(" · ") : "—") + (stale ? " (stale)" : "");
    cell.classList.toggle("ss-stats-stale", stale);

    var titleLines = stats.disks.map(function (disk) {
      return disk.mount + ": " + disk.use_percent + "%";
    });
    cell.title =
      "Daily snapshot from " +
      new Date(stats.generatedAt).toLocaleString() +
      (stale
        ? " — more than 30h old; the snapshot cron on raven may have stopped."
        : "") +
      (titleLines.length ? "\n" + titleLines.join("\n") : "");
  }

  function render() {
    var table = document.querySelector("[data-status-base]");
    if (!table) return;
    var base = table.getAttribute("data-status-base");

    Promise.all(
      SOURCES.map(function (name) {
        return fetchSource(base, name);
      })
    ).then(function (docs) {
      var readings = mergeReadings(docs);
      var ravenStats = mergeRavenStats(docs);
      var now = Date.now();
      var rows = table.querySelectorAll("tr[data-host]");
      Array.prototype.forEach.call(rows, function (row) {
        var host = row.getAttribute("data-host");
        paintRow(row, readings[host], now);
        if (host === "raven") paintStats(row, ravenStats, now);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }

  // mkdocs-material swaps page content without a reload when instant
  // navigation is enabled, so re-render on those transitions too.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(render);
  }
})();
