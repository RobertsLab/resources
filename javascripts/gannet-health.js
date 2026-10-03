/*
 * Gannet daily health report, on two pages:
 *
 *   Computing Hardware  - the "Daily health" cell in the status table
 *                         ([data-health="gannet"]) and the compact
 *                         "Gannet Health" section ([data-gannet-summary]).
 *   Gannet Dashboard    - the full dashboard ([data-gannet-dashboard]).
 *
 * The report itself is written once a day on gannet by gannet_health.sh
 * (https://gannet.fish.washington.edu/v1_web/owlshell/latest.txt). The
 * probers in scripts/ parse it into doc.gannet_stats and relay it through the
 * server-status branch, because gannet does not send CORS headers and the
 * page cannot fetch the text file directly. See scripts/README.md.
 *
 * Like raven_stats, the freshest copy wins by its own "generated" timestamp,
 * not by which prober ran last.
 */
(function () {
  "use strict";

  // Daily report: 30 hours clears normal day-to-day slip in when the cron
  // fires while still catching a stuck job within about a day.
  var STALE_MS = 30 * 60 * 60 * 1000;
  var SOURCES = ["internal.json", "external.json"];
  var DEFAULT_BASE =
    "https://raw.githubusercontent.com/RobertsLab/resources/server-status/status";
  var REPORT_URL = "https://gannet.fish.washington.edu/v1_web/owlshell/latest.txt";
  var SVG_NS = "http://www.w3.org/2000/svg";

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
      if (!doc || !doc.gannet_stats) return;
      var at = Date.parse(doc.gannet_stats.generated);
      if (isNaN(at)) return;
      if (best && best.generatedAt >= at) return;
      best = doc.gannet_stats;
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

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function fullnessClass(pct) {
    if (pct >= 90) return "ss-disk-critical";
    if (pct >= 75) return "ss-disk-warn";
    return "";
  }

  function alertClass(level) {
    if (level === "critical") return "gh-critical";
    if (level === "warning" || level === "warn") return "gh-warning";
    return "gh-info";
  }

  // The worst alert decides the overall state; words carry it, color helps.
  function overall(stats) {
    var alerts = stats.alerts || [];
    if (alerts.some(function (a) { return a.level === "critical"; })) {
      return { cls: "ss-down", label: "critical" };
    }
    if (alerts.length) return { cls: "gh-dot-warn", label: "warning" };
    return { cls: "ss-up", label: "healthy" };
  }

  function metaText(stats, now) {
    var stale = now - stats.generatedAt > STALE_MS;
    var text =
      "Report generated " +
      new Date(stats.generatedAt).toLocaleString() +
      " (" +
      relativeTime(stats.generatedAt, now) +
      ")";
    if (stale) text += " · stale — the report cron on gannet may have stopped";
    return { text: text, stale: stale };
  }

  function barCell(pct) {
    var td = el("td", "ss-disk-pct " + (pct == null ? "" : fullnessClass(pct)));
    if (pct == null) {
      td.textContent = "—";
      return td;
    }
    var bar = el("span", "ss-bar");
    var fill = el("span", "ss-bar-fill");
    fill.style.width = pct + "%";
    bar.appendChild(fill);
    td.appendChild(bar);
    td.appendChild(el("span", "ss-bar-label", pct + "%"));
    return td;
  }

  function table(headers, rows) {
    // No class: mkdocs-material only styles table:not([class]).
    var t = el("table");
    var thead = el("thead");
    var tr = el("tr");
    headers.forEach(function (h) { tr.appendChild(el("th", null, h)); });
    thead.appendChild(tr);
    t.appendChild(thead);
    var tbody = el("tbody");
    rows.forEach(function (row) { tbody.appendChild(row); });
    t.appendChild(tbody);
    return t;
  }

  function row(cells) {
    var tr = el("tr");
    cells.forEach(function (c) {
      tr.appendChild(c instanceof Node ? c : el("td", null, c == null ? "—" : String(c)));
    });
    return tr;
  }

  function alertList(stats) {
    var alerts = stats.alerts || [];
    if (!alerts.length) return el("p", "gh-ok", "✓ No alerts in the latest report.");
    var ul = el("ul", "gh-alerts");
    alerts.forEach(function (a) {
      var li = el("li", alertClass(a.level));
      li.appendChild(el("strong", null, a.level.toUpperCase()));
      li.appendChild(document.createTextNode(" " + a.message));
      ul.appendChild(li);
    });
    return ul;
  }

  function diskTable(stats, withInodes) {
    var disks = (stats.disks || []).slice().sort(function (a, b) {
      return b.use_percent - a.use_percent;
    });
    var headers = ["Mount", "Size", "Used", "Available", "% Full"];
    if (withInodes) headers.push("Inodes");
    return table(
      headers,
      disks.map(function (d) {
        var mount = el("td", "ss-mount", d.mount);
        mount.title = d.filesystem + (d.type ? " (" + d.type + ")" : "");
        var cells = [mount, d.size, d.used, d.available, barCell(d.use_percent)];
        if (withInodes) cells.push(d.inode_percent == null ? "—" : d.inode_percent + "%");
        return row(cells);
      })
    );
  }

  // Report lines look like "/dev/sda  health=PASSED  temp=32C realloc=0 pending=0";
  // "?" means smartctl did not report that attribute for the drive.
  function parseSmartLine(line) {
    var fields = line.trim().split(/\s+/);
    if (!fields.length || fields[0].indexOf("/dev/") !== 0) return null;
    var drive = { device: fields[0] };
    fields.slice(1).forEach(function (f) {
      var kv = f.split("=");
      if (kv.length !== 2) return;
      var v = kv[1].replace(/C$/, "");
      drive[kv[0]] = v === "?" || v === "" ? null : v;
    });
    return drive;
  }

  function countCell(value) {
    if (value == null) return el("td", "gh-muted", "not reported");
    var n = Number(value);
    if (isNaN(n)) return el("td", null, value);
    return el("td", n > 0 ? "gh-critical" : "gh-ok", n > 0 ? "⚠ " + n : "0");
  }

  function smartSection(parent, lines) {
    var drives = lines.map(parseSmartLine).filter(Boolean);
    if (!drives.length) {
      parent.appendChild(el("pre", null, lines.join("\n")));
      return;
    }
    var failing = drives.filter(function (d) { return d.health && d.health !== "PASSED"; });
    var missing = drives.filter(function (d) { return d.temp == null && d.realloc == null && d.pending == null; });

    parent.appendChild(
      el(
        "p",
        failing.length ? "gh-critical" : "gh-ok",
        failing.length
          ? "✗ " + failing.length + " of " + drives.length + " drives fail their SMART self-check."
          : "✓ All " + drives.length + " drives pass their SMART self-check."
      )
    );

    parent.appendChild(
      table(
        ["Drive", "Self-check", "Temperature", "Reallocated sectors", "Pending sectors"],
        drives.map(function (d) {
          var h = d.health;
          var healthCell = el("td", h == null ? "gh-muted" : h === "PASSED" ? "gh-ok" : "gh-critical",
            h == null ? "not reported" : h === "PASSED" ? "✓ passed" : "✗ " + h.toLowerCase());
          var temp = d.temp == null ? el("td", "gh-muted", "not reported") : el("td", null, d.temp + " °C");
          return row([d.device, healthCell, temp, countCell(d.realloc), countCell(d.pending)]);
        })
      )
    );

    var note =
      "Self-check is the drive's own pass/fail verdict. Reallocated sectors are bad spots the drive " +
      "has already swapped out; pending sectors are spots it is unsure about. Both should stay at 0, " +
      "and a rising count is an early sign the drive is wearing out.";
    if (missing.length) {
      note +=
        " " + missing.length + " of " + drives.length + " drives give only the pass/fail verdict " +
        "(\"not reported\"): the health script found no temperature or sector counts for them, which " +
        "usually means the drive reports these values under different names or through a RAID controller.";
    }
    parent.appendChild(el("p", "gh-note", note));
  }

  // ---- Computing Hardware page -------------------------------------------

  function paintHealthCell(cell, stats, now) {
    cell.innerHTML = "";
    if (!stats) {
      cell.textContent = "no report yet";
      return;
    }
    var state = overall(stats);
    var link = el("a");
    link.href = cell.getAttribute("data-dashboard") || "../Gannet-Dashboard/";
    link.appendChild(el("span", "ss-dot " + state.cls));
    var alerts = stats.alerts || [];
    link.appendChild(
      el(
        "span",
        "ss-label",
        alerts.length
          ? alerts.length + (alerts.length === 1 ? " alert" : " alerts") + ": " + alerts[0].message
          : "no alerts"
      )
    );
    cell.appendChild(link);
    cell.title = metaText(stats, now).text;
  }

  function paintSummary(root, stats, now) {
    root.innerHTML = "";
    if (!stats) {
      root.appendChild(el("p", null, "No gannet health report available yet."));
      return;
    }
    var meta = metaText(stats, now);
    var bits = [meta.text];
    if (stats.uptime) bits.push("up " + stats.uptime);
    if (stats.load) bits.push("load " + stats.load.join(" / ") + (stats.cpu_cores ? " on " + stats.cpu_cores + " cores" : ""));
    root.appendChild(el("p", "ss-raven-meta" + (meta.stale ? " ss-stats-stale" : ""), bits.join(" · ")));
    root.appendChild(alertList(stats));
    root.appendChild(diskTable(stats, false));
  }

  // ---- Dashboard ---------------------------------------------------------

  function tile(label, value, sub, cls) {
    var t = el("div", "gh-tile " + (cls || ""));
    t.appendChild(el("div", "gh-tile-label", label));
    t.appendChild(el("div", "gh-tile-value", value));
    if (sub) t.appendChild(el("div", "gh-tile-sub", sub));
    return t;
  }

  function section(root, title) {
    var s = el("section", "gh-section");
    s.appendChild(el("h2", null, title));
    root.appendChild(s);
    return s;
  }

  function svg(tag, attrs) {
    var node = document.createElementNS(SVG_NS, tag);
    Object.keys(attrs || {}).forEach(function (k) { node.setAttribute(k, attrs[k]); });
    return node;
  }

  /*
   * Small line chart. series: [{name, cls, points: [{x: index, y, label}]}].
   * yMax fixes the scale (100 for percentages); ref draws a dashed reference
   * line (e.g. CPU core count for load). right widens the right margin for
   * longer direct labels. One y-axis only.
   */
  function lineChart(dates, series, opts) {
    var W = 640, H = 200, L = 40, R = opts.right || 90, T = 12, B = 28;
    var yMax = opts.yMax;
    if (yMax == null) {
      yMax = 1;
      series.forEach(function (s) {
        s.points.forEach(function (p) { if (p.y > yMax) yMax = p.y; });
      });
      if (opts.ref != null && opts.ref > yMax) yMax = opts.ref;
      yMax = Math.ceil(yMax * 1.15);
    }
    var n = dates.length;
    function x(i) { return n <= 1 ? L + (W - L - R) / 2 : L + (i * (W - L - R)) / (n - 1); }
    function y(v) { return T + (H - T - B) * (1 - v / yMax); }

    var chart = svg("svg", {
      viewBox: "0 0 " + W + " " + H,
      class: "gh-chart",
      role: "img",
      "aria-label": opts.label
    });

    [0, 0.5, 1].forEach(function (f) {
      var v = Math.round(yMax * f);
      chart.appendChild(svg("line", { x1: L, x2: W - R, y1: y(v), y2: y(v), class: "gh-grid" }));
      var t = svg("text", { x: L - 6, y: y(v) + 4, class: "gh-axis", "text-anchor": "end" });
      t.textContent = v + (opts.unit || "");
      chart.appendChild(t);
    });

    if (opts.ref != null) {
      chart.appendChild(svg("line", { x1: L, x2: W - R, y1: y(opts.ref), y2: y(opts.ref), class: "gh-ref" }));
      var rt = svg("text", { x: W - R + 6, y: y(opts.ref) + 4, class: "gh-axis" });
      rt.textContent = opts.refLabel;
      chart.appendChild(rt);
    }

    [0, n - 1].forEach(function (i, k) {
      if (k === 1 && n <= 1) return;
      var t = svg("text", { x: x(i), y: H - 8, class: "gh-axis", "text-anchor": k ? "end" : "start" });
      if (n <= 1) t.setAttribute("text-anchor", "middle");
      t.textContent = dates[i];
      chart.appendChild(t);
    });

    var directLabels = [];
    series.forEach(function (s) {
      var pts = s.points;
      if (pts.length > 1) {
        chart.appendChild(
          svg("polyline", {
            points: pts.map(function (p) { return x(p.x) + "," + y(p.y); }).join(" "),
            class: "gh-line " + s.cls
          })
        );
      }
      pts.forEach(function (p) {
        var dot = svg("circle", { cx: x(p.x), cy: y(p.y), r: 4, class: "gh-point " + s.cls });
        var title = svg("title");
        title.textContent = s.name + " · " + dates[p.x] + ": " + p.label;
        dot.appendChild(title);
        chart.appendChild(dot);
        // Bigger invisible hit target for the tooltip.
        var hit = svg("circle", { cx: x(p.x), cy: y(p.y), r: 10, class: "gh-hit" });
        hit.appendChild(title.cloneNode(true));
        chart.appendChild(hit);
      });
      // Direct label at the last point so identity is never color alone.
      var last = pts[pts.length - 1];
      if (last) {
        var lbl = svg("text", { x: x(last.x) + 8, class: "gh-direct" });
        lbl.textContent = s.name + " " + last.label;
        chart.appendChild(lbl);
        directLabels.push({ node: lbl, y: y(last.y) + 4 });
      }
    });
    // Push direct labels apart vertically so lines ending at similar
    // values do not print on top of each other.
    directLabels.sort(function (a, b) { return a.y - b.y; });
    directLabels.forEach(function (d, i) {
      if (i && d.y < directLabels[i - 1].y + 13) d.y = directLabels[i - 1].y + 13;
      d.node.setAttribute("y", d.y);
    });
    return chart;
  }

  function historyNote(history) {
    return el(
      "p",
      "gh-note",
      history.length < 2
        ? "History fills in as daily reports accumulate (" + history.length + " day so far). Hover a point for its value."
        : "Last " + history.length + " daily reports. Hover a point for its value."
    );
  }

  function paintDashboard(root, stats, now) {
    root.innerHTML = "";
    if (!stats) {
      root.appendChild(el("p", null, "No gannet health report available yet."));
      return;
    }

    var meta = metaText(stats, now);
    var head = el("p", "ss-raven-meta" + (meta.stale ? " ss-stats-stale" : ""));
    head.appendChild(document.createTextNode(meta.text + " · "));
    var raw = el("a", null, "raw report");
    raw.href = REPORT_URL;
    head.appendChild(raw);
    root.appendChild(head);

    // KPI tiles
    var tiles = el("div", "gh-tiles");
    var state = overall(stats);
    var alerts = stats.alerts || [];
    tiles.appendChild(
      tile("Overall", state.label, alerts.length + (alerts.length === 1 ? " alert" : " alerts"),
           state.label === "healthy" ? "gh-good" : state.label === "critical" ? "gh-critical" : "gh-warning")
    );
    var disks = (stats.disks || []).filter(function (d) { return d.mount !== "/"; });
    disks.sort(function (a, b) { return b.use_percent - a.use_percent; });
    disks.forEach(function (d) {
      var c = fullnessClass(d.use_percent);
      tiles.appendChild(
        tile(d.mount, d.use_percent + "% full", d.available + " free of " + d.size,
             c === "ss-disk-critical" ? "gh-critical" : c === "ss-disk-warn" ? "gh-warning" : "")
      );
    });
    if (stats.load) {
      var cores = stats.cpu_cores;
      tiles.appendChild(
        tile("Load (15 min)", String(stats.load[2]),
             cores ? "on " + cores + " cores" : "",
             cores && stats.load[2] > cores ? "gh-warning" : "")
      );
    }
    if (stats.memory && stats.memory.mem) {
      var m = stats.memory.mem;
      tiles.appendChild(tile("Memory available", m.available || m.free, "of " + m.total));
    }
    var raid = stats.raid || [];
    if (raid.length) {
      var ok = raid.filter(function (a) { return a.healthy; }).length;
      tiles.appendChild(
        tile("RAID arrays", ok + " / " + raid.length + " healthy", "", ok === raid.length ? "gh-good" : "gh-critical")
      );
    }
    if (stats.uptime) tiles.appendChild(tile("Uptime", stats.uptime, ""));
    root.appendChild(tiles);

    section(root, "Alerts").appendChild(alertList(stats));

    var storage = section(root, "Storage");
    storage.appendChild(diskTable(stats, true));

    var history = stats.history || [];
    var dates = history.map(function (h) { return h.date; });
    var volumes = ["/volume2", "/volume1"];
    var volCls = ["gh-s1", "gh-s2"];
    var volSeries = volumes.map(function (mount, k) {
      var pts = [];
      history.forEach(function (h, i) {
        if (h.disks && h.disks[mount] != null) pts.push({ x: i, y: h.disks[mount], label: h.disks[mount] + "%" });
      });
      return { name: mount, cls: volCls[k], points: pts };
    }).filter(function (s) { return s.points.length; });
    if (volSeries.length) {
      storage.appendChild(el("h3", null, "Volume use over time"));
      var legend = el("div", "gh-legend");
      volSeries.forEach(function (s) {
        var item = el("span", "gh-legend-item");
        item.appendChild(el("span", "gh-swatch " + s.cls));
        item.appendChild(document.createTextNode(s.name));
        legend.appendChild(item);
      });
      storage.appendChild(legend);
      storage.appendChild(lineChart(dates, volSeries, { yMax: 100, unit: "%", label: "Percent full per volume by day" }));
      storage.appendChild(historyNote(history));
    }

    var sys = section(root, "System");
    var loadPts = [];
    history.forEach(function (h, i) {
      if (h.load) loadPts.push({ x: i, y: h.load[2], label: String(h.load[2]) });
    });
    if (loadPts.length) {
      sys.appendChild(el("h3", null, "15-minute load average over time"));
      sys.appendChild(
        lineChart(dates, [{ name: "load", cls: "gh-s1", points: loadPts }], {
          ref: stats.cpu_cores,
          refLabel: stats.cpu_cores ? stats.cpu_cores + " cores" : "",
          label: "15-minute load average by day"
        })
      );
      sys.appendChild(historyNote(history));
    }
    if (stats.memory) {
      sys.appendChild(el("h3", null, "Memory"));
      var mem = stats.memory;
      var memRows = [];
      if (mem.mem) memRows.push(row(["RAM", mem.mem.total, mem.mem.used, mem.mem.free, mem.mem.available]));
      if (mem.swap) memRows.push(row(["Swap", mem.swap.total, mem.swap.used, mem.swap.free, null]));
      sys.appendChild(table(["", "Total", "Used", "Free", "Available"], memRows));
    }

    if (raid.length) {
      var rs = section(root, "RAID");
      rs.appendChild(
        table(
          ["Array", "Level", "State", "Members", "Health"],
          raid.map(function (a) {
            var h = el("td", a.healthy ? "gh-ok" : "gh-critical", a.healthy ? "✓ all members up" : "✗ degraded");
            return row([a.name, a.level, a.state, a.active + " / " + a.members, h]);
          })
        )
      );
    }

    var svc = section(root, "Services");
    svc.appendChild(
      table(
        ["Service", "State"],
        (stats.services || []).map(function (s) {
          return row([s.name, el("td", s.state === "active" ? "gh-ok" : "gh-critical", s.state)]);
        })
      )
    );
    var failed = stats.failed_units || [];
    svc.appendChild(el("h3", null, "Failed systemd units"));
    if (failed.length) {
      svc.appendChild(
        table(["Unit", "Description"], failed.map(function (f) { return row([f.unit, f.description]); }))
      );
    } else {
      svc.appendChild(el("p", "gh-ok", "✓ None."));
    }

    var logs = section(root, "Kernel errors (last 24 h)");
    var kernel = stats.kernel_errors || [];
    if (kernel.length) {
      logs.appendChild(el("pre", null, kernel.join("\n")));
    } else {
      logs.appendChild(el("p", "gh-ok", "✓ None."));
    }
    if (stats.smart && stats.smart.length) {
      var smart = section(root, "Drive health (SMART)");
      smartSection(smart, stats.smart);
    }

    if (stats.raw) {
      var details = el("details", "gh-raw");
      details.appendChild(el("summary", null, "Full text of the latest report"));
      details.appendChild(el("pre", null, stats.raw));
      root.appendChild(details);
    }
  }

  function render() {
    var cells = document.querySelectorAll('[data-health="gannet"]');
    var summary = document.querySelector("[data-gannet-summary]");
    var dashboard = document.querySelector("[data-gannet-dashboard]");
    if (!cells.length && !summary && !dashboard) return;

    var holder = dashboard || summary;
    var base = (holder && holder.getAttribute("data-status-base")) || DEFAULT_BASE;

    Promise.all(SOURCES.map(function (n) { return fetchSource(base, n); })).then(function (docs) {
      var stats = mergeStats(docs);
      var now = Date.now();
      Array.prototype.forEach.call(cells, function (c) { paintHealthCell(c, stats, now); });
      if (summary) paintSummary(summary, stats, now);
      if (dashboard) paintDashboard(dashboard, stats, now);
    });
  }

  // Shared with hyak-alloc.js, which loads after this file.
  window.RobertsLabCharts = { lineChart: lineChart, historyNote: historyNote };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(render);
  }
})();
