#!/bin/bash
# Launch RStudio Server from an Apptainer/Singularity container on Raven.
#
# Usage:
#   bash raven-rstudio.sh                        # newest .sif in /home/shared/containers
#   bash raven-rstudio.sh /path/to/container.sif # a specific container
#
# Prints the URL, username, and a one-time password to log in with.
# Press Ctrl-C (or close the screen session) to stop RStudio Server.
#
# Docs: https://robertslab.github.io/resources/raven_RStudio-Server/

set -euo pipefail

SHARED_CONTAINERS=/home/shared/containers

SIF="${1:-${RSTUDIO_SIF:-}}"
if [[ -z "${SIF}" ]]; then
  # Default to the most recently modified container in the shared directory
  SIF=$(ls -t "${SHARED_CONTAINERS}"/*.sif 2>/dev/null | head -n 1 || true)
fi
if [[ -z "${SIF}" || ! -f "${SIF}" ]]; then
  echo "Usage: bash $0 [/path/to/container.sif]" 1>&2
  echo "Container not found: '${SIF}'" 1>&2
  exit 1
fi

# Prefer singularity: on Raven (Ubuntu 24.04) unprivileged apptainer fails
# because AppArmor restricts user namespaces, while singularity works.
if command -v singularity >/dev/null 2>&1; then
  RUNTIME=singularity
elif command -v apptainer >/dev/null 2>&1; then
  RUNTIME=apptainer
else
  echo "Neither apptainer nor singularity found on PATH." 1>&2
  exit 1
fi

# Private, per-session directories so users don't collide in /tmp
RSTUDIO_TMP=$(mktemp -d -t rstudio-${USER}-XXXXXX)
trap 'rm -rf "${RSTUDIO_TMP}"' EXIT
mkdir -p -m 700 \
  "${RSTUDIO_TMP}/run" \
  "${RSTUDIO_TMP}/tmp" \
  "${RSTUDIO_TMP}/var/lib/rstudio-server"

cat > "${RSTUDIO_TMP}/database.conf" <<END
provider=sqlite
directory=/var/lib/rstudio-server
END

# Wrapper so the R session runs with the host user's name and home directory
# (otherwise it can default to the container's "rstudio" user and /home/rstudio)
cat > "${RSTUDIO_TMP}/rsession.sh" <<END
#!/bin/sh
export USER=${USER}
export LOGNAME=${USER}
export HOME=${HOME}
exec /usr/lib/rstudio-server/bin/rsession "\${@}"
END
chmod +x "${RSTUDIO_TMP}/rsession.sh"

# Pick an unused port so multiple users can run at once
PORT=$(python3 -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')

PASSWORD=$(openssl rand -base64 15)
# Set both prefixes so this works whether singularity is SingularityCE or apptainer
for ENV_PREFIX in SINGULARITYENV_ APPTAINERENV_; do
  export "${ENV_PREFIX}USER=${USER}"
  export "${ENV_PREFIX}PASSWORD=${PASSWORD}"
  # Do not suspend idle sessions
  export "${ENV_PREFIX}RSTUDIO_SESSION_TIMEOUT=0"
done

cat 1>&2 <<END

RStudio Server is starting (${RUNTIME}, container: $(basename "${SIF}")).

  1. Open:      http://raven.fish.washington.edu:${PORT}
  2. Username:  ${USER}
     Password:  ${PASSWORD}

To stop: press Ctrl-C here (or quit RStudio's session first, then Ctrl-C).

END

"${RUNTIME}" exec --cleanenv --home "${HOME}" \
  --bind "${RSTUDIO_TMP}/run:/run" \
  --bind "${RSTUDIO_TMP}/tmp:/tmp" \
  --bind "${RSTUDIO_TMP}/database.conf:/etc/rstudio/database.conf" \
  --bind "${RSTUDIO_TMP}/rsession.sh:/etc/rstudio/rsession.sh" \
  --bind "${RSTUDIO_TMP}/var/lib/rstudio-server:/var/lib/rstudio-server" \
  "${SIF}" \
  rserver --www-port "${PORT}" \
          --www-address 0.0.0.0 \
          --auth-none=0 \
          --auth-pam-helper-path=pam-helper \
          --auth-timeout-minutes=0 \
          --auth-stay-signed-in-days=30 \
          --rsession-path=/etc/rstudio/rsession.sh \
          --server-user="${USER}"
