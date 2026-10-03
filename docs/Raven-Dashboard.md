# Raven Dashboard

Activity on `raven.fish.washington.edu` from the [daily snapshot](https://gannet.fish.washington.edu/v1_web/owlshell/bu-github/ghr.log) a cron on raven writes to gannet each morning around 7am: CPU and memory in use, the top accounts by CPU (the **Winners** list), the processes using the most memory, and drive space. For whether raven is answering right now, see [Server Status](Computing-Hardware.md#server-status).

<div data-raven-dashboard data-status-base="https://raw.githubusercontent.com/RobertsLab/resources/server-status/status">
  <p>Loading raven's latest snapshot…</p>
</div>

!!! note
    Every value is a single reading taken when the snapshot runs, not a daily average. A job that runs overnight and finishes by 7am will not appear. Raven only keeps the latest snapshot, so the history here is collected by the server status probers one day at a time and starts on the day this page went live.
