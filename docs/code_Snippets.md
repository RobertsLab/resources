A few useful code chunks.

## Shell Basics




## File Transfers


`gdown -O PGA_assembly.fasta https://drive.google.com/uc?id=1Yanmb5yBXn-D4b_fzkR2GSxP`




## Fasta





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
