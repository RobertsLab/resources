/*
 * Raven Dashboard ([data-raven-dashboard] on docs/Raven-Dashboard.md).
 *
 * Two inputs, both on the server-status branch (see scripts/README.md):
 *
 *   internal.json / external.json  doc.raven_stats, the latest parsed ghr.log
 *                                  snapshot (disks, CPU, memory, Winners,
 *                                  top memory processes).
 *   raven_history.json             one entry per day, accumulated by the
 *                                  probers, since raven keeps no dated
 *                                  copies of ghr.log.
 *
 * Every number here is a single sample taken when raven's cron runs each
 * morning, not a daily average.
 */
(function () {
  "use strict";

  var STALE_MS = 30 * 60 * 60 * 1000;
  var SOURCES = ["internal.json", "external.json"];
  var LOG_URL = "https://gannet.fish.washington.edu/v1_web/owlshell/bu-github/ghr.log";
  var SVG_NS = "http://www.w3.org/2000/svg";
  // Service accounts that show up in ps but are not people running jobs.
  var SYSTEM_USERS = ["root", "mysql", "rstudio+", "systemd+", "message+", "syslog", "daemon"];

  function fetchJson(base, name) {
    return fetch(base + "/" + name + "?t=" + Date.now(), { cache: "no-store" })
      .then(function (res) {
        return res.ok ? res.json() : null;
      })
      .catch(function () {
        return null;
      });
  }

  function latestStats(docs) {
    var best = null;
    docs.forEach(function (doc) {
      if (!doc || !doc.raven_stats) return;
      var at = Date.parse(doc.raven_stats.generated);
      if (isNaN(at)) return;
      if (best && best.generatedAt >= at) return;
      best = doc.raven_stats;
      best.generatedAt = at;
    });
    return best;
  }

  function relativeTime(then, now) {
    var mins = Math.round((now - then) / 60000);
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

  function svg(tag, attrs) {
    var node = document.createElementNS(SVG_NS, tag);
    Object.keys(attrs || {}).forEach(function (k) { node.setAttribute(k, attrs[k]); });
    return node;
  }

  function section(root, title) {
    var s = el("section", "gh-section");
    s.appendChild(el("h2", null, title));
    root.appendChild(s);
    return s;
  }

  function tile(label, value, sub, cls) {
    var t = el("div", "gh-tile " + (cls || ""));
    t.appendChild(el("div", "gh-tile-label", label));
    t.appendChild(el("div", "gh-tile-value", value));
    if (sub) t.appendChild(el("div", "gh-tile-sub", sub));
    return t;
  }

  function table(headers, rows) {
    var t = el("table");
    var thead = el("thead");
    var tr = el("tr");
    headers.forEach(function (h) { tr.appendChild(el("th", null, h)); });
    thead.appendChild(tr);
    t.appendChild(thead);
    var tbody = el("tbody");
    rows.forEach(function (cells) {
      var r = el("tr");
      cells.forEach(function (c) {
        r.appendChild(c instanceof Node ? c : el("td", null, c == null ? "—" : String(c)));
      });
      tbody.appendChild(r);
    });
    t.appendChild(tbody);
    return t;
  }

  function fullnessClass(pct) {
    if (pct >= 90) return "ss-disk-critical";
    if (pct >= 75) return "ss-disk-warn";
    return "";
  }

  function barCell(pct) {
    var td = el("td", "ss-disk-pct " + fullnessClass(pct));
    var bar = el("span", "ss-bar");
    var fill = el("span", "ss-bar-fill");
    fill.style.width = Math.min(pct, 100) + "%";
    bar.appendChild(fill);
    td.appendChild(bar);
    td.appendChild(el("span", "ss-bar-label", pct + "%"));
    return td;
  }

  function isSystem(user) {
    return SYSTEM_USERS.indexOf(user) !== -1;
  }

  function note(text) {
    return el("p", "gh-note", text);
  }

  /*
   * Who shows up in the Winners list, day by day. One row per user, one
   * column per snapshot; a filled square means the user was in that day's
   * top 5 by CPU, shaded by how much CPU they had. Rows sorted by number of
   * appearances, and the count is printed at the end of each row so the
   * shading is never the only carrier of meaning.
   */
  function occurrenceGrid(history) {
    var users = {};
    var cpuMax = 0;
    history.forEach(function (h, i) {
      (h.winners || []).forEach(function (w) {
        if (!users[w.user]) users[w.user] = { user: w.user, days: {}, count: 0 };
        users[w.user].days[i] = w;
        users[w.user].count += 1;
        if (w.cpu > cpuMax) cpuMax = w.cpu;
      });
    });
    var rows = Object.keys(users).map(function (k) { return users[k]; });
    rows.sort(function (a, b) {
      if (isSystem(a.user) !== isSystem(b.user)) return isSystem(a.user) ? 1 : -1;
      return b.count - a.count || a.user.localeCompare(b.user);
    });
    if (!rows.length) return null;

    var n = history.length;
    var L = 90, R = 70, T = 6, rowH = 18;
    var cell = Math.max(4, Math.min(16, Math.floor((640 - L - R) / n)));
    var W = L + n * cell + R;
    var H = T + rows.length * rowH + 22;

    var chart = svg("svg", {
      viewBox: "0 0 " + W + " " + H,
      class: "gh-chart rv-grid",
      style: "max-width:" + Math.max(W, 320) / 16 + "rem",
      role: "img",
      "aria-label": "Days each user appeared in raven's Winners list"
    });

    rows.forEach(function (r, ri) {
      var y = T + ri * rowH;
      var name = svg("text", { x: L - 8, y: y + 12, class: "gh-axis", "text-anchor": "end" });
      name.textContent = r.user;
      chart.appendChild(name);
      for (var i = 0; i < n; i++) {
        var w = r.days[i];
        var rect = svg("rect", {
          x: L + i * cell + 1,
          y: y + 2,
          width: cell - 2,
          height: rowH - 4,
          rx: 2,
          class: w ? (isSystem(r.user) ? "rv-on rv-system" : "rv-on") : "rv-off"
        });
        if (w) {
          // Shade from 35% to 100% opacity by CPU, so even a small entry is visible.
          var f = cpuMax > 0 ? w.cpu / cpuMax : 1;
          rect.setAttribute("fill-opacity", (0.35 + 0.65 * f).toFixed(2));
          var title = svg("title");
          title.textContent =
            r.user + " · " + history[i].date + ": " + w.cpu + "% CPU, " + w.mem_percent + "% memory";
          rect.appendChild(title);
        }
        chart.appendChild(rect);
      }
      var count = svg("text", { x: L + n * cell + 8, y: y + 12, class: "gh-direct" });
      count.textContent = r.count + (r.count === 1 ? " day" : " days");
      chart.appendChild(count);
    });

    var first = svg("text", { x: L, y: H - 6, class: "gh-axis" });
    first.textContent = history[0].date;
    chart.appendChild(first);
    if (n > 1) {
      var last = svg("text", { x: L + n * cell, y: H - 6, class: "gh-axis", "text-anchor": "end" });
      last.textContent = history[n - 1].date;
      chart.appendChild(last);
    }
    return chart;
  }

  function historyNote(history) {
    return note(
      history.length < 2
        ? "History started on " + (history[0] ? history[0].date : "—") +
          " and fills in one day at a time. Hover a point for its value."
        : history.length + " daily snapshots, " + history[0].date + " to " +
          history[history.length - 1].date + ". Hover a point for its value."
    );
  }

  function paint(root, stats, history, now) {
    root.innerHTML = "";
    var charts = window.RobertsLabCharts;
    history = history || [];

    if (!stats && !history.length) {
      root.appendChild(el("p", null, "No raven snapshot available yet."));
      return;
    }

    if (stats) {
      var stale = now - stats.generatedAt > STALE_MS;
      var head = el("p", "ss-raven-meta" + (stale ? " ss-stats-stale" : ""));
      head.appendChild(
        document.createTextNode(
          "Snapshot from " + new Date(stats.generatedAt).toLocaleString() +
            " (" + relativeTime(stats.generatedAt, now) + ")" +
            (stale ? " · stale — the snapshot cron on raven may have stopped" : "") +
            " · "
        )
      );
      var raw = el("a", null, "raw log");
      raw.href = LOG_URL;
      head.appendChild(raw);
      root.appendChild(head);

      var tiles = el("div", "gh-tiles");
      tiles.appendChild(tile("CPU in use", stats.cpu_percent != null ? stats.cpu_percent + "%" : "—", "all cores"));
      tiles.appendChild(tile("Memory in use", stats.memory_percent != null ? stats.memory_percent + "%" : "—", "of RAM"));
      var disks = (stats.disks || []).slice().sort(function (a, b) { return b.use_percent - a.use_percent; });
      if (disks[0]) {
        var c = fullnessClass(disks[0].use_percent);
        tiles.appendChild(
          tile("Fullest drive", disks[0].use_percent + "% full", disks[0].mount + " · " + disks[0].available + " free",
               c === "ss-disk-critical" ? "gh-critical" : c === "ss-disk-warn" ? "gh-warning" : "")
        );
      }
      var people = (stats.winners || []).filter(function (w) { return !isSystem(w.user); });
      tiles.appendChild(
        tile("Top user", people[0] ? people[0].user : "—", people[0] ? people[0].cpu + "% CPU" : "no user jobs")
      );
      root.appendChild(tiles);
    }

    // CPU and memory over time
    var load = section(root, "CPU and memory");
    var dates = history.map(function (h) { return h.date; });
    var series = [
      ["CPU", "cpu_percent", "gh-s1"],
      ["memory", "memory_percent", "gh-s2"]
    ].map(function (s) {
      var pts = [];
      history.forEach(function (h, i) {
        if (h[s[1]] != null) pts.push({ x: i, y: h[s[1]], label: h[s[1]] + "%" });
      });
      return { name: s[0], cls: s[2], points: pts };
    }).filter(function (s) { return s.points.length; });
    if (charts && series.length) {
      var legend = el("div", "gh-legend");
      series.forEach(function (s) {
        var item = el("span", "gh-legend-item");
        item.appendChild(el("span", "gh-swatch " + s.cls));
        item.appendChild(document.createTextNode(s.name));
        legend.appendChild(item);
      });
      load.appendChild(legend);
      load.appendChild(
        charts.lineChart(dates, series, { yMax: 100, unit: "%", label: "Raven CPU and memory in use by day" })
      );
      load.appendChild(historyNote(history));
    } else {
      load.appendChild(note("No history yet."));
    }

    // Winners
    var win = section(root, "Winners");
    win.appendChild(
      note(
        "The top 5 accounts by CPU when the snapshot was taken. CPU is summed over each account's processes, " +
          "so 100% is one full core and values above 100% mean several cores."
      )
    );
    if (stats && stats.winners && stats.winners.length) {
      win.appendChild(el("h3", null, "Latest"));
      win.appendChild(
        table(
          ["User", "CPU", "Memory"],
          stats.winners.map(function (w) {
            return [w.user + (isSystem(w.user) ? " (system)" : ""), w.cpu + "%", w.mem_percent + "%"];
          })
        )
      );
    }
    var grid = occurrenceGrid(history);
    if (grid) {
      win.appendChild(el("h3", null, "Appearances in the Winners list"));
      win.appendChild(grid);
      win.appendChild(
        note(
          "One square per daily snapshot; darker means more CPU that day. System accounts are listed last in gray. " +
            "Hover a square for the numbers."
        )
      );
    }

    // Memory by process
    if (stats && stats.top_memory && stats.top_memory.length) {
      var mem = section(root, "Top memory processes");
      mem.appendChild(
        table(
          ["User", "Command", "Memory"],
          stats.top_memory.map(function (p) {
            var cmd = el("td", "ss-mount", p.command);
            return [p.user, cmd, p.mem_percent + "%"];
          })
        )
      );
    }

    // Storage
    if (stats && stats.disks && stats.disks.length) {
      var st = section(root, "Storage");
      st.appendChild(
        table(
          ["Mount", "Size", "Used", "Available", "% Full"],
          stats.disks
            .slice()
            .sort(function (a, b) { return b.use_percent - a.use_percent; })
            .map(function (d) {
              return [el("td", "ss-mount", d.mount), d.size, d.used, d.available, barCell(d.use_percent)];
            })
        )
      );
    }
  }

  function render() {
    var root = document.querySelector("[data-raven-dashboard]");
    if (!root) return;
    var base = root.getAttribute("data-status-base");
    Promise.all(
      SOURCES.map(function (n) { return fetchJson(base, n); }).concat([fetchJson(base, "raven_history.json")])
    ).then(function (results) {
      var history = results.pop();
      paint(root, latestStats(results), Array.isArray(history) ? history : [], Date.now());
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(render);
  }
})();
