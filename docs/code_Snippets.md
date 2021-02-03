A few useful code chunks.

## Shell Basics




## File Transfers


```
gdown -O PGA_assembly.fasta https://drive.google.com/uc?id=1Yanmb5yBXn-D4b_fzkR2GSxP
```




## Fasta

- fasta to tab-delimited

```
!perl -e '$count=0; $len=0; while(<>) {s/\r?\n//; s/\t/ /g; if (s/^>//) { if ($. != 1) {print "\n"} s/ |$/\t/; $count++; $_ .= "\t";} else {s/ //g; $len += length($_)} print $_;} print "\n"; warn "\nConverted $count FASTA records in $. lines to tabular format\nTotal sequence length: $len\n\n";' \
../data/GCF_000297895.1_oyster_v9_cds_from_genomic.fna > ../analyses/GCF_000297895.1_oyster_v9_cds_from_genomic.tab
```



##  Blast

```
Applications/bioinfo/ncbi-blast-2.11.0+/bin/blastx \
-query ../data/GCF_000297895.1_oyster_v9_cds_from_genomic.fna \
-db ../blastdb/Caenorhabditis_elegans.WBcel235.pep  \
-out ../analyses/Cg-WBcel235_blastx.tab \
-evalue 1E-05 \
-num_threads s \
-max_target_seqs 1 \
-max_hsps 1 \
-outfmt "6 qaccver saccver evalue"
```
