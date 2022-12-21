
# Annotation

## Intro (Blast)
Blast is a key component of working with lesser studied taxa. Here are some resources to help with this.

**First off, you should be familar with the command line interface and bash**

- [Introducing the Shell](http://swcarpentry.github.io/shell-novice/01-intro/)
- [Introduction to the Command Line for Genomics](https://datacarpentry.org/shell-genomics/)
- <https://explainshell.com/>

---


### Blast Notebooks

- <https://github.com/RobertsLab/code/blob/master/09-blast.ipynb> - An example of how one might take a multi sequence fasta file and using NCBI Blast, compare the sequences with the Swiss-Prot Database on their own computer.

- <https://github.com/RobertsLab/code/blob/master/10-blast-2-slim.ipynb> - A notebook to seamlessly take blast output to GO Slim list

- <https://github.com/RobertsLab/code/blob/master/script-box/complete_go_annotation_notebook.Rmd> -

- https://github.com/sr320/ceabigr/blob/main/code/17-Swiss-Prot-Annotation.Rmd -  Blasting C virginica to Swiss-Prot. Author: Steven Roberts ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/ceabigr)

## Genome features
In addition to sequence database alignment, finding spatial relationship within a genome is also an import approach for annotation. Often this is done using software tools such as `bedtools`.

### `bedtools::intersectbed`
see also https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html

## Transcriptome (Trinity)

After [transcriptome assembly using Trinity](https://robertslab.github.io/resources/bio_Transcriptome-assembly/)

- Transdecoder

- longest Open Reading Frames

- BLASTp

- pFam

- Trinotate
