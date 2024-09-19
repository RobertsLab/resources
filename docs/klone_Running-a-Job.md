
**NOTE** - Use [`/gscratch/scrubbed/<UW_NetID>`](https://robertslab.github.io/resources/klone_Data-Storage-and-System-Organization/#3-temporary-storage) for running jobs (i.e. writing output files to). As the name suggests, you will need to move files to a "bird" for archival storage. If you are needing a set of large raw files for analysis - also place these in the `/gscratch/scrubbed/<UW_NetID>` directory.

---

`sbatch` is the main execution command for the job scheduler ([SLURM](https://slurm.schedmd.com/overview.html)). It spools up a compute node for long-term or compute-intensive tasks such as assemblies, blasts, alignments, etc.

`sbatch` can be run from a login node with the command:

```bash
sbatch <slurm_script_name.sh>
```

`sbatch` requires a shell script to function, with two main parts: the header and the execute portion.

## The Header

<pre>
<code>
#!/bin/bash
## Job Name
#SBATCH --job-name=<b>myjob</b>
## Allocation Definition
#SBATCH --account=srlab
#SBATCH --partition=cpu-g2-mem2x
## Nodes
#SBATCH --nodes=1
## Walltime (days-hours:minutes:seconds format)
#SBATCH --time=<b>dd-hh:mm:ss</b>
## Memory per node
#SBATCH --mem=<b>450G</b>
##turn on e-mail notification
#SBATCH --mail-type=ALL
#SBATCH --mail-user=$USER
## Specify the working directory for this job
#SBATCH --chdir=<b>/gscratch/srubbed/<UW_NetID>/to/your/desired/directory</b>
</code>
</pre>


<b>Bolded sections above must be changed prior to execution.</b> Those specific sections are described in more detail.

- `--job-name=`**`myjob`** is an identifier for your current job. It's what shows up in `scontrol` and `squeue` calls. Providing a unique-to-you job name may be helpful for distinguishing between different runs, by is not necessary.

- `--time=`**`dd-hh:mm:ss`** is the "wall" time, or how long we are reserving the node for our use. This argument requires some consideration and knowledge about the program you're running prior to execution. Selecting too little wall time will cause the scheduler to kill your process mid-run when time runs out. Selecting too much time limits other's ability to use Hyak functions, but the scheduler releases a node upon program completion usually, so this is a secondary consideration.

- `--mem=`**`450G`** specifies how much memory (RAM) to allocate to the process. We have a single slice with a maximum of 490GB of RAM. Specifying a value below the maximum allows for some additional processing overhead. Usually, setting this to the maximum is fine, but reserving only what you might need can allow for multiple users to use the slice at the same time.

- `--chdir=`**`/gscratch/srubbed/<UW_NetID>/to/your/desired/directory`** indicates the working directory where output will be written. All jobs should be executed in your `/gscratch/srubbed/<UW_NetID>` directory. See the [Data Storage & System Organization section of the wiki](https://github.com/RobertsLab/hyak_mox/wiki/Data-Storage-&-System-Organization) for more info.

## The Execute portion

This section contains the commands/programs you want executed. You can treat it like the command line, in that it executes commands sequentially as input. These can include program calls, module loading, making directories, etc. However, since Klone relies on the use of [containers](./klone_containers.md) to run, your SLURM script will _require_ the following:

    ```bash
    # Load modules
    module load apptainer

    # Execute Roberts Lab bionformatics container
    # Binds home directory
    # Binds /gscratch directory
    # Directory bindings allow outputs to be written to the hard drive.
    apptainer exec \
    --home $PWD \
    --bind /mmfs1/home/ \
    --bind /mmfs1/gscratch/ \
    /gscratch/srlab/containers/srlab-bioinformatics-container-<git_commit_hash>.sif \
    <commands_script.sh>
    ```

## SLURM Script Template/Example - Multiple Commands

If you need to execute multiple commands using a container, which will usually be the case and is shown in the example directly above this, you'll need to place those commands in a separate script.

### Command script example

Here's an example script, called `commands.sh`. This is where we'll set all of our variables and execute various commands/programs we'd like for our analysis:

    ```bash
    #!/bin/bash

    # Requires Bash >=4.0, as script uses associative arrays.

    ###################################################################################
    # These variables need to be set by user

    ## Number of CPU threads to use for programs (if applicable)
    threads=28

    ## Programs associative array
    ## Using array is useful for logging program options (see end of script)
    declare -A programs_array

    programs_array=(
    [bowtie2]="bowtie2" \
    [bowtie2_build]="bowtie2-build" \
    [samtools_index]="samtools index" \
    [samtools_sort]="samtools sort" \
    [samtools_view]="samtools view"
    )


    ## INPUT FILES ##
    genome_fasta="./data/C_gigas/genomes/cgig-NCBI-genome.fasta"
    genome_name="cgig-NCBI-genome"

    ###################################################################################

    # Capture program options
    if [[ "${#programs_array[@]}" -gt 0 ]]; then
      echo "Logging program options..."
      for program in "${!programs_array[@]}"
      do
        {
        echo "Program options for ${program}: "
        echo ""
        # Handle samtools help menus
        if [[ "${program}" == "samtools_index" ]] \
        || [[ "${program}" == "samtools_sort" ]] \
        || [[ "${program}" == "samtools_view" ]]
        then
          ${programs_array[$program]}

        # Handle DIAMOND BLAST menu
        elif [[ "${program}" == "diamond" ]]; then
          ${programs_array[$program]} help

        # Handle NCBI BLASTx menu
        elif [[ "${program}" == "blastx" ]]; then
          ${programs_array[$program]} -help

        # Handle StringTie prepDE script
        elif [[ "${program}" == "prepDE" ]]; then
          python3 ${programs_array[$program]} -h
        fi
        ${programs_array[$program]} -h
        echo ""
        echo ""
        echo "----------------------------------------------"
        echo ""
        echo ""
      } &>> program_options.log || true

        # If MultiQC is in programs_array, copy the config file to this directory.
        if [[ "${program}" == "multiqc" ]]; then
          cp --preserve ~/.multiqc_config.yaml multiqc_config.yaml
        fi
      done
      echo "Finished logging programs options."
      echo ""
    fi


    # Document programs in PATH (primarily for program version ID)
    echo "Logging system $PATH..."
    {
    date
    echo ""
    echo "System PATH for $SLURM_JOB_ID"
    echo ""
    printf "%0.s-" {1..10}
    echo "${PATH}" | tr : \\n
    } >> system_path.log
    echo "Finished logging system $PATH."
    ```

To run the `commands.sh` script above in our conatiner on Klone, we would use the following SLURM script, which we'll call `example-SLURM-script.sh`.

This example will perform the following:

- Request the slice assigned to our account (`--account=srlab`)
- Request the parition on the `srlab` slice (`--partition=cpu-g2-mem2x`)
- Set a run time of 10 days (`--time=10-00:00:00`)
- Requst 120GB of memory (`--mem=120G`)
- Identify the most recent version of the bioinformatics container to use.
- Run the `commands.sh` script from the bioinformatics container to constuct a bowtie2 index of the provided genome FastA.

NOTE: This is written to assume that the `commands.sh` script and the SLURM script are in the same directory.

```bash
#!/bin/bash
## Job Name
#SBATCH --job-name=DESCRIPTIVE_JOB_NAME
## Allocation Definition
#SBATCH --account=srlab
#SBATCH --partition=cpu-g2-mem2x
## Resources
## Nodes
#SBATCH --nodes=1
## Walltime (days-hours:minutes:seconds format)
#SBATCH --time=10-00:00:00
## Memory per node
#SBATCH --mem=120G
##turn on e-mail notification
#SBATCH --mail-type=ALL
#SBATCH --mail-user=$USER@uw.edu
## Specify the working directory for this job
#SBATCH --chdir=/gscratch/scrubbed/$USER/to/your/desired/directory
###################################################################################

# Exit script if any command fails
set -e

# Get most recent container git hash
git_commit_hash=$(find /gscratch/srlab/containers/ \
-name "srlab-bioinformatics-container*" \
-printf "%T+ %p\n" \
| sort -n \
| awk -F[-.] 'NR == 1 {print $7}')

# Load modules
module load apptainer

# Execute Roberts Lab bionformatics container
# Binds home directory
# Binds /gscratch directory
# Directory bindings allow outputs to be written to the hard drive.
apptainer exec \
--home "$PWD" \
--bind /mmfs1/home/ \
--bind /mmfs1/gscratch/ \
/gscratch/srlab/containers/srlab-bioinformatics-container-"${git_commit_hash}$".sif \
commands.sh
```

Finally, to submit the job to SLURM:

```bash
sbatch example-SLURM-script.sh
```

This will execute `example-SLURM-script.sh` which contains instructions for submitting it into the SLURM job scheduler and onto our slice (the header portion). The rest of the script will then be executed, which will result in the execution of `commands.sh`.


## SLURM Script Template/Example - Single Command

Less likely to be used, as many of our analyses require multiple steps, but is still useful to know.

```bash
#!/bin/bash
## Job Name
#SBATCH --job-name=DESCRIPTIVE_JOB_NAME
## Allocation Definition
#SBATCH --account=srlab
#SBATCH --partition=cpu-g2-mem2x
## Resources
## Nodes
#SBATCH --nodes=1
## Walltime (days-hours:minutes:seconds format)
#SBATCH --time=10-00:00:00
## Memory per node
#SBATCH --mem=120G
##turn on e-mail notification
#SBATCH --mail-type=ALL
#SBATCH --mail-user=$USER@uw.edu
## Specify the working directory for this job
#SBATCH --chdir=/gscratch/scrubbed/$USER/to/your/desired/directory
###################################################################################

# Exit script if any command fails
set -e

# Get most recent container git hash
git_commit_hash=$(find /gscratch/srlab/containers/ \
-name "srlab-bioinformatics-container*" \
-printf "%T+ %p\n" \
| sort -n \
| awk -F[-.] 'NR == 1 {print $7}')

# Load modules
module load apptainer

# Execute Roberts Lab bionformatics container
# Binds home directory
# Binds /gscratch directory
# Directory bindings allow outputs to be written to the hard drive.
apptainer exec \
--home "$PWD" \
--bind /mmfs1/home/ \
--bind /mmfs1/gscratch/ \
/gscratch/srlab/containers/srlab-bioinformatics-container-"${git_commit_hash}$".sif \
bowtie2_build \
--threads 28 \
/gscratch/scrubbed/"$USER"/data/C_gigas/genomes/cgig-ncbi-genome.fasta \
cgig-ncbi-genome
```

