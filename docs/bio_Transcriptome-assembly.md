Introductory guide to transcriptome assembly using [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) and short-read sequencing data.

## QC

A normal starting point would be having raw sequence data provided by a core facility. When downloading said data you need to make sure you check the integrity of the files after transfer by confirming checksum hashes (usually `MD5` checksums) match those provided by the sequencing facility. 

You should run [`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess sequencing quality. This might vary based on the details of your project but generally you can ID outliers and those samples with poor read quality. Presence of adapters can also be visualized.


## Trimming

Quality and adapter trimming is required prior to assembly. [`fastp`](https://github.com/OpenGene/fastp) is recommended due to its speed and FastQC-like report(s). Additionally, the output from [`fastp`](https://github.com/OpenGene/fastp) can also be analyzed by [`MultiQC`](https://multiqc.info/) (requires a "plug-in"). Trimmed files should be passed through `[`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) and assessed. Although rare, some projects may require a second round of trimming.

Alternatively, [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has trimming capabilities built in, using [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic). Although convenient, it limits the ability to assess post-trimming sequencing data prior to assembly.

## Assembly

[`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) is the _de facto_ standard. It is well-documented, well-supported, and actively updated. Additionally, the developer is very responsive, considerate, and helpful to [all GitHub Issues](https://github.com/trinityrnaseq/trinityrnaseq/issues).

[`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) is powerful and has complex, but useful options availalbe. Take time to consider how you will use your assembly for later analysis. [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has many options available for downstream analysis (e.g. [gene expression](#gene-expression)) that can be simplified with careful planning prior to assembly. It is recommended to create a sample list file for [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) to use. Here's the example from [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki). Sample file list is tab-delimited like this:

```
cond_A    cond_A_rep1    A_rep1_left.fq    A_rep1_right.fq
cond_A    cond_A_rep2    A_rep2_left.fq    A_rep2_right.fq
cond_B    cond_B_rep1    B_rep1_left.fq    B_rep1_right.fq
cond_B    cond_B_rep2    B_rep2_left.fq    B_rep2_right.fq
```

Due to the intensive processing required for assembly (high CPU and RAM usage), it is highly recommended to run all assemblies on an [execute node on Mox](https://robertslab.github.io/resources/mox_Node-Types/).

### _De novo_ assembly

A _de novo_ assembly is an assembly that is done without the use of a reference genome.


### Genome-guided assembly

A genome-guided assembly is an assembly which utilizes a reference genome.

## Gene expression

## Annotation