Introductory guide to transcriptome assembly using [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) and short-read sequencing data.

## QC

A normal starting point would be having raw sequence data provided by a core facility. When downloading said data you need to make sure you check the integrity of the files after transfer by confirming checksum hashes (usually `MD5` checksums) match those provided by the sequencing facility. 

You should run [`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess sequencing quality. This might vary based on the details of your project but generally you can ID outliers and those samples with poor read quality. Presence of adapters can also be visualized.


## Trimming

Quality and adapter trimming is required prior to assembly. [`fastp`](https://github.com/OpenGene/fastp) is recommended due to its speed and FastQC-like report(s). Additionally, the output from [`fastp`](https://github.com/OpenGene/fastp) can also be analyzed by [`MultiQC`](https://multiqc.info/) (requires a "plug-in"). Trimmed files should be passed through `[`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) and assessed. Although rare, some projects may require a second round of trimming.

Alternatively, [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has trimming capabilities built in, using [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic). Although convenient, it limits the ability to assess post-trimming sequencing data prior to assembly.

## Assembly

[`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) is the _de facto_ standard. It is well-documented, well-supported, and actively updated. Additionally, the developer is very responsive, considerate, and helpful to [all GitHub Issues](https://github.com/trinityrnaseq/trinityrnaseq/issues).

[`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) is powerful and has complex, but useful options availalbe. Take time to consider how you will use your assembly for later analysis. [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has many options available for downstream analysis (e.g. [gene expression](#gene-expression)) that can be simplified with careful planning prior to assembly.

Due to the intensive processing required for assembly (high CPU and RAM usage), it is highly recommended to run all assemblies on an [execute node on Mox](https://robertslab.github.io/resources/mox_Node-Types/). As such, all code examples are written with the assumption that the commands are being run on Mox.

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

A _de novo_ assembly is an assembly that is done without the use of a reference genome. Here's an example command, using paired-end reads:

```shell
${trinity_dir}/Trinity \
--seqType fq \
--SS_lib_type RF \
--max_memory 100G \
--CPU ${threads} \
--samples_file ${samples}
```

- `--max_memory 100G` should _not_ be changed, per communications with the developer.

#### Use cases from our lab

- [Transcriptome-Assembly-C.bairdi-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox](https://robertslab.github.io/sams-notebook/2020/03/30/Transcriptome-Assembly-C.bairdi-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox.html)

### Genome-guided assembly

A genome-guided assembly is an assembly which utilizes a reference genome. This requires a sorted BAM as input, which means you have to have previously aligned your RNA-seq reads to a reference genome. See our Handbook entry on using [Hisat2](https://robertslab.github.io/resources/bio-Gene-expression/#alignment-hisat2) for read alignment. Here's an example command, using paired-end reads

```shell
${programs_array[trinity]} \
--genome_guided_bam ${sorted_bam} \
--genome_guided_max_intron ${max_intron} \
--seqType fq \
--SS_lib_type RF \
--max_memory 100GB \
--CPU ${threads} \
--samples_file ${samples}
```

- `--genome_guided_max_intron ${max_intron}`: The value used in the [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) examples is 10000.

- `--max_memory 100G` should _not_ be changed, per communications with the developer.

#### Use cases from our lab

- [Transcriptome-Assembly-Genome-guided-C.virginica-Adult-Gonad-OA-RNAseq-Using-Trinity-on-Mox](https://robertslab.github.io/sams-notebook/2022/02/07/Transcriptome-Assembly-Genome-guided-C.virginica-Adult-Gonad-OA-RNAseq-Using-Trinity-on-Mox.html)

## Gene expression

## Annotation