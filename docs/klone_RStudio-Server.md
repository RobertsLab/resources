## RStudio Server on Klone: Two Approaches

There are two primary ways to run RStudio Server on Klone:

1. **On-Demand Interactive Sessions** (Recommended for immediate use)
2. **SLURM Batch Jobs** (For scheduled or longer-running sessions)

---

## Method 1: On-Demand Interactive RStudio Sessions

This method allows you to start RStudio Server immediately in an interactive session, perfect for exploratory data analysis and immediate work.

### Prerequisites

- Ensure you have the RStudio container available in your directory
- Set up your `~/.Renviron` file (see setup instructions below)

### Quick Start with Interactive Session

1. **Start an interactive session** on a compute node:

   ```bash
   srun -p cpu-g2-mem2x -A srlab --time=04:00:00 --mem=32G --cpus-per-task=4 --pty /bin/bash
   ```
   
   - Adjust `--time`, `--mem`, and `--cpus-per-task` based on your needs
   - Use `hyakalloc` to find available partitions for your account

2. **Launch RStudio Server** once in the interactive session:

   ```bash
   # Set your working directory and container path
   export RSTUDIO_CWD="/gscratch/srlab/${USER}"
   export RSTUDIO_SIF="srlab-bioinformatics-container-2bd5d44.sif"
   
   # Create temporary directories
   export RSTUDIO_TMP=$(mktemp -d)
   mkdir -p -m 700 ${RSTUDIO_TMP}/{run,tmp,var/lib/rstudio-server}
   
   # Create database config
   cat > ${RSTUDIO_TMP}/database.conf <<END
   provider=sqlite
   directory=/var/lib/rstudio-server
   END
   
   # Create rsession script
   cat > ${RSTUDIO_TMP}/rsession.sh <<END
   #!/bin/sh
   export OMP_NUM_THREADS=${SLURM_JOB_CPUS_PER_NODE:-4}
   export R_LIBS_USER=${RSTUDIO_CWD}/R
   exec /usr/lib/rstudio-server/bin/rsession "\${@}"
   END
   chmod +x ${RSTUDIO_TMP}/rsession.sh
   
   # Set up Apptainer bindings
   export APPTAINER_BIND="${RSTUDIO_CWD}:${RSTUDIO_CWD},/gscratch:/gscratch,${RSTUDIO_TMP}/run:/run,${RSTUDIO_TMP}/tmp:/tmp,${RSTUDIO_TMP}/database.conf:/etc/rstudio/database.conf,${RSTUDIO_TMP}/rsession.sh:/etc/rstudio/rsession.sh,${RSTUDIO_TMP}/var/lib/rstudio-server:/var/lib/rstudio-server"
   
   # Generate credentials
   export APPTAINERENV_USER=$(id -un)
   export APPTAINERENV_PASSWORD=$(openssl rand -base64 15)
   export APPTAINERENV_RSTUDIO_SESSION_TIMEOUT=0
   
   # Get available port
   PORT=$(python3 -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
   
   echo "=== RStudio Server Connection Info ==="
   echo "1. In a NEW terminal on your local machine, run:"
   echo "   ssh -N -L 8787:${HOSTNAME}:${PORT} ${APPTAINERENV_USER}@klone.hyak.uw.edu"
   echo ""
   echo "2. Open your web browser to: http://localhost:8787"
   echo ""
   echo "3. Login with:"
   echo "   Username: ${APPTAINERENV_USER}"
   echo "   Password: ${APPTAINERENV_PASSWORD}"
   echo ""
   echo "4. When finished, press Ctrl+C here and type 'exit' to end the session"
   echo "====================================="
   
   # Load Apptainer and start RStudio Server
   module load apptainer
   apptainer exec --cleanenv --home ${RSTUDIO_CWD} ${RSTUDIO_CWD}/${RSTUDIO_SIF} \
       rserver --www-port ${PORT} \
               --auth-none=0 \
               --auth-pam-helper-path=pam-helper \
               --auth-stay-signed-in-days=30 \
               --auth-timeout-minutes=0 \
               --rsession-path=/etc/rstudio/rsession.sh \
               --server-user=${APPTAINERENV_USER}
   ```

3. **Connect from your local machine**: 

   - Open a new terminal on your local computer
   - Run the SSH tunnel command shown in the output
   - Open your browser to `http://localhost:8787`
   - Login with the provided credentials

4. **Clean up when done**:
   - Close RStudio in your browser
   - Press `Ctrl+C` in the terminal running RStudio Server
   - Type `exit` to end the interactive session

### Advantages of Interactive Sessions

- **Immediate access**: No waiting in queue for batch job scheduling
- **Real-time interaction**: Direct terminal access for debugging
- **Flexible duration**: Easy to extend or terminate as needed
- **Simpler setup**: Fewer files to manage compared to batch jobs

---

## Method 2: SLURM Batch Jobs

[**Screen Recording How-to**](https://washington.zoom.us/rec/share/tM_4zmytAnDQrPoIxqDH0Q7RpaZviXcs9ih7ypUPSJCbaQc0Kwa6NnsqdeMvkvdF.P4qX95_arDgBeGMF) (UW sign-in required)

This method uses a SLURM script to launch RStudio Server as a batch job, suitable for longer-running sessions or when you want to queue the job for later execution.

### SLURM Script Example

### Setup Requirements (For Both Methods)

Before using either method, you need to set up your environment:

#### 1. Container Setup
- Copy the RStudio container to your directory: `srlab-bioinformatics-container-2bd5d44.sif`
- Ensure `RSTUDIO_CWD` points to where your container is located
- The example uses the container located in `/gscratch/srlab/containers/`

#### 2. R Library Configuration
Create or update your `~/.Renviron` file to specify where R packages should be installed:

```bash
# Create the file if it doesn't exist
touch ~/.Renviron

# Add library path (adjust the path as needed)
echo "R_LIBS_USER=/gscratch/srlab/${USER}/R_libs_apptainer" >> ~/.Renviron
```

You can verify your setup:
```shell
cat ~/.Renviron 
# Should show:
# R_LIBS_USER=/gscratch/srlab/${USER}/R_libs_apptainer
```

#### 3. Partition Access
- Use `hyakalloc` to find available partitions for your account
- Update partition names in commands/scripts accordingly

### SLURM Script Configuration

For the batch job method, you need to customize the following in your SLURM script:

- `#SBATCH --time=02:00:00` (adjust time as needed)
- `#SBATCH --mem=20G` (adjust memory as needed)  
- `--chdir=/gscratch/scrubbed/${USER}/<add_rest_of_path>` (set your working directory)
- `RSTUDIO_SIF="srlab-bioinformatics-container-2bd5d44.sif"` (update container name/path)

### Running the SLURM Batch Job

After customizing your `rstudio-server.job` script:

1. **Submit the job**: `sbatch rstudio-server.job`

2. **Monitor job status**: `squeue -u $USER`

3. **Check the output file**: Look in your specified `--chdir` directory for `rstudio-server_JOBID.out`

4. **Follow connection instructions** from the output file for:
   - SSH tunnel command to the compute node
   - Browser URL (`localhost:8787`)
   - Username/password for RStudio Server
   - How to terminate the session

5. **Important notes**:
   - When creating the SSH tunnel, the terminal will not show a confirmation message
   - Keep the tunnel terminal window open during your RStudio session
   - To terminate: Exit RStudio, then run `scancel -f JOBID`

### Example SLURM Script

The following script uses the `srlab-bioinformatics-container-2bd5d44.sif` container:

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

## List of Roberts Lab Apptainers


- `/gscratch/srlab/containers/srlab-R4.4-bioinformatics-container-f050784.sif`



<https://github.com/RobertsLab/code/tree/master/apptainer_definition_files> 

`code/apptainer_definition_files`

### Apptainer (Singularity) Definition Files

This is a repository for all of [the Roberts Lab](https://robertslab.github.io/resources/) definition files used for creating [Apptainer](https://apptainer.org/) images.

---

- [`r_packages_installs.R`](./r_packages_installs.R): R package installation instructions required for building the Roberts Lab bioinformatics container with [`srlab-bioinformatics-container.def`](./srlab-bioinformatics-container.def).

- [`srlab-bioinformatics-build.sh`](./srlab-bioinformatics-container.def): A Bash script used to build the Apptainer container generated by [`srlab-bioinformatics-container.def`](./srlab-bioinformatics-container.def). The script is specifically designed to be executed on the UW Hyak HPC, Klone. It will:

  1. Execute the most recent commit of [`srlab-bioinformatics-container.def`](./srlab-bioinformatics-container.def).

  2. Copy [`r_packages_installs.R`](./r_packages_installs.R) to `/tmp/` (needed for build process).

  3. Move completed Apptainer container to `/gscratch/srlab/containers/srlab-bioinformatics-container-<commit>.sif`.

- [`srlab-bioinformatics-container.def`](./srlab-bioinformatics-container.def): Apptainer definition file for the Roberts Lab bioinformatics container. Built on the `rocker/rstudio:4.4.1` image to allow usage of RStudio.

---

## Method Comparison and Best Practices

### When to Use Interactive Sessions (On-Demand)
- **Exploratory data analysis**: Quick data examination and visualization
- **Short-term work**: Sessions lasting 1-4 hours
- **Learning and testing**: Trying new packages or testing code 
- **Immediate access needed**: Don't want to wait in queue
- **Debugging**: Need direct terminal access to troubleshoot

### When to Use SLURM Batch Jobs
- **Long-running analyses**: Sessions longer than 4-6 hours
- **Scheduled work**: Want to queue job for later execution
- **Resource-intensive tasks**: Need guaranteed resource allocation
- **Reproducible workflows**: Need to document exact resource requirements
- **Unattended execution**: Can run without constant monitoring

### General Tips
- **Resource management**: Always specify appropriate time, memory, and CPU requirements
- **Clean up**: Always exit sessions properly to free resources for other users
- **Container location**: Keep containers in shared locations when possible to save space
- **R packages**: Install packages to your personal library path as configured in `~/.Renviron`
- **Data storage**: Keep large datasets in `/gscratch` rather than home directories
- **Network usage**: Minimize internet downloads during sessions - prepare data beforehand

### Troubleshooting
- **Port conflicts**: If port 8787 is busy, the scripts will automatically find an available port
- **Container not found**: Verify the container path and filename in your settings
- **R package issues**: Check that `R_LIBS_USER` is properly set in `~/.Renviron`
- **SSH tunnel problems**: Ensure you're using the correct hostname and port from the output
- **Session timeouts**: Interactive sessions end at their time limit - plan accordingly
