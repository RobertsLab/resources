A few useful code chunks.

## Shell Basics

Most commands are for bash (shell) scripts.

Also, assumes usage of bash >=4.0.

---

### Handling paired end FastQ files

- Create separate arrays for R1 and R2 reads

    With a for loop
    ```shell
    # Declare arrays
    R1_array=()
    R2_array=()

    # Populate arrays
    for fastq in *R1.fq
    do
      R1_array+=(${fastq})
    done

    for fastq in *R2.fq
    do
      R2_array+=(${fastq})
    done
    ```

    Using "globbing"
    ```shell
    # Declare arrays
    R1_array=()
    R2_array=()

    # Populate arrays
    R1_array=(*R1.fq)
    R2_array=(*R2.fq)
    ```

- Creating single array with paired reads

    ```shell
    ## Assumes there is only a single set of paired reads per sample

    # Declare array
    reads_array=()

    # Populate array
    # Corresponding reads will be placed next to each other in array
    # (e.g. sample01_R1.fq sample01_R2.fq sample02_R1.fq samples02_R2.fq)
    reads_array=(*.fq)
    ```

- Loop through single array of paired reads

    ```shell
    ## Assumes there is only a single set of paired reads per sample

    # Declare array
    reads_array=()

    # Populate array
    reads_array=(*.fq)

    # Loop through read pairs
    # Increment by 2 to process next pair of FastQ files
    for (( i=0; i<${#reads_array[@]} ; i+=2 ))
      do
      echo "Read 1: ${reads_array[i]}"
      echo "Read 2: ${reads_array[i+1]}"
    done
    ```


## File Transfers


```
wget -r \
--no-directories --no-parent \
-P . \
-A _001_val_1.fq.gz https://gannet.fish.washington.edu/metacarcinus/Salmo_Calig/analyses/20190806_TrimGalore/
```

```
gdown -O PGA_assembly.fasta https://drive.google.com/uc?id=1Yanmb5yBXn-D4b_fzkR2GSxP
```




## FastA

###  Filter FastA File by Minimum Sequence Length
 Just change the number "200" in the code below to your desired minimum sequence length.

 ```bash
 $ awk '!/^>/ { next } { getline seq } length(seq) >= 200 { print $0 "\n" seq }' InputFastaFile.fasta
 ```

 Code explanation:

 `!/^>/ { next }`:

 - If a line (i.e. record) begins with a “>”, go to the next line (record). The "!" tells awk to skip the regular expression that immediatley follows. The "^" tells awk that the regular expression it's looking for should only match if it's at the beginning of a line. Finally, the regular expression we're looking for in this example is the ">", which denotes the sequence descriptor portion of FASTA files.

`{ getline seq } `:

 - “getline” reads the next record and assigns the entire record to a variable called “seq”

` length(seq) >=200`:

- If the length of the “seq” record is greater than, or equal to, 200 then…

`{print $0 "\n" seq>}`:

 - Print all records (`$0`) of the variable “seq” in the file that matched our conditions, each on a new line (“\n”)

### fasta to tab-delimited

```
!perl -e '$count=0; $len=0; while(<>) {s/\r?\n//; s/\t/ /g; if (s/^>//) { if ($. != 1) {print "\n"} s/ |$/\t/; $count++; $_ .= "\t";} else {s/ //g; $len += length($_)} print $_;} print "\n"; warn "\nConverted $count FASTA records in $. lines to tabular format\nTotal sequence length: $len\n\n";' \
../data/GCF_000297895.1_oyster_v9_cds_from_genomic.fna > ../analyses/GCF_000297895.1_oyster_v9_cds_from_genomic.tab
```

## FastQC

Pass space-delimited list of FastQ files to FastQC
```shell
# Set CPU threads to use
threads=20

# Populate array with FastQ files
fastq_array=(*.fq.gz)

# Pass array contents to new variable
fastqc_list=$(echo "${fastq_array[*]}")

# Run FastQC
# NOTE: Do NOT quote ${fastqc_list}
fastqc \
--threads ${threads} \
--outdir ${output_dir} \
${fastqc_list}
```


##  Blast

```
Applications/bioinfo/ncbi-blast-2.11.0+/bin/blastx \
-query ../data/GCF_000297895.1_oyster_v9_cds_from_genomic.fna \
-db ../blastdb/Caenorhabditis_elegans.WBcel235.pep  \
-out ../analyses/Cg-WBcel235_blastx.tab \
-evalue 1E-05 \
-num_threads 4 \
-max_target_seqs 1 \
-max_hsps 1 \
-outfmt "6 qaccver saccver evalue"
```
