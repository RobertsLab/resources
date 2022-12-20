Introductory guide to transcriptome assembly using [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) and short-read sequencing data.

## QC
A normal starting point would be having raw sequence data provided by a core facility. When downloading said data you need to make sure you check the integrity of the files after transfer by confirming checksum hashes (usually `MD5` checksums) match those provided by the sequencing facility. 

You should run [`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess sequencing quality. This might vary based on the details of your project but generally you can ID outliers and those samples with poor read quality. Presence of adapters can also be visualized.


## Trimming
Quality and adapter trimming is required prior to assembly. [`fastp`](https://github.com/OpenGene/fastp) is recommended due to its speed and FastQC-like report(s). Additionally, the output from [`fastp`](https://github.com/OpenGene/fastp) can also be analyzed by [`MultiQC`](https://multiqc.info/) (requires a "plug-in"). Trimmed files should be passed through `[`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) and assessed. Although rare, some projects may require a second round of trimming.

Alternatively, [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki) has trimming capabilities built in, using [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic). Although convenient, it limits the ability to assess post-trimming sequencing data prior to assembly.