## Quick Start Guide

Example SLURM Script to launch RStudio Server.

The example will use the `srlab-bioinformatics-container-2bd5d44.sif` container in the SLURM script called `rstudio-server.job`.

- User needs to set/change the following in the SLURM script before starting script:

    - `#SBATCH --time=02:00:00`
    - `#SBATCH --mem=20G`
    - `--chdir=/gscratch/scrubbed/${USER}/<add_rest_of_path>`
    - `RSTUDIO_SIF="srlab-bioinformatics-container-2bd5d44.sif" # UPDATE THIS LINE`

- Users should add the following line in `~/.Renviron`. If you don't have a `~/.Renviron`, you can create it like this: `touch ~/.Renviron`
    
    - `R_LIBS_USER` in `~/.Renviron`. Example:

        ```shell
        cat ~/.Renviron 
        # Set local library installation path
        R_LIBS_USER=/gscratch/srlab/${USER}/R_libs_apptainer
        ```

- After submitting script (`sbatch rstudio-server.job`), view the SLURM output file located in `--chdir=/gscratch/scrubbed/${USER}/<add_rest_of_path>` for information on:

    1. How to create tunnel to Mox node.

      - NOTE: When logging into the tunnel, the terminal will _not_ acknowledge when you've logged in. You need to leave this Terminal window open.

    2. What address to direct your web browser to (`localhost:8787`).

    3. Username/password to enter into RStudio Server interface.

    4. How to terminate RStudio Server and the SLURM job.

- Example script uses the following Apptainer container image: `srlab-bioinformatics-container-2bd5d44.sif`.

```shell
$ cat rstudio-server.job 


#!/bin/sh

#SBATCH --job-name=rstudio-server
#SBATCH --account=srlab
#SBATCH --partition=cpu-g2-mem2x #update this line - use hyakalloc to find partitions you can use
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --mem=20G
#SBATCH --signal=USR2
#SBATCH --output=%x_%j.out
## Specify the working directory for this job
#SBATCH --chdir=/gscratch/scrubbed/${USER}

# This script will request a single CPU with four threads with 20GB of RAM for 2 hours. 
# You can adjust --time, --nodes, --ntasks, and --mem above to adjust these settings for your session.

# --output=%x_%j.out creates a output file called rstudio-server_NNNNNNNN.out 
# where the %x is short hand for --job-name above and the N's are an 8-digit 
# jobID assigned by SLURM when our job is submitted.

RSTUDIO_CWD="/gscratch/srlab/containers" # UPDATE THIS LINE
RSTUDIO_SIF="srlab-bioinformatics-container-2bd5d44.sif" # UPDATE THIS LINE

# Create temp directory for ephemeral content to bind-mount in the container
RSTUDIO_TMP=$(/usr/bin/python3 -c 'import tempfile; print(tempfile.mkdtemp())')

mkdir -p -m 700 \
        ${RSTUDIO_TMP}/run \
        ${RSTUDIO_TMP}/tmp \
        ${RSTUDIO_TMP}/var/lib/rstudio-server

cat > ${RSTUDIO_TMP}/database.conf <<END
provider=sqlite
directory=/var/lib/rstudio-server
END

# Set OMP_NUM_THREADS to prevent OpenBLAS (and any other OpenMP-enhanced
# libraries used by R) from spawning more threads than the number of processors
# allocated to the job.
#
# Set R_LIBS_USER to a path specific to rocker/rstudio to avoid conflicts with
# personal libraries from any R installation in the host environment

cat > ${RSTUDIO_TMP}/rsession.sh <<END
#!/bin/sh

export OMP_NUM_THREADS=${SLURM_JOB_CPUS_PER_NODE}
export R_LIBS_USER=${RSTUDIO_CWD}/R
exec /usr/lib/rstudio-server/bin/rsession "\${@}"
END

chmod +x ${RSTUDIO_TMP}/rsession.sh

export APPTAINER_BIND="${RSTUDIO_CWD}:${RSTUDIO_CWD},/gscratch:/gscratch,${RSTUDIO_TMP}/run:/run,${RSTUDIO_TMP}/tmp:/tmp,${RSTUDIO_TMP}/database.conf:/etc/rstudio/database.conf,${RSTUDIO_TMP}/rsession.sh:/etc/rstudio/rsession.sh,${RSTUDIO_TMP}/var/lib/rstudio-server:/var/lib/rstudio-server"

# Do not suspend idle sessions.
# Alternative to setting session-timeout-minutes=0 in /etc/rstudio/rsession.conf
export APPTAINERENV_RSTUDIO_SESSION_TIMEOUT=0

export APPTAINERENV_USER=$(id -un)
export APPTAINERENV_PASSWORD=$(openssl rand -base64 15)

# get unused socket per https://unix.stackexchange.com/a/132524
# tiny race condition between the python & apptainer commands
readonly PORT=$(/mmfs1/sw/pyenv/versions/3.9.5/bin/python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
cat 1>&2 <<END
1. SSH tunnel from your workstation using the following command:

   ssh -N -L 8787:${HOSTNAME}:${PORT} ${APPTAINERENV_USER}@klone.hyak.uw.edu

   and point your web browser to http://localhost:8787

2. log in to RStudio Server using the following credentials:

   user: ${APPTAINERENV_USER}
   password: ${APPTAINERENV_PASSWORD}

When done using RStudio Server, terminate the job by:

1. Exit the RStudio Session ("power" button in the top right corner of the RStudio window)
2. Issue the following command on the login node:

      scancel -f ${SLURM_JOB_ID}
END

source /etc/bashrc
module load apptainer

apptainer exec --cleanenv --home ${RSTUDIO_CWD} ${RSTUDIO_CWD}/${RSTUDIO_SIF} \
    rserver --www-port ${PORT} \
            --auth-none=0 \
            --auth-pam-helper-path=pam-helper \
            --auth-stay-signed-in-days=30 \
            --auth-timeout-minutes=0 \
            --rsession-path=/etc/rstudio/rsession.sh \
            --server-user=${APPTAINERENV_USER}

APPTAINER_EXIT_CODE=$?
echo "rserver exited $APPTAINER_EXIT_CODE" 1>&2
exit $APPTAINER_EXIT_CODE
```

---

## Create/customize your own Apptainer Rstudio Server container

NOTE: These instructions are written to be performed on Klone (Hyak).

1. Create an [Apptainer definition file](https://apptainer.org/docs/user/main/definition_files.html):

    - Example filename: `rstudio-4.4.1.def`

    - Here's an example with a good set of basic installations for R 4.4.1:

    ```
    Bootstrap: docker
    From: rocker/rstudio:4.4.1
    %files
        # Load file with R package installation commands in to container at /tmp
        # Expects file called "r_packages_installs.R" to be in current directory.
        r_packages_installs.R /tmp/

    %post
        # Install additional system packages in container
        # Most are needed for R/RStudio dependencies
        apt -y update
        apt -y install libxml2 libz-dev libbz2-dev liblzma-dev libxtst6 libxt6
        
        # Run R package installation script file
        Rscript /tmp/r_packages_installs.R
    ```

2. Create file `r_packages_installs.R` containing R package installation instructions.

    - NOTE: The container already has a base set of R packages (e.g. `ggplot2` installed).

    - Here's an example with a set of commonly used packages:

    ```R
    # Update base packages
    update.packages(ask = FALSE)

    # Install BioConductor package manager
    if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
    BiocManager::install(version = "3.19")

    # Install tidyverse
    install.packages("tidyverse")

    # Install matrixStats 0.61.0 (needed for DESeq2)
    install.packages("https://cran.rstudio.com/src/contrib/matrixStats_0.61.0.tar.gz", repos=NULL, type="source")

    # Install remotes package (allows for package installs from GitHub)
    BiocManager::install("remotes")

    # Install GSEABase (a dependency for numerous gene ontology/enrichment analysis)
    BiocManager::install("Bioconductor/GSEABase")

    # Install qvalue package
    BiocManager::install("qvalue")

    # Install GO.db (annotation maps for Gene Ontology data)
    BiocManager::install("GO.db")

    # Install MatrixGenerics (needed for DESeq2)
    BiocManager::install("MatrixGenerics")

    # Install Methylkit
    BiocManager::install("methylKit")

    # Install GOseq
    BiocManager::install("goseq")

    # Install WGCNA
    BiocManager::install("WGCNA")

    # Install DESeq2
    BiocManager::install("DESeq2")


    ```


3. Initiate an [interactive node](./klone_Node-Types.md).

4. Build the container from the definition file:
    
    - NOTE: Resulting container name will be `rstudio-4.4.1.sjw-v1.0.sif`

    `apptainer build --fakeroot rstudio-4.4.1.sjw-v1.0.sif rstudio-4.4.1.sjw-v1.0.def`

5. Exit the interactive node.

6. Use the SLURM script above to start the container.

    - NOTE: Be sure to update the script line to reflect your container name:
    
    ```
    # Set container name
    container="rstudio-4.4.1.sif"
    ```
