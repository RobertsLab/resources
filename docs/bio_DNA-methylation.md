# DNA Methylation Analysis

This page is a practical starting point for DNA methylation analysis in the lab. It focuses on common bisulfite sequencing workflows: aligning reads, extracting methylation calls, calling variants from bisulfite data, testing differential methylation, and summarizing methylation across genes.

Most users should start with a clear analysis goal, confirm the required inputs, then choose one of the workflows below. The examples are lab-specific and should be checked against the official tool documentation before use.

## Quick Start

1. Confirm that you have raw FASTQ files or existing bisulfite BAM files.
2. Confirm that you have the correct reference genome FASTA and index files.
3. Decide whether you need alignment, variant calling, differential methylation, or gene-level summaries.
4. Use the table below to choose the relevant tool.
5. Run a small test before submitting a full HPC job.

## Which Workflow Should I Use?

| Goal | Tool | Input | Output | Use when |
| --- | --- | --- | --- | --- |
| Align bisulfite reads and extract methylation calls | Bismark | FASTQ files and reference genome | BAM files, coverage files, cytosine reports, HTML reports | You want a transparent step-by-step workflow for bisulfite sequence processing. |
| Run a whole-genome bisulfite sequencing pipeline | `EpiDiverse/wgbs` | FASTQ files and reference genome | Pipeline-managed WGBS outputs | You want a Nextflow pipeline instead of running each step manually. |
| Call SNPs from bisulfite data | BS-Snper | Bisulfite alignments | Variant calls | You need variants from bisulfite sequence data. |
| Call variants or clusters from bisulfite BAMs | `EpiDiverse/snp` | BAM files and reference genome | Variant and cluster outputs | You want a Nextflow workflow for SNP-related analysis. |
| Analyze differential methylation | methylKit | Methylation count or coverage files | Differential methylation results and plots | You have methylation calls and want statistics in R. |
| Summarize gene-level methylation | Gene methylation workflows | Methylation calls and genome annotations | Gene-level methylation summaries | You want methylation summarized by genes or genomic features. |

## Prerequisites

Before starting, make sure you have:

- Raw FASTQ files, or BAM files if starting after alignment.
- A reference genome FASTA.
- A FASTA index file when required by the selected workflow.
- A Bismark genome folder if using Bismark alignment.
- Access to the relevant compute environment, usually Mox or Raven.
- A working SLURM script for HPC runs.
- The needed software environment, such as a conda environment or installed program path.
- A small test dataset or subset for checking paths and parameters.

## Bismark: Align Reads and Extract Methylation

Bismark is the main step-by-step workflow shown here for bisulfite read alignment and methylation extraction.

Official documentation:

- [Bismark User Guide](https://felixkrueger.github.io/Bismark/)
- [Babraham Bioinformatics Bismark page](https://www.bioinformatics.babraham.ac.uk/projects/bismark/)

Typical Bismark workflow:

1. Prepare the genome.
2. Align reads.
3. Deduplicate alignments when appropriate.
4. Extract methylation calls.
5. Generate reports and summaries.

Deduplication is recommended for whole-genome bisulfite samples, but should not be used for reduced-representation libraries such as RRBS, amplicon, or target-enrichment libraries.

??? example "Bismark command example"

    Always check the official manual before running these commands. This example shows the general lab workflow, not a universal recipe.

    **Prepare the genome**

    Usage:

    ```text
    bismark_genome_preparation [options] <path_to_genome_folder>
    ```

    Example:

    ```shell
    ${bismark_dir}/bismark_genome_preparation \
    --verbose \
    --parallel 28 \
    --path_to_aligner ${bowtie2_dir} \
    ${genome_folder}
    ```

    You should expect a prepared genome directory structure similar to:

    ```text
    ./roslin_M/Bisulfite_Genome
    ./roslin_M/Bisulfite_Genome/GA_conversion
    ./roslin_M/Bisulfite_Genome/CT_conversion
    ```

    **Align reads**

    Usage:

    ```text
    bismark [options] --genome <genome_folder> {-1 <mates1> -2 <mates2> | <singles>}
    ```

    Example:

    ```shell
    find ${reads_dir}*_R1_001_val_1.fq.gz \
    | xargs basename -s _R1_001_val_1.fq.gz | xargs -I{} ${bismark_dir}/bismark \
    --path_to_bowtie ${bowtie2_dir} \
    -genome ${genome_folder} \
    -p 4 \
    -score_min L,0,-0.6 \
    --non_directional \
    -1 ${reads_dir}{}_R1_001_val_1.fq.gz \
    -2 ${reads_dir}{}_R2_001_val_2.fq.gz \
    -o Mcap_tg
    ```

    This creates BAM files.

    **Deduplicate alignments**

    Usage:

    ```text
    deduplicate_bismark --bam [options] <filenames>
    ```

    Example:

    ```shell
    find *.bam | \
    xargs basename -s .bam | \
    xargs -I{} ${bismark_dir}/deduplicate_bismark \
    --bam \
    --paired \
    {}.bam
    ```

    This creates deduplicated BAM files.

    **Extract methylation calls**

    Usage:

    ```text
    bismark_methylation_extractor [options] <filenames>
    ```

    Example:

    ```shell
    ${bismark_dir}/bismark_methylation_extractor \
    --bedGraph --counts --scaffolds \
    --multicore 14 \
    --buffer_size 75% \
    *deduplicated.bam
    ```

    Alternative example:

    ```shell
    ${bismark_dir}/bismark_methylation_extractor \
    --bedGraph \
    --counts \
    --comprehensive \
    --merge_non_CpG \
    --multicore 28 \
    --buffer_size 75% \
    *deduplicated.bam
    ```

    **Generate reports**

    ```shell
    ${bismark_dir}/bismark2report
    ```

    ```shell
    ${bismark_dir}/bismark2summary
    ```

    Example report formats:

    - [Bismark paired-end report](https://www.bioinformatics.babraham.ac.uk/projects/bismark/PE_report.html)
    - [Bismark summary report](https://www.bioinformatics.babraham.ac.uk/projects/bismark/bismark_summary_report.html)

??? note "Expected Bismark output formats"

    The methylation extractor creates files such as `deduplicated.bismark.cov.gz`. When using `--bedGraph`, the uncompressed coverage output has this format:

    ```text
    NC_035784.1 141 141 37.5    3   5
    NC_035784.1 142 142 100 2   0
    NC_035784.1 155 155 70  7   3
    NC_035784.1 156 156 100 2   0
    NC_035784.1 291 291 0   0   2
    NC_035784.1 292 292 0   0   3
    NC_035784.1 313 313 0   0   1
    NC_035784.1 314 314 66.6666666666667    2   1
    NC_035784.1 470 470 66.6666666666667    4   2
    NC_035784.1 611 611 0   0   4
    ```

    Columns:

    ```text
    <chromosome> <start position> <end position> <methylation percentage> <count methylated> <count unmethylated>
    ```

    To create a genome-wide cytosine report from coverage output, use `coverage2cytosine`:

    ```shell
    find *deduplicated.bismark.cov.gz \
    | xargs basename -s _trimmed_bismark_bt2.deduplicated.bismark.cov.gz \
    | xargs -I{} ${bismark_dir}/coverage2cytosine \
    --genome_folder ${genome_folder} \
    -o {} \
    --merge_CpG \
    --zero_based \
    {}_trimmed_bismark_bt2.deduplicated.bismark.cov.gz
    ```

    This generates a file ending in `.CpG_report.merged_CpG_evidence.cov`.

    Example:

    ```text
    NC_035785.1 217 219 100.000000  17  0
    NC_035785.1 523 525 87.500000   7   1
    NC_035785.1 556 558 50.000000   5   5
    NC_035785.1 727 729 100.000000  16  0
    NC_035785.1 1330    1332    0.000000    0   2
    NC_035785.1 1403    1405    0.000000    0   2
    NC_035785.1 1494    1496    66.666667   2   1
    NC_035785.1 1747    1749    100.000000  8   0
    NC_035785.1 2024    2026    100.000000  24  0
    NC_035785.1 2054    2056    93.333333   14  1
    ```

### Bismark Lab Examples

- <https://github.com/RobertsLab/code/blob/master/20-bismark.sh>
- <https://github.com/sr320/paper-oly-mbdbs-gen/blob/master/code/00-Bismark.sh> - processes BS-MBDSeq data from Olympia oysters on Mox. Author: Steven Roberts. ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/paper-oly-mbdbs-gen)
- <https://raw.githubusercontent.com/laurahspencer/C.magister_methyl-oa/master/scripts/20201214_Cmag_bismark-align.sh> - SLURM script used to process MiSeq data from Dungeness crab on Mox. [Jupyter Notebook with details](https://github.com/laurahspencer/C.magister_methyl-oa/blob/master/notebooks/MBD-01%20Processing%20QC%20MiSeq%20data.ipynb). Author: Laura Spencer, derived from the [MethCompare workflow](https://github.com/hputnam/Meth_Compare). ![GitHub last commit](https://img.shields.io/github/last-commit/laurahspencer/C.magister_methyl-oa)
- <https://github.com/sr320/paper-oly-wgbs/blob/master/submission/Narrative.Rmd> - R Markdown narrative for WGBS Olympia oyster data. Author: Steven Roberts. ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/paper-oly-wgbs)
- <https://github.com/hputnam/Geoduck_Meth/blob/master/code/03-bismark.sh> - geoduck environmental memory project on Mox. Author: Steven Roberts. ![GitHub last commit](https://img.shields.io/github/last-commit/hputnam/Geoduck_Meth)
- <https://raw.githubusercontent.com/epigeneticstoocean/paper-gonad-meth/master/code/02-bismark.sh> - eastern oyster data on Mox. ![GitHub last commit](https://img.shields.io/github/last-commit/epigeneticstoocean/paper-gonad-meth)
- <https://github.com/hputnam/Meth_Compare/blob/master/code/00.01-DNA-sequence-processing.md> - complete DNA processing protocol from a comparison of bisulfite sequencing methods in corals. ![GitHub last commit](https://img.shields.io/github/last-commit/hputnam/Meth_Compare)

## EpiDiverse/wgbs: Pipeline Option

`EpiDiverse/wgbs` is a Nextflow pipeline for WGBS analysis.

Official documentation:

- <https://github.com/EpiDiverse/wgbs>

Use this when you want a pipeline-managed WGBS workflow rather than a manual Bismark workflow.

??? example "Run EpiDiverse/wgbs on Mox"

    Add the following code below your SLURM header. Replace items enclosed in angle brackets with your own paths.

    ```shell
    # Load Anaconda
    # Unknown why this is needed, but Anaconda will not run if this line is not included.
    . "/gscratch/srlab/programs/anaconda3/etc/profile.d/conda.sh"

    # Activate the EpiDiverse/wgbs Anaconda environment
    conda activate epidiverse-wgbs_env
    ```

    ```shell
    # Run Nextflow EpiDiverse/wgbs pipeline
    # Expects paired end, gzipped FastQ files named *.fastq.gz. Add --SE for single end data.
    # Genome FastA must have a corresponding FastA index file.
    # Can perform trimming if desired. Add --trim.
    # Can run FastQC after trimming. Add --fastqc.
    NXF_VER=20.07.1 \
    /gscratch/srlab/programs/nextflow \
    /gscratch/srlab/programs/epidiverse-pipelines/wgbs \
    --input <path to directory with *.fastq.gz files> \
    --reference <path to genome FastA> \
    --INDEX
    ```

## Variant Calling From Bisulfite Data

Variant calling from bisulfite data requires tools that are aware of bisulfite conversion.

### BS-Snper

Official documentation:

- <https://github.com/hellbelly/BS-Snper>

Lab example:

- <https://nbviewer.org/github/RobertsLab/project-gigas-oa-meth/blob/master/code/07-BS-SNPer.ipynb> - Pacific oyster exposed to ocean acidification. Author: Yaamini Venkataraman. ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/project-gigas-oa-meth)

### EpiDiverse/snp

`EpiDiverse/snp` is a Nextflow pipeline for SNP-related analysis from bisulfite data.

Official documentation:

- <https://github.com/EpiDiverse/snp>

??? example "Run EpiDiverse/snp on Mox"

    Add this below your SLURM script header. Replace `bams_dir` and `genome_fasta` locations with your own.

    A FASTA index file needs to be present in the same directory as your genome FASTA file.

    ```shell
    # These variables need to be set by user

    # Directory with BAM(s)
    bams_dir="/gscratch/scrubbed/samwhite/data/C_virginica/BSseq/120321-cvBS"

    # Location of EpiDiverse/snp pipeline directory
    epi_snp="/gscratch/srlab/programs/epidiverse-pipelines/snp"

    # FastA file is required to end with .fa
    # Requires FastA index file to be present in same directory as FastA
    genome_fasta="/gscratch/srlab/sam/data/C_virginica/genomes/GCF_002022765.2_C_virginica-3.0_genomic.fa"

    # Location of Nextflow
    nextflow="/gscratch/srlab/programs/nextflow-21.10.6-all"

    # Specify desired/needed version of Nextflow
    nextflow_version="20.07.1"

    # Exit script if a command fails
    set -e

    # Load Anaconda
    # Unknown why this is needed, but Anaconda will not run if this line is not included.
    . "/gscratch/srlab/programs/anaconda3/etc/profile.d/conda.sh"

    # Activate EpiDiverse/snp conda environment
    conda activate epidiverse-snp_env

    # Count BAMs
    # Needed to pass info to EpiDiverse/snp and avoid artificial file count limitation.
    bam_count=0

    for bam in ${bams_dir}*.bam
    do
      # Increments counter by 1 for each BAM
      ((bam_count++))
    done

    # Run EpiDiverse/snp
    NXF_VER=${nextflow_version} \
    ${nextflow} run \
    ${epi_snp} \
    --input ${bams_dir} \
    --reference ${genome_fasta} \
    --variants \
    --clusters \
    --take ${bam_count}
    ```

## methylKit: Differential Methylation Analysis

methylKit is an R package for methylation statistics and visualization after methylation calls have already been generated.

Official documentation:

- [methylKit vignette](https://bioconductor.org/packages/release/bioc/vignettes/methylKit/inst/doc/methylKit.html)

Lab examples:

- <https://github.com/sr320/paper-oly-mbdbs-gen/blob/master/code/01-methylkit.Rmd> - processes BS-MBDSeq data from Olympia oysters on a personal computer. Author: Laura Spencer. ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/paper-oly-mbdbs-gen)
- <https://github.com/hputnam/Meth_Compare/blob/master/code/MethCompare_methylKit_analysis.R> - coral methylation comparison of methods. ![GitHub last commit](https://img.shields.io/github/last-commit/hputnam/Meth_Compare)
- <https://github.com/epigeneticstoocean/paper-gonad-meth/blob/master/code/04-methylkit.Rmd> - eastern oyster ocean acidification work. ![GitHub last commit](https://img.shields.io/github/last-commit/epigeneticstoocean/paper-gonad-meth)

??? info "methylKit workflow diagram"

    ![methylKit workflow diagram](https://user-images.githubusercontent.com/17264765/131020085-f32e8a51-9a29-474c-aa56-2fa599e006d9.png)

    Flowchart of possible operations by methylKit. Figure and caption adapted from [Akalin et al. 2012](https://doi.org/10.1186/gb-2012-13-10-r87).

## Gene-Level Methylation

Use gene-level methylation workflows when you already have methylation calls and want to summarize methylation by genes or genome features.

Lab example:

- <https://sr320.github.io/gene-meth/>
