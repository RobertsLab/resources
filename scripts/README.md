# Server status lights

These scripts drive the status table at the top of
[Computing Hardware](../docs/Computing-Hardware.md).

## Why there are two probers

The three servers are not reachable from the same place:

| Host | Public DNS | How it is checked |
|---|---|---|
| `raven.fish.washington.edu` | no | TCP 8787 (RStudio Server), falling back to 22 — **UW network only** |
| `gannet.fish.washington.edu` | yes | HTTPS `GET /` |
| `klone.hyak.uw.edu` | yes | TCP 22 — there is no web port to probe |

Raven is not in public DNS, so nothing outside the UW network can see it. Klone
has no HTTP port at all, and browsers refuse to connect to port 22, so no
purely client-side check can work either.

So there are two probers writing to the same place:

- **`internal`** — cron on a machine inside the UW network. The only source
  that can see raven. This is the primary.
- **`external`** — the `server-status` GitHub Action. Sees gannet and klone
  from the public internet, so a dead internal prober does not take out all
  three lights at once.

Each writes `status/<profile>.json` to the orphan `server-status` branch. The
page fetches both from `raw.githubusercontent.com` (which sends
`access-control-allow-origin: *`, so there is no CORS problem) and takes the
most recent fresh reading per host.

The branch is rewritten as a single root commit on every run. At one check
every 10 minutes an append-only branch would add roughly 50,000 commits a year
to a repo that everyone clones.

## Files

- `check_servers.py` — runs the probes, prints or writes the JSON. Stdlib only.
- `publish_status.sh` — runs the checker and pushes the result to the
  `server-status` branch. Used by both the cron job and the Action.

Check without publishing anything:

```bash
./scripts/check_servers.py --profile internal
```

Off the UW network, raven will report `DNS lookup failed` — that is expected,
and is exactly why the internal prober has to run inside.

## Setting up the in-network cron

Run this on a machine inside the UW network that is up continuously. Gannet is
the natural choice.

**1. Give the machine push access.** Generate a deploy key on that host:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/robertslab_status -C "roberts-lab status bot" -N ""
```

Add the public key (`~/.ssh/robertslab_status.pub`) at
<https://github.com/RobertsLab/resources/settings/keys> as a deploy key **with
write access checked**. A deploy key is scoped to this one repo, so it cannot
be used to touch anything else in the org.

Then point git at it in `~/.ssh/config`:

```
Host github-robertslab
  HostName github.com
  User git
  IdentityFile ~/.ssh/robertslab_status
  IdentitiesOnly yes
```

**2. Clone the repo** somewhere on that host, e.g. `~/robertslab-resources`.

**3. Add the cron entry** with `crontab -e`:

```
*/10 * * * * ~/robertslab-resources/scripts/publish_status.sh --profile internal --repo github-robertslab:RobertsLab/resources.git >> ~/status-cron.log 2>&1
```

`publish_status.sh` keeps its own scratch clone under
`~/.cache/robertslab-server-status`, so it will not disturb the checkout it is
run from.

**4. Confirm** that `status/internal.json` appears on the
[`server-status` branch](https://github.com/RobertsLab/resources/tree/server-status/status)
and that the lights on the handbook page go green within a few minutes.

## Notes and limits

- A green light means the port answered. It says nothing about Slurm health,
  disk space, or whether jobs are running.
- `raw.githubusercontent.com` caches for about 5 minutes, so the page can lag
  the actual check by that much on top of the check interval.
- GitHub's scheduled workflows are best-effort: delayed under load, minimum
  5-minute interval, and disabled automatically after 60 days without repo
  activity. That is why the in-network cron is primary and the Action is only a
  backstop. Measured on this repo, the Action asks for `*/15` but lands every
  30-71 minutes (median 46). The 90-minute stale threshold in
  `docs/javascripts/server-status.js` is sized around that; if you tighten it,
  make sure the in-network cron is actually running first, or the lights will
  spend most of each cycle showing `unknown`.
- To add a host: add a probe in `check_servers.py` and a `<tr data-host="...">`
  row in `docs/Computing-Hardware.md`. The JavaScript matches the two by name
  and needs no change.
