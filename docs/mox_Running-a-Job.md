`sbatch` is the main execution command for the job scheduler ([slurm](https://slurm.schedmd.com/overview.html)). It spools up an execute node for long term or compute intensive tasks such as assemblies, blasts, or other things of that nature.

`sbatch` can be run from a login node with the command
 `
```
sbatch shell.script
```

`sbatch` requires a shell script to function, with two main parts, the header and the execute portion.

## The Header

<pre>
<code>
#!/bin/bash
## Job Name
#SBATCH --job-name=<b>myjob</b>
## Allocation Definition
#SBATCH --account=srlab
#SBATCH --partition=srlab
## Nodes
#SBATCH --nodes=<b>n</b>
## Walltime (days-hours:minutes:seconds format)
#SBATCH --time=<b>dd-hh:mm:ss</b>
## Memory per node
#SBATCH --mem=<b>500G</b>
##turn on e-mail notification
#SBATCH --mail-type=ALL
#SBATCH --mail-user=$USER
## Specify the working directory for this job
#SBATCH --chdir=<b>/gscratch/srlab/path/to/your/desired/directory</b>
</code>
</pre>


<b>Bolded sections must be changed prior to execution.</b>

- `--job-name=`**`myjob`** is just an identifier for the system. It's what shows up in `scontrol` and `squeue` calls.

- `--nodes=`<b>`n`</b> Replace `n` with the number of nodes (maximum 2).

- `--time=`**`dd-hh:mm:ss`** is the "wall" time, or how long we are reserving the node for our use. This argument requires some consideration and knowledge about the program you're running prior to execution. Selecting too little wall time will cause the scheduler to kill your process mid-run when time runs out. Selecting too much time limits other's ability to use Hyak functions, but the scheduler releases a node upon program completion usually, so this is a secondary consideration.

- `--mem=`**`500G`** specifies how much memory (RAM) to allocate to the process. We have two nodes with two different amounts of RAM: 512GB and 128GB. The amount entered will determine which node is assigned to your job. E.g. if two jobs are submitted that request >128GB RAM, then the jobs will be run sequentially, in the order they were submitted, because there is only one node that has >128GB of RAM.

- `--chdir=`**`/gscratch/srlab/path/to/your/desired/directory`** indicates the working directory where output will be written, and how things will be referenced inside of the home node. Ideally this will be on the `/gscratch/srlab/` drive, but there's no requirement for this. See the [Data Storage & System Organization section of the wiki](https://github.com/RobertsLab/hyak_mox/wiki/Data-Storage-&-System-Organization) for more info.

## The Execute portion

This section contains the commands you want executed. You can treat it like the command line in that it executes commands sequentially as input. These can include program calls, module loading, making directories, etc. See the Full Example script below.


## Full Example script

The script below (named `Plat_Illu_Run2.sh`) specifies a job called "Oly_Platanus_Illu" and requests a single node,  720hrs of computing time, using 500G of RAM.

_NOTE: Since only a single node is requested, another job could be submitted and run simultaneously on our other node, but the job would have to request <=128GB of RAM (the max on the available node)._

The actual jobs that follow the ```sbatch``` header loads the Anaconda module (which is used to load a Python environment), makes a new directory in ```/scr/srlab/seanb80/plat_illu_tmp```, runs the ```platanus``` program on a set of files, and then runs the ```redundans``` programm on a set of files.

To run the script below, one would enter the following in a login node:

```sbatch Plat_Illu_Run2.sh```

```bash
#!/bin/bash
## Job Name
#SBATCH --job-name=Oly_Platanus_Illu
## Resources
## Nodes
#SBATCH --nodes=1
## Walltime (720 hours)
#SBATCH --time=720:00:00
## Memory per node
#SBATCH --mem=500G
## Specify the working directory for this job
#SBATCH --chdir=/gscratch/srlab/data/Oly_Plat_Illu2/

module load anaconda2_4.3.1

mkdir -p /scr/srlab/seanb80/plat_illu_tmp

/gscratch/srlab/programs/platanus_1.2.4/platanus assemble \
-f /gscratch/srlab/data/OlyData/Illumina/trimmed/*.fq.fq \
-t 28 \
-k 20 \
-u 0.2 \
-o Oly_Out_ \
-m 500

/gscratch/srlab/programs/redundans/redundans.py \
-t 28 \
-v \
-l /gscratch/srlab/data/OlyData/PacBio/170210_PCB-CC_MS_EEE_20kb_P6v2_D01_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170228_PCB-CC_AL_20kb_P6v2_C01_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170228_PCB-CC_AL_20kb_P6v2_D01_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170228_PCB-CC_AL_20kb_P6v2_E01_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170307_PCB-CC_AL_20kb_P6v2_C01_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170307_PCB-CC_AL_20kb_P6v2_C02_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170314_PCB-CC_20kb_P6v2_A01_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170314_PCB-CC_20kb_P6v2_A02_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170314_PCB-CC_20kb_P6v2_A03_1_filtered_subreads.fastq /gscratch/srlab/data/OlyData/PacBio/170314_PCB-CC_20kb_P6v2_A04_1_filtered_subreads.fastq \
-f /gscratch/srlab/data/Oly_Plat_Illu/Oly_Out__contig.fa \
-o /gscratch/srlab/data/Oly_Redundans_Run2

```

## SBATCH Script Template/Example

```bash
#!/bin/bash
## Job Name
#SBATCH --job-name=DESCRIPTIVE_JOB_NAME
## Allocation Definition
#SBATCH --account=srlab
#SBATCH --partition=srlab
## Resources
## Nodes
#SBATCH --nodes=1
## Walltime (days-hours:minutes:seconds format)
#SBATCH --time=10-00:00:00
## Memory per node
#SBATCH --mem=120G
##turn on e-mail notification
#SBATCH --mail-type=ALL
#SBATCH --mail-user=YOUR_UW_NET_ID@uw.edu
## Specify the working directory for this job
#SBATCH --chdir=/gscratch/scrubbed/path/to/your/desired/directory

# Requires Bash >=4.0, as script uses associative arrays.

###################################################################################
# These variables need to be set by user

## Number of CPU threads to use for programs (if applicable)
threads=28

## Program paths
bowtie2_dir="/gscratch/srlab/programs/bowtie2-2.4.2-linux-x86_64"
samtools="/gscratch/srlab/programs/samtools-1.10/samtools"

## Programs associative array
## Using array is useful for logging program options (see end of script)
declare -A programs_array

programs_array=(
[bowtie2]="${bowtie2_dir}/bowtie2" \
[bowtie2_build]="${bowtie2_dir}/bowtie2-build" \
[samtools_index]="${samtools} index" \
[samtools_sort]="${samtools} sort" \
[samtools_view]="${samtools} view"
)



###################################################################################

# Exit script if any command fails
set -e

# Load Python Mox module for Python module availability
module load intel-python3_2017


## PUT COMMANDS IN THIS SECTION

## CALL PROGRAMS FROM ARRAY
${programs_array[bowtie2_build]} \
--threads ${threads} \
${transcriptomes_array[$transcriptome]} \
${transcriptome_name}


###################################################################################

## Capture program options
## Expects program options to be accessible via an "-h" argument,
## but has exceptions for some other commonly used programs (e.g. samtools, multiqc)
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

echo ""
echo "Finished logging program options."
echo ""

echo ""
echo "Logging system PATH."

# Document programs in PATH (primarily for program version ID)
{
date
echo ""
echo "System PATH for $SLURM_JOB_ID"
echo ""
printf "%0.s-" {1..10}
echo "${PATH}" | tr : \\n
} >> system_path.log

echo "Finished logging system PATH"
```
