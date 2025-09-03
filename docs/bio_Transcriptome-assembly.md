Introductory guide to transcriptome assembly using [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) and short-read sequencing data.

## QC

A normal starting point would be having raw sequence data provided by a core facility. When downloading said data you need to make sure you check the integrity of the files after transfer by confirming checksum hashes (usually `MD5` checksums) match those provided by the sequencing facility. 

You should run [`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess sequencing quality. This might vary based on the details of your project but generally you can ID outliers and those samples with poor read quality. Presence of adapters can also be visualized.


## Trimming

Quality and adapter trimming is required prior to assembly. [`fastp`](https://github.com/OpenGene/fastp) is recommended due to its speed and FastQC-like report(s). Additionally, the output from [`fastp`](https://github.com/OpenGene/fastp) can also be analyzed by [`MultiQC`](https://multiqc.info/) (requires a "plug-in"). Trimmed files should be passed through [`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) and assessed. Although rare, some projects may require a second round of trimming.

Alternatively, [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has trimming capabilities built in, using [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic). Although convenient, it limits the ability to assess post-trimming sequencing data prior to assembly.

## Assembly

[`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) is the _de facto_ standard. It is well-documented, well-supported, and actively updated. Additionally, the developer is very responsive, considerate, and helpful to [all GitHub Issues](https://github.com/trinityrnaseq/trinityrnaseq/issues).

[`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) is powerful and has complex, but useful options availalbe. Take time to consider how you will use your assembly for later analysis. [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has many options available for downstream analysis (e.g. [gene expression](#gene-expression)) that can be simplified with careful planning prior to assembly.

Due to the intensive processing required for assembly (high CPU and RAM usage), it is highly recommended to run all assemblies on a high-performance computing cluster such as UW's Klone or Raven systems.

### Sample list file

It is recommended to create a sample list file for [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) to use. One of the biggest benefits is that this sample file list can be used for other downstream operations in the [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) pipeline. Additionally, it's an easy way to document which sequencing files were used for assembly. Here's the example from [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki). Sample file list is tab-delimited like this:

```
cond_A    cond_A_rep1    A_rep1_left.fq    A_rep1_right.fq
cond_A    cond_A_rep2    A_rep2_left.fq    A_rep2_right.fq
cond_B    cond_B_rep1    B_rep1_left.fq    B_rep1_right.fq
cond_B    cond_B_rep2    B_rep2_left.fq    B_rep2_right.fq
```

### Stranded sequencing reads

[`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has the option (`--SS_lib_type`) to specify whether or not the sequences you're assembly are "stranded". This is dependent upon the library construction. With that said, most paired-end RNA-seq project libraries are constructed using Illumina's stranded kit. As such, the user should specify this in the following fashion as on option in the [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) command (example specifies typical stranded libraries): `--SS_lib_type RF`

If you do not know whether your libraries are stranded or not (for example, if you downloaded RNA-seq data from NCBI and the metadata doesn't indicate library construction methodology), [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has a built-in tool to help assess your sequencing reads, _after_ assembly:

[Examine-Strand-Specificity](https://github.com/trinityrnaseq/trinityrnaseq/wiki/Examine-Strand-Specificity)



### _De novo_ assembly

A _de novo_ assembly is an assembly that is done without the use of a reference genome. Here's an example command, using trimmed paired-end reads. This set of commands will assembly the reads into contigs, generate assembly statistics, a gene map file (maps isoforms to "gene" names), and a sequence length file (useful for downstream gene expression).

```shell
# Perform assembly
${trinity_dir}/Trinity \
--seqType fq \
--SS_lib_type RF \
--max_memory 100G \
--CPU ${threads} \
--samples_file ${samples}

# Assembly stats
${trinity_dir}/util/TrinityStats.pl \
trinity_out_dir/"${fasta_name}" \
> ${assembly_stats}

# Create gene map files
${trinity_dir}/util/support_scripts/get_Trinity_gene_to_trans_map.pl \
trinity_out_dir/"${fasta_name}" \
> "${fasta_name}".gene_trans_map

# Create sequence lengths file (used for differential gene expression)
${trinity_dir}/util/misc/fasta_seq_length.pl \
trinity_out_dir/"${fasta_name}" \
> "${fasta_name}".seq_lens
```

- `--max_memory 100G` should _not_ be changed, per communications with the developer.

Another example via SR
```
export PATH=/home/shared/jellyfish-2.3.0/bin:$PATH
export PATH=/home/shared/bowtie2-2.4.4-linux-x86_64/:$PATH
export PATH=/home/shared/salmon-1.4.0_linux_x86_64/bin:$PATH
/home/shared/trinityrnaseq-v2.12.0/Trinity \
--seqType fq \
--max_memory 50G \
--CPU 8 \
--left ../data/raw/der/PSC-0517_R1_001.fastq.gz \
--right ../data/raw/der/PSC-0517_R2_001.fastq.gz \
--output ../output/01-data-explore/trinity
```

#### Use cases from our lab

- [Transcriptome-Assembly-C.bairdi-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox](https://robertslab.github.io/sams-notebook/2020/03/30/Transcriptome-Assembly-C.bairdi-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox.html)

### Genome-guided assembly

A genome-guided assembly is an assembly which utilizes a reference genome. This requires a sorted BAM as input, which means you have to have previously aligned your RNA-seq reads to a reference genome. See our Handbook entry on using [Hisat2](https://robertslab.github.io/resources/bio-Gene-expression/#alignment-hisat2) for read alignment. Here's an example command, using trimmed paired-end reads. This set of commands will assembly the reads into contigs, generate assembly statistics, a gene map file (maps isoforms to "gene" names), and a sequence length file (useful for downstream gene expression).

```shell
# Perform assembly
${programs_array[trinity]} \
--genome_guided_bam ${sorted_bam} \
--genome_guided_max_intron ${max_intron} \
--seqType fq \
--SS_lib_type RF \
--max_memory 100GB \
--CPU ${threads} \
--samples_file ${samples}

# Assembly stats
${trinity_dir}/util/TrinityStats.pl \
trinity_out_dir/"${fasta_name}" \
> ${assembly_stats}

# Create gene map files
${trinity_dir}/util/support_scripts/get_Trinity_gene_to_trans_map.pl \
trinity_out_dir/"${fasta_name}" \
> "${fasta_name}".gene_trans_map

# Create sequence lengths file (used for differential gene expression)
${trinity_dir}/util/misc/fasta_seq_length.pl \
trinity_out_dir/"${fasta_name}" \
> "${fasta_name}".seq_lens
```

- `--genome_guided_max_intron ${max_intron}`: The value used in the [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) examples is 10000.

- `--max_memory 100G` should _not_ be changed, per communications with the developer.

#### Use cases from our lab

- [Transcriptome-Assembly-Genome-guided-C.virginica-Adult-Gonad-OA-RNAseq-Using-Trinity-on-Mox](https://robertslab.github.io/sams-notebook/2022/02/07/Transcriptome-Assembly-Genome-guided-C.virginica-Adult-Gonad-OA-RNAseq-Using-Trinity-on-Mox.html)

## Output files

Both types of assemblies listed above will generate your assembly as a FastA file:

- `Trinity.fasta`: This is the default name.

If you ran the commands above you will also get the following files:

- `assembly_stats.txt`: Statistics on your assembly. Will look something like this:

    ```
    ################################
    ## Counts of transcripts, etc.
    ################################
    Total trinity 'genes':	887315
    Total trinity transcripts:	1849486
    Percent GC: 36.26

    ########################################
    Stats based on ALL transcript contigs:
    ########################################

    Contig N10: 7967
    Contig N20: 5284
    Contig N30: 3814
    Contig N40: 2801
    Contig N50: 2062

    Median contig length: 562
    Average contig: 1117.46
    Total assembled bases: 2066718534


    #####################################################
    ## Stats based on ONLY LONGEST ISOFORM per 'GENE':
    #####################################################

    Contig N10: 6904
    Contig N20: 4398
    Contig N30: 3003
    Contig N40: 2120
    Contig N50: 1501

    Median contig length: 434
    Average contig: 860.79
    Total assembled bases: 763788564
    ```

- `Trinity.fasta.gene_trans_map`:

    ```
    TRINITY_GG_1_c20044_g1	TRINITY_GG_1_c20044_g1_i2
    TRINITY_GG_1_c20044_g1	TRINITY_GG_1_c20044_g1_i4
    TRINITY_GG_1_c27757_g4	TRINITY_GG_1_c27757_g4_i1
    TRINITY_GG_1_c4646_g1	TRINITY_GG_1_c4646_g1_i1
    TRINITY_GG_1_c31636_g3	TRINITY_GG_1_c31636_g3_i1
    TRINITY_GG_1_c5375_g1	TRINITY_GG_1_c5375_g1_i2
    TRINITY_GG_1_c5375_g1	TRINITY_GG_1_c5375_g1_i7
    TRINITY_GG_1_c5375_g1	TRINITY_GG_1_c5375_g1_i5
    TRINITY_GG_1_c5375_g1	TRINITY_GG_1_c5375_g1_i6
    TRINITY_GG_1_c5375_g1	TRINITY_GG_1_c5375_g1_i4
    TRINITY_GG_1_c5375_g1	TRINITY_GG_1_c5375_g1_i1
    ```

- `Trinity.fasta.seq_lens`:

    ```
    #fasta_entry	length
    TRINITY_GG_1_c20044_g1_i2	1058
    TRINITY_GG_1_c20044_g1_i4	1057
    TRINITY_GG_1_c27757_g4_i1	265
    TRINITY_GG_1_c4646_g1_i1	347
    TRINITY_GG_1_c31636_g3_i1	215
    TRINITY_GG_1_c5375_g1_i2	324
    TRINITY_GG_1_c5375_g1_i7	511
    TRINITY_GG_1_c5375_g1_i5	349
    TRINITY_GG_1_c5375_g1_i6	340
    ```

## Gene expression

## Annotation
