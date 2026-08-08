#!/usr/bin/env bash
#
# Run the server checks and publish the result to the `server-status` branch.
# Used both by the cron job inside the UW network (--profile internal) and by
# the GitHub Action (--profile external). See scripts/README.md for setup.
#
# The status branch is kept separate from master on purpose: it updates every
# few minutes, and putting that in the docs history would spam the log and
# trigger a full site rebuild on every check.
#
# The branch is rewritten as a single root commit each time rather than
# accumulating history -- at one check every 10 minutes an append-only branch
# would add ~50k commits a year to a repo everyone clones.
#
# Usage: publish_status.sh --profile internal|external [--repo URL] [--workdir DIR]

set -euo pipefail

PROFILE="internal"
REPO="git@github.com:RobertsLab/resources.git"
WORKDIR="${HOME}/.cache/robertslab-server-status"
BRANCH="server-status"

while [ $# -gt 0 ]; do
  case "$1" in
    --profile) PROFILE="$2"; shift 2 ;;
    --repo)    REPO="$2"; shift 2 ;;
    --workdir) WORKDIR="$2"; shift 2 ;;
    -h|--help) sed -n '2,16p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

case "$PROFILE" in
  internal|external) ;;
  *) echo "usage: $0 --profile internal|external" >&2; exit 2 ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHECKER="${SCRIPT_DIR}/check_servers.py"

if [ ! -f "$CHECKER" ]; then
  echo "cannot find checker at ${CHECKER}" >&2
  exit 1
fi

if [ ! -d "${WORKDIR}/.git" ]; then
  mkdir -p "$WORKDIR"
  git init --quiet "$WORKDIR"
  git -C "$WORKDIR" remote add origin "$REPO"
fi

cd "$WORKDIR"

git config user.name "roberts-lab-status-bot"
git config user.email "roberts-lab-status-bot@users.noreply.github.com"
git remote set-url origin "$REPO"

# Every step is checked explicitly: `set -e` does not apply inside a function
# invoked as an `if` condition, so a bare command failing here would otherwise
# be silently skipped and the run would report success.
publish() {
  local old_sha=""

  # Get off `fresh` before deleting it, in case a previous run died mid-flight.
  git checkout --quiet -B staging >/dev/null 2>&1 || true
  git branch -D fresh >/dev/null 2>&1 || true

  # Start from whatever the remote currently has, so the other prober's file is
  # carried forward rather than clobbered.
  if git fetch --quiet --depth 1 origin "$BRANCH" 2>/dev/null; then
    old_sha="$(git rev-parse FETCH_HEAD)" || return 1
    git checkout --quiet -B staging "$old_sha" || return 1
    git reset --quiet --hard "$old_sha" || return 1
    git clean --quiet -fd || return 1
  else
    find . -mindepth 1 -maxdepth 1 -not -name .git -exec rm -rf {} + || return 1
  fi

  mkdir -p status || return 1
  python3 "$CHECKER" --profile "$PROFILE" --out "status/${PROFILE}.json" || return 1

  # Re-orphan so the branch stays at exactly one commit. --orphan keeps the
  # working tree and index, so `git add -A` below stages the full contents.
  git checkout --quiet --orphan fresh || return 1
  git add -A || return 1
  git commit --quiet -m "status(${PROFILE}): $(date -u +%Y-%m-%dT%H:%M:%SZ)" || return 1

  if [ -n "$old_sha" ]; then
    # A concurrent push from the other prober invalidates the lease, which
    # rejects our push instead of silently dropping their update.
    git push --quiet \
      --force-with-lease="refs/heads/${BRANCH}:${old_sha}" \
      origin "fresh:refs/heads/${BRANCH}" || return 1
  else
    git push --quiet origin "fresh:refs/heads/${BRANCH}" || return 1
  fi

  echo "published status/${PROFILE}.json" >&2
}

for attempt in 1 2 3; do
  if publish; then
    exit 0
  fi
  echo "publish attempt ${attempt} failed; retrying" >&2
  sleep 5
done

echo "failed to publish status after 3 attempts" >&2
exit 1
