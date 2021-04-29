## Quick Start Guide

Example SLURM Script to launch RStudio Server:

- User needs to set the following before starting script:

    - `--mail-user=`
    - `--chdir=`
    - `R_LIBS_USER` in `~/.Renviron`. Example:

        ```shell
        cat ~/.Renviron 
        # Set local library installation path
        R_LIBS_USER=/gscratch/srlab/${USER}/R_libs_singularity
        ```

- After submitting script, view the SLURM output file located in `--chdir=` for information on:

    1. How to create tunnel to Mox node.

    2. What address to direct your web browser to.

    3. Username/password to enter into RStudio Server interface.

    4. How to terminate RStudio Server and the SLURM job.

- Example script uses the following Singularity container image: `rstudio-4.0.2.sjw-v1.0`.

```shell
#!/bin/bash
## Job Name
#SBATCH --job-name=rstudio_server_test
## Allocation Definition
#SBATCH --account=srlab
#SBATCH --partition=srlab
## Resources
## Nodes
#SBATCH --nodes=1
## Walltime (days-hours:minutes:seconds format)
#SBATCH --time=0-08:00:00
## Memory per node
#SBATCH --mem=100G
#SBATCH --signal=USR2
##turn on e-mail notification
#SBATCH --mail-type=ALL
#SBATCH --mail-user=
## Specify the working directory for this job
#SBATCH --chdir=


################################################################
# Set user-defined variables inside this box.

# Set container path
container_path="/gscratch/srlab/programs/singularity_containers"

# Set container name
container="rstudio-4.0.2.sjw-v1.0"
################################################################

## MAKE NO CHANGES BELOW THIS LINE

module load singularity



export PASSWORD=$(openssl rand -base64 15)
# get unused socket per https://unix.stackexchange.com/a/132524
# tiny race condition between the python & singularity commands
readonly PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
cat 1>&2 <<END
1. SSH tunnel from your workstation using the following command:

   ssh -N -L 8787:${HOSTNAME}:${PORT} ${USER}@mox.hyak.uw.edu

   and point your web browser to http://localhost:8787

2. log in to RStudio Server using the following credentials:

   user: ${USER}
   password: ${PASSWORD}

When done using RStudio Server, terminate the job by:

1. Exit the RStudio Session ("power" button in the top right corner of the RStudio window)
2. Issue the following command on the login node:

      scancel -f ${SLURM_JOB_ID}
END


##NOTE##
# This is a local drive location I can write, you should be able
# to just set to a subfolder of your HPC home/scratch directory
export TMPDIR="/gscratch/scrubbed/${USER}/rstudio-tmp"

mkdir -p "$TMPDIR/tmp/rstudio-server"
uuidgen > "$TMPDIR/tmp/rstudio-server/secure-cookie-key"
chmod 0600 "$TMPDIR/tmp/rstudio-server/secure-cookie-key"

mkdir -p "$TMPDIR/var/lib"
mkdir -p "$TMPDIR/var/run"

# User-installed R packages go into their home directory
if [ ! -e ${HOME}/.Renviron ]
then
  printf '\nNOTE: creating ~/.Renviron file\n\n'
  echo 'R_LIBS_USER=~/R/%p-library/%v' >> ${HOME}/.Renviron
fi

# This example bind mounts the /gscratch/scrubbed/${USER} directory on the host into the Singularity container.
# By default the only host file systems mounted within the container are $HOME, /tmp, /proc, /sys, and /dev.
singularity exec \
--bind="$TMPDIR/var/lib:/var/lib/rstudio-server" \
--bind="$TMPDIR/var/run:/var/run/rstudio-server" \
--bind="$TMPDIR/tmp:/tmp" \
--bind=/gscratch/scrubbed/${USER} \
${container_path}/${container} \
rserver --www-port ${PORT} --auth-none=0 --auth-pam-helper-path=pam-helper
```

---

## Create/customize your own Singularity Rstudio Server container

NOTE: These instructions require an existing installation of [Singularity](https://sylabs.io/guides/3.0/user-guide/index.html) - which is only avaible for Linux.

NOTE: Instructions incomplete as of this commit! Updates coming soon.

1. Download/install/create a new container (if needed/desired):

    `singularity build --sandbox rstudio-4.0.2.sandbox.simg docker://rocker/rstudio:4.0.2`

2. Enter the container at the command line as root user:

    `sudo singularity shell --writable rstudio-4.0.2.sandbox.simg/`

3. Update/install system packages:

    ```shell
    apt -y update && apt -y install \
    libbz2-dev \
    liblzma-dev \
    libxml2 \
    libz-dev \
    libxtst6
    ```

4. Run `R`:

    - `R`

    ![screenshot of starting R in Singularity container]()

5. Install BioConductor (required for many commonly used programs):

    ```R
    if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
    BiocManager::install(version = "3.12")
    ```


6. Install package(s) of your choosing using standard `install.packages()` function in `R`.

    - For example, `tidyverse` is not installed by default. To install:

      ```R
      install.packages("tidyverse")
      ```

    - If installing [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html), you'll encounter some errors. You'll need to install the following:

        - matrixStats:

            ```R
            install.packages("https://cran.rstudio.com/src/contrib/matrixStats_0.58.0.tar.gz", repos=NULL, type="source")
            ```

        - MatrixGenerics:

            ```R
            BiocManager::install("MatrixGenerics")
            ```


8. Quit `R`:

    - `quit()`

9. Exit the container:

    - `exit`

10. Convert sandboxed container to image (needed for transfer to Mox):

    `sudo singularity build rstudio-4.0.2.sjw-v1.0.simg rstudio-4.0.2.sandbox.simg/`

    - This will create a file called `rstudio-4.0.2.sjw-v1.0.simg` which can be rsync'd to your desired Mox folder.