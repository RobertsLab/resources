
## Bismark

See also the official documentation.

User Guides

1) <http://felixkrueger.github.io/Bismark/Docs/>       
2) <https://www.bioinformatics.babraham.ac.uk/projects/bismark/>


### Use cases from our lab

<https://github.com/RobertsLab/code/blob/master/20-bismark.sh>

- <https://github.com/sr320/paper-oly-mbdbs-gen/blob/master/code/00-Bismark.sh>  -  used to processes BS-MBDSeq Data from Olympia oysters, run on Mox. Author: Steven Roberts ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/paper-oly-mbdbs-gen)

- <https://raw.githubusercontent.com/laurahspencer/C.magister_methyl-oa/master/scripts/20201214_Cmag_bismark-align.sh> - slurm script used to process MiSeq data from Dungeness crab, run on Mox. [Here is a Jupyter Notebook](https://github.com/laurahspencer/C.magister_methyl-oa/blob/master/notebooks/MBD-01%20Processing%20QC%20MiSeq%20data.ipynb) with more details/narrative. Author: Laura Spencer, but derived from the [MethCompare workflow](https://github.com/hputnam/Meth_Compare). ![GitHub last commit](https://img.shields.io/github/last-commit/laurahspencer/C.magister_methyl-oa)

- <https://github.com/sr320/paper-oly-wgbs/blob/master/submission/Narrative.Rmd> part of Rmd narrative, used for WGBS Olympia oyster data. Author: Steven Roberts ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/paper-oly-wgbs)

- <https://github.com/hputnam/Geoduck_Meth/blob/master/code/03-bismark.sh> geoduck environmental memory project. Run on Mox. Author: Steven Roberts ![GitHub last commit](https://img.shields.io/github/last-commit/hputnam/Geoduck_Meth)

- <https://raw.githubusercontent.com/epigeneticstoocean/paper-gonad-meth/master/code/02-bismark.sh> eastern oyster data, run on Mox ![GitHub last commit](https://img.shields.io/github/last-commit/epigeneticstoocean/paper-gonad-meth)

- <https://github.com/hputnam/Meth_Compare/blob/master/code/00.01-DNA-sequence-processing.md> Complete DNA processing protocol from comparison of BS methods on corals. ![GitHub last commit](https://img.shields.io/github/last-commit/hputnam/Meth_Compare)



### Diagram




### Code Output Expectations
(**Always default to the Manual/User Guide!** - this is merely an attempt at explaining our workflow)

## Bismark

[Bismark User Guide](https://rawgit.com/FelixKrueger/Bismark/master/Docs/Bismark_User_Guide.htm)


**(I) Running bismark_genome_preparation**

USAGE:
bismark_genome_preparation [options] <path_to_genome_folder>
```
${bismark_dir}/bismark_genome_preparation \
--verbose \
--parallel 28 \
--path_to_aligner ${bowtie2_dir} \
${genome_folder}
```

You should expect to prepared genome with directory structure similar to
```
./roslin_M/Bisulfite_Genome
./roslin_M/Bisulfite_Genome/GA_conversion
./roslin_M/Bisulfite_Genome/CT_conversion
```

**(II) Running bismark**

USAGE:
bismark [options] --genome <genome_folder> {-1 <mates1> -2 <mates2> | <singles>}

```
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

This will create bam files (sequence alignment files)

**(III) Running deduplicate_bismark**


deduplicate_bismark --bam [options] <filenames>

This command will deduplicate the Bismark alignment BAM file and remove all reads but one which align to the the very same position and in the same orientation. This step is recommended for whole-genome bisulfite samples, but should not be used for reduced representation libraries such as RRBS, amplicon or target enrichment libraries.

```
find *.bam | \
xargs basename -s .bam | \
xargs -I{} ${bismark_dir}/deduplicate_bismark \
--bam \
--paired \
{}.bam
```

This will create a deduplicated bam file.

**(IV) Running bismark_methylation_extractor**

USAGE:
bismark_methylation_extractor [options] <filenames>

```
${bismark_dir}/bismark_methylation_extractor \
--bedGraph --counts --scaffolds \
--multicore 14 \
--buffer_size 75% \
*deduplicated.bam
```

```
# ${bismark_dir}/bismark_methylation_extractor \
# --bedGraph \
# --counts \
# --comprehensive \
# --merge_non_CpG \
# --multicore 28 \
# --buffer_size 75% \
# *deduplicated.bam
```

This will create deduplicated.bismark.cov.gz, uncompressed is in this format. Not we are using `--bedGraph` output, this is not default.

> Alternatively, the output of the methylation extractor can be transformed into a bedGraph and coverage file using the option --bedGraph (see also --counts)... Optionally, the bedGraph counts output can be used to generate a genome-wide cytosine report which reports the number on every single CpG (optionally every single cytosine) in the genome, irrespective of whether it was covered by any reads or not. As this type of report is informative for cytosines on both strands the output may be fairly large.

```
NC_035784.1	141	141	37.5	3	5
NC_035784.1	142	142	100	2	0
NC_035784.1	155	155	70	7	3
NC_035784.1	156	156	100	2	0
NC_035784.1	291	291	0	0	2
NC_035784.1	292	292	0	0	3
NC_035784.1	313	313	0	0	1
NC_035784.1	314	314	66.6666666666667	2	1
NC_035784.1	470	470	66.6666666666667	4	2
NC_035784.1	611	611	0	0	4
```

`<chromosome> <start position> <end position> <methylation percentage> <count methylated> <count unmethylated>`



**genome-wide cytosine report output**

>Starting from the coverage output, the Bismark methylation extractor can optionally also output a genome-wide cytosine methylation report. The module coverage2cytosine (part of the Bismark package) may also be run individually. It is also sorted by chromosomal coordinates but also contains the sequence context and is in the following format:
<chromosome> <position> <strand> <count methylated> <count unmethylated> <C-context> <trinucleotide context>

>The main difference to the bedGraph or coverage output is that every cytosine on both the top and bottom strands will be considered irrespective of whether they were actually covered by any reads in the experiment or not. For this to work one has to also specify the genome that was used for the Bismark alignments using the option --genome_folder <path>. As for the bedGraph mode, this will only consider cytosines in CpG context by default but can be extended to cytosines in any sequence context by using the option --CX (cf. Appendix (III)). Be aware though that this might mean an output with individual lines for more than 1.1 billion cytosines for any large mammalian genome...

```
find *deduplicated.bismark.cov.gz \
| xargs basename -s _trimmed_bismark_bt2.deduplicated.bismark.cov.gz \
| xargs -I{} ${bismark_dir}/coverage2cytosine \
--genome_folder ${genome_folder} \
-o {} \
--merge_CpG \
--zero_based \
{}_trimmed_bismark_bt2.deduplicated.bismark.cov.gz
```

generates a file `.CpG_report.merged_CpG_evidence.cov`



```
NC_035785.1	217	219	100.000000	17	0
NC_035785.1	523	525	87.500000	7	1
NC_035785.1	556	558	50.000000	5	5
NC_035785.1	727	729	100.000000	16	0
NC_035785.1	1330	1332	0.000000	0	2
NC_035785.1	1403	1405	0.000000	0	2
NC_035785.1	1494	1496	66.666667	2	1
NC_035785.1	1747	1749	100.000000	8	0
NC_035785.1	2024	2026	100.000000	24	0
NC_035785.1	2054	2056	93.333333	14	1
```



**(V) Running bismark2report**

USAGE:
bismark2report [options]

```
${bismark_dir}/bismark2report
```

**(VI) Running bismark2summary**

USAGE:
bismark2summary [options]

Produces report like [this](https://www.bioinformatics.babraham.ac.uk/projects/bismark/PE_report.html)


```
${bismark_dir}/bismark2summary
```

Produces report like [this](https://www.bioinformatics.babraham.ac.uk/projects/bismark/bismark_summary_report.html)

---
  
## BS-Snpr
See https://github.com/hellbelly/BS-Snper

### Use cases from our lab
  
- <https://nbviewer.org/github/RobertsLab/project-gigas-oa-meth/blob/master/code/07-BS-SNPer.ipynb> - Pacific oyster exposed to OA. Author: Yaamini Venkataraman ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/project-gigas-oa-meth)

---

## Methylkit

See also the official documentation - [MethylKit Vignette](https://bioconductor.org/packages/release/bioc/vignettes/methylKit/inst/doc/methylKit.html)


### Use cases from our lab

- <https://github.com/sr320/paper-oly-mbdbs-gen/blob/master/code/01-methylkit.Rmd> - used to processes BS-MBDSeq Data from Olympia oysters, run on personal computer (not Mox). Author: Laura Spencer ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/paper-oly-mbdbs-gen)

- <https://github.com/hputnam/Meth_Compare/blob/master/code/MethCompare_methylKit_analysis.R> coral methylation comparison of methods. ![GitHub last commit](https://img.shields.io/github/last-commit/hputnam/Meth_Compare)

- <https://github.com/epigeneticstoocean/paper-gonad-meth/blob/master/code/04-methylkit.Rmd> eastern oyster OA work ![GitHub last commit](https://img.shields.io/github/last-commit/epigeneticstoocean/paper-gonad-meth)

### Diagram

![image](https://user-images.githubusercontent.com/17264765/131020085-f32e8a51-9a29-474c-aa56-2fa599e006d9.png)
_Flowchart of possible operations by methylKit. A summary of the most importantmethylKit features is shown in a flow chart. It depicts the main features of methylKitand the sequential relationship between them. The functions that could be used for thosefeatures are also printed in the boxes._ - Figure and caption from [Akalin et al. 2012](https://doi.org/10.1186/gb-2012-13-10-r87)
