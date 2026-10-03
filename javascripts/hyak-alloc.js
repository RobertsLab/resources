/*
 * Klone allocation table for the Computing Hardware page
 * ([data-hyak-alloc]).
 *
 * A scrontab job on klone runs `hyakalloc` at 06:00 Pacific and copies the
 * output to gannet (https://gannet.fish.washington.edu/v1_web/owlshell/hyakalloc.txt).
 * The probers in scripts/ parse it into doc.hyak_stats and relay it through
 * the server-status branch, because gannet does not send CORS headers. See
 * scripts/README.md.
 *
 * Like raven_stats and gannet_stats, the freshest copy wins by its own
 * "generated" timestamp, not by which prober ran last.
 */
(function () {
  "use strict";

  // Daily snapshot: same 30-hour threshold as the other daily reports.
  var STALE_MS = 30 * 60 * 60 * 1000;
  var SOURCES = ["internal.json", "external.json"];

  function fetchSource(base, name) {
    return fetch(base + "/" + name + "?t=" + Date.now(), { cache: "no-store" })
      .then(function (res) {
        return res.ok ? res.json() : null;
      })
      .catch(function () {
        return null;
      });
  }

  function mergeStats(docs) {
    var best = null;
    docs.forEach(function (doc) {
      if (!doc || !doc.hyak_stats) return;
      var at = Date.parse(doc.hyak_stats.generated);
      if (isNaN(at)) return;
      if (best && best.generatedAt >= at) return;
      best = doc.hyak_stats;
      best.generatedAt = at;
    });
    return best;
  }

  function relativeTime(then, now) {
    var mins = Math.round((now - then) / 60000);
    if (mins < 1) return "just now";
    if (mins < 60) return mins + " min ago";
    var hrs = Math.round(mins / 60);
    if (hrs < 24) return hrs + " hr ago";
    var days = Math.round(hrs / 24);
    return days === 1 ? "1 day ago" : days + " days ago";
  }

  // Same thresholds and classes as raven's disk table: at 90%+ in use a
  // new job will likely sit in the queue.
  function fullnessClass(percent) {
    if (percent >= 90) return "ss-disk-critical";
    if (percent >= 75) return "ss-disk-warn";
    return "";
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  // "28 / 32" with a bar showing the share in use; free goes in the tooltip.
  function usageCell(used, total, free, unit) {
    var td = el("td", "ss-disk-pct");
    if (used == null || !total) {
      td.textContent = "—";
      return td;
    }
    var pct = Math.round((100 * used) / total);
    td.className += " " + fullnessClass(pct);
    td.title = pct + "% in use, " + free + unit + " free";
    var bar = el("span", "ss-bar");
    var fill = el("span", "ss-bar-fill");
    fill.style.width = Math.min(pct, 100) + "%";
    bar.appendChild(fill);
    td.appendChild(bar);
    td.appendChild(el("span", "ss-bar-label", used + " / " + total + unit));
    return td;
  }

  function paint(container, stats, now) {
    container.innerHTML = "";

    if (!stats || !stats.partitions || !stats.partitions.length) {
      container.appendChild(el("p", null, "No hyakalloc snapshot available yet."));
      return;
    }

    var stale = now - stats.generatedAt > STALE_MS;
    var bits = [];
    if (stats.checkpoint) {
      bits.push(
        "Checkpoint (ckpt) idle: " +
          stats.checkpoint.idle_cpus +
          " CPUs, " +
          stats.checkpoint.idle_gpus +
          " GPUs"
      );
    }
    bits.push(
      "snapshot from " +
        new Date(stats.generatedAt).toLocaleString() +
        " (" +
        relativeTime(stats.generatedAt, now) +
        ")"
    );
    if (stale) bits.push("stale — the hyakalloc job on klone may have stopped");
    var meta = el("p", "ss-raven-meta", bits.join(" · "));
    meta.classList.toggle("ss-stats-stale", stale);
    container.appendChild(meta);

    // GPUs only get a column if some partition actually has them.
    var hasGpus = stats.partitions.some(function (p) {
      return p.total && p.total.gpus > 0;
    });

    var table = el("table");
    var head = el("tr");
    ["Account", "Partition", "CPUs in use", "Memory in use"]
      .concat(hasGpus ? ["GPUs in use"] : [])
      .forEach(function (h) {
        head.appendChild(el("th", null, h));
      });
    var thead = el("thead");
    thead.appendChild(head);
    table.appendChild(thead);

    var tbody = el("tbody");
    stats.partitions.forEach(function (p) {
      var used = p.used || {};
      var free = p.free || {};
      var tr = el("tr");
      tr.appendChild(el("td", null, p.account));
      tr.appendChild(el("td", "ss-mount", p.partition));
      tr.appendChild(usageCell(used.cpus, p.total.cpus, free.cpus, ""));
      tr.appendChild(
        usageCell(
          used.memory_gb != null ? Math.round(used.memory_gb) : null,
          Math.round(p.total.memory_gb || 0),
          free.memory_gb != null ? Math.round(free.memory_gb) : "?",
          "G"
        )
      );
      if (hasGpus) {
        tr.appendChild(usageCell(used.gpus, p.total.gpus, free.gpus, ""));
      }
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    container.appendChild(table);
    paintHistory(container, stats);
  }

  var SERIES_CLS = ["gh-s1", "gh-s2", "gh-s3"];

  // One chart per resource, one line per partition, as % of that
  // partition's total. Built from the dated hyakalloc_YYYY-MM-DD.txt copies.
  function paintHistory(container, stats) {
    var charts = window.RobertsLabCharts;
    var history = stats.history || [];
    if (!charts || !history.length) return;

    var dates = history.map(function (h) { return h.date; });
    var keys = stats.partitions.map(function (p) {
      return p.account + "/" + p.partition;
    });

    function seriesFor(usedKey, totalKey) {
      return keys.slice(0, SERIES_CLS.length).map(function (key, k) {
        var pts = [];
        history.forEach(function (h, i) {
          var p = h.partitions && h.partitions[key];
          if (!p || p[usedKey] == null || !p[totalKey]) return;
          var pct = Math.round((100 * p[usedKey]) / p[totalKey]);
          // Just the %, so the direct label fits beside the chart; the table
          // above has the absolute numbers.
          pts.push({ x: i, y: pct, label: pct + "%" });
        });
        // Direct labels use the partition name only; the account is in the
        // legend and the tooltip.
        return { name: key.split("/")[1], cls: SERIES_CLS[k], points: pts, key: key };
      }).filter(function (s) { return s.points.length; });
    }

    var details = el("details", "hy-history");
    details.appendChild(el("summary", null, "Usage history"));

    var legendSeries = seriesFor("cpus", "cpus_total");
    var legend = el("div", "gh-legend");
    legendSeries.forEach(function (s) {
      var item = el("span", "gh-legend-item");
      item.appendChild(el("span", "gh-swatch " + s.cls));
      item.appendChild(document.createTextNode(s.key));
      legend.appendChild(item);
    });
    details.appendChild(legend);

    [
      ["CPUs in use", "cpus", "cpus_total"],
      ["Memory in use", "memory_gb", "memory_total_gb"]
    ].forEach(function (c) {
      var series = seriesFor(c[1], c[2]);
      if (!series.length) return;
      details.appendChild(el("h4", null, c[0] + " (% of partition)"));
      details.appendChild(
        charts.lineChart(dates, series, {
          yMax: 100,
          unit: "%",
          right: 150,
          label: c[0] + " per partition by day"
        })
      );
    });
    details.appendChild(charts.historyNote(history));
    container.appendChild(details);
  }

  function render() {
    var container = document.querySelector("[data-hyak-alloc]");
    if (!container) return;
    var base = container.getAttribute("data-status-base");
    Promise.all(
      SOURCES.map(function (name) {
        return fetchSource(base, name);
      })
    ).then(function (docs) {
      paint(container, mergeStats(docs), Date.now());
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }

  // Re-render on mkdocs-material instant navigation.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(render);
  }
})();
