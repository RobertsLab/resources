# Gannet Dashboard

Health of `gannet.fish.washington.edu`, the lab's Synology NAS, from the [daily health report](https://gannet.fish.washington.edu/v1_web/owlshell/latest.txt) it writes each morning. The server status probers pick up each new report within about an hour of it being written, so this page is at most a day old. It is flagged if the report goes stale. For whether gannet is answering right now, see [Server Status](Computing-Hardware.md#server-status).

<div data-gannet-dashboard data-status-base="https://raw.githubusercontent.com/RobertsLab/resources/server-status/status">
  <p>Loading gannet's latest health report…</p>
</div>

!!! note
    Volumes at 90% or more are marked critical and 75% or more are marked as warnings. The history charts are built from the dated `gannet_health_YYYY-MM-DD.txt` copies of the report (the last 30 days).
