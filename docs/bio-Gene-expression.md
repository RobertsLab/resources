This primarily refers to dealing with transcriptome wide analysis (eg RNA-seq, tag-seq). Please see also Roberts and Gavery (2018) [Opportunities in Functional Genomics: A Primer on Lab and Computational Aspects](http://eagle.fish.washington.edu/whale/pub/jsr37309_1r8rd0.pdf)
There are several workflows out there, but here we outline common workflows in our lab.

## QC
A normal starting point would be having raw sequence data provided by a core facility. When downloading said data you need to make sure you check the integrity by making sure the hash at the source is the same once you get it to where you want to analyse it. 

To begin with, you should run fastqc to assess quality. This might vary based on the details of your project but generally you can ID outliers and those samples with poor read quality. Presence of adapters can also be visualized.


## trimming
It is debatable how necessary how necessary trimming reads is, though if done correctly there is likely no reason it is detrimental.


## reference choice
The next step is to take the sequence reads, align, and compare counts. Alignent be done using either a transcriptome or genome. Distinct software that is genome-aware will be needed for the latter. 


## alignment: kallisto (pseudo-alignment)
See the official documentation.

User Guides

### Use cases from our lab

- <https://github.com/RobertsLab/paper-tanner-crab/blob/master/notebooks/kallisto-4libraries.ipynb> tanner crab ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/paper-tanner-crab)


## Alignment: [HiSat2](https://daehwankimlab.github.io/hisat2/manual/)
See the official documentation (linked above).

Benefits to using [`HISAT2`](https://daehwankimlab.github.io/hisat2/) for alignments:

- Fast.

- Can detect exon/intron junctions (i.e. alternative isoform splice sites).

For RNA-Seq, [`HISAT2`](https://daehwankimlab.github.io/hisat2/) alignments are frequently followed up using [`StringTie`](https://ccb.jhu.edu/software/stringtie/) for transcript assembly and quantitation of splice variants.

General usage:

1. Build a [`HISAT2`](https://daehwankimlab.github.io/hisat2/) reference sequence index:

    ```bash
    # Create Hisat2 exons tab file
    "${programs_array[hisat2_exons]}" \
    "${transcripts_gtf}" \
    > "${exons}"

    # Create Hisat2 splice sites tab file
    "${programs_array[hisat2_splice_sites]}" \
    "${transcripts_gtf}" \
    > "${splice_sites}"

    # Build Hisat2 reference index using splice sites and exons
    "${programs_array[hisat2_build]}" \
    "${genome_fasta}" \
    "${genome_index_name}" \
    --exon "${exons}" \
    --ss "${splice_sites}" \
    -p "${threads}" \
    2> hisat2-build_stats.txt
    ```

2. Perform alignment(s):

    ```bash
    # Hisat2 alignments
    "${programs_array[hisat2]}" \
    -x "${genome_index_name}" \
    -1 "${fastq_list_R1}" \
    -2 "${fastq_list_R2}" \
    -S "${sample_name}".sam \
    --threads "${threads}" \
    2> "${sample_name}"-hisat2_stats.txt

    # Sort SAM files, convert to BAM, and index
    ${programs_array[samtools_view]} \
    -@ "${threads}" \
    -Su "${sample_name}".sam \
    | ${programs_array[samtools_sort]} - \
    -@ "${threads}" \
    -o "${sample_name}".sorted.bam
    ${programs_array[samtools_index]} "${sample_name}".sorted.bam


    # Delete unneccessary index files
    rm "${genome_index_name}"*.ht2

    # Delete unneeded SAM files
    rm ./*.sam
    ```

See links in the "use cases" section below for full-fledged scripts and advanced usage (e.g. assigning read groups to alignment files (SAM) for improved downstream handling/accessiblity).

### Use cases from our lab

- [RNAseq Alignments - P.generosa Alignments and Alternative Transcript Identification Using Hisat2 and StringTie on Mox](https://robertslab.github.io/sams-notebook/posts/2022/2022-09-14-RNAseq-Alignments---P.generosa-Alignments-and-Alternative-Transcript-Identification-Using-Hisat2-and-StringTie-on-Mox/)

- [Splice Site Identification - S.namaycush Liver Parasitized and Non-Parasitized SRA RNAseq Using Hisat2-Stingtie with Genome GCF_016432855.1](https://robertslab.github.io/sams-notebook/posts/2022/2022-08-10-Splice-Site-Identification---S.namaycush-Liver-Parasitized-and-Non-Parasitized-SRA-RNAseq-Using-Hisat2-Stingtie-with-Genome-GCF_016432855.1/)



---

## DESeq2

See also the official documentation.

User Guides
- [Analyzing RNA-seq data with DESeq2](http://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)


### Use cases from our lab
- <https://github.com/laurahspencer/O.lurida_QuantSeq-2020/blob/master/notebooks/02-Adult-data-analysis-QuantSeq2020.Rmd> - draft code analyzing QuantSeq data from Olympia oyster gill tissue by two factors (population, pCO2 treatment). See [2020-QuantSeq-Processing_Raw-to-Counts.ipynb](https://github.com/laurahspencer/O.lurida_QuantSeq-2020/blob/master/notebooks/2020-QuantSeq-Processing_Raw-to-Counts.ipynb) and [01-Importing-data-QuantSeq2020.Rmd](https://github.com/laurahspencer/O.lurida_QuantSeq-2020/blob/master/notebooks/01-Importing-data-QuantSeq2020.Rmd) for steps prior to DeSeq2. Author: Laura Spencer  ![GitHub last commit](https://img.shields.io/github/last-commit/laurahspencer/O.lurida_QuantSeq-2020)

- <https://github.com/RobertsLab/paper-tanner-crab/blob/master/scripts/DESeq.Rmd> ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/paper-tanner-crab)
