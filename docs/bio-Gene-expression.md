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


## alignment: HiSat



---

## DESeq2

See also the official documentation.

User Guides
- [Analyzing RNA-seq data with DESeq2](http://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)


### Use cases from our lab
- <https://github.com/laurahspencer/O.lurida_QuantSeq-2020/blob/master/notebooks/02-Adult-data-analysis-QuantSeq2020.Rmd> - draft code analyzing QuantSeq data from Olympia oyster gill tissue by two factors (population, pCO2 treatment). See [2020-QuantSeq-Processing_Raw-to-Counts.ipynb](https://github.com/laurahspencer/O.lurida_QuantSeq-2020/blob/master/notebooks/2020-QuantSeq-Processing_Raw-to-Counts.ipynb) and [01-Importing-data-QuantSeq2020.Rmd](0https://github.com/laurahspencer/O.lurida_QuantSeq-2020/blob/master/notebooks/01-Importing-data-QuantSeq2020.Rmd) for steps prior to DeSeq2. Author: Laura Spencer  ![GitHub last commit](https://img.shields.io/github/last-commit/laurahspencer/O.lurida_QuantSeq-2020)

- <https://github.com/RobertsLab/paper-tanner-crab/blob/master/scripts/DESeq.Rmd> ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/paper-tanner-crab)
