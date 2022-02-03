
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
