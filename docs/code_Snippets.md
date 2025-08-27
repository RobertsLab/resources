A few useful code chunks.

## Shell Basics

Most commands are for bash (shell) scripts.

Also, assumes usage of bash >=4.0.

---


## R Markdown

### Use Bash variables across chunks

Variables are saved to a “dot file” and that file needs to be sourced in each Bash chunk to have access to the Bash variables across Bash chunks.

The Bash variables set in the example below are:

- `${threads}`

- `${my_fasta}`

- `${samtools}`

```R
{bash save-bash-variables-to-rvars-file}
# Send text to export Bash variables to .rvars file
{
echo "# CPU threads"
echo 'export threads=8'
echo ""
echo "# Programs"
echo 'export my_fasta="~/data/temporary.fasta"'
echo 'export samtools="~/programs/samtools-1.12/samtools"'
echo ""
} > .rvars
```

In subsequent Bash chunks, load the variables into memory to use them:

```R
{bash load-bash-variables}
# Load contents of .rvars into memory so varaibles are accessible
source .rvars

# Create FastA index file
"${samtools} faidx "${my_fasta}"
```

---

## Git

### Add files >100MB to .gitignore file

`find ./* -size +100M | cat >> .gitignore`

Run this from top directory of your repo.

This finds all files in your current directory (presumably a Git repo) greater than 100MB and writes the paths to those files in your .gitignore file. 

### Fix "refusing to merge unrelated histories" error

This error occurs when your local repository and the remote repository have diverged with completely different commit histories. This commonly happens when:

- Someone force-pushed to the remote repository, rewriting history
- The remote repository was reset or recreated
- You're trying to merge two repositories that were created independently

#### Solution 1: Allow unrelated histories (Recommended)

```bash
git pull origin main --allow-unrelated-histories
```

After running this command, Git will attempt to merge the unrelated histories. You may need to resolve merge conflicts manually.

#### Solution 2: Create backup and re-clone (Safest)

If you have uncommitted local changes you want to keep:

```bash
# Create a backup of your local changes
cp -r your_repo your_repo_backup

# Remove the problematic repository
rm -rf your_repo

# Re-clone the repository
git clone https://github.com/username/repository.git your_repo

# Copy back any local files you need from the backup
# (Be careful not to overwrite files that should come from the remote)
```

#### Solution 3: Force pull (Use with caution)

**Warning**: This will overwrite your local changes permanently.

```bash
# Fetch the latest changes
git fetch origin

# Reset your local branch to match the remote
git reset --hard origin/main
```

#### Solution 4: Manual merge resolution

If you need to preserve both local and remote changes:

```bash
# Create a new branch from your current state
git checkout -b backup-local-changes

# Switch back to main
git checkout main

# Force update to match remote
git fetch origin
git reset --hard origin/main

# Merge your local changes back
git merge backup-local-changes --allow-unrelated-histories
```

#### Prevention

To avoid this issue in the future:
- Always pull before making changes: `git pull origin main`
- Use `git status` regularly to check your repository state
- Avoid force-pushing unless absolutely necessary
- Communicate with team members before making major repository changes

---

## FastQ files

### Create separate arrays for R1 and R2 reads

- With a for loop
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

- Using "globbing"
  ```shell
  # Declare arrays
  R1_array=()
  R2_array=()

  # Populate arrays
  R1_array=(*R1.fq)
  R2_array=(*R2.fq)
  ```

  - Create comma-separated lists of FastQ reads

      (E.g. This is useful when running [`bowtie2`](https://github.com/BenLangmead/bowtie2) or [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki))

      ```shell
      R1_list=$(echo "${R1_array[@]}" | tr " " ",")
      R2_list=$(echo "${R2_array[@]}" | tr " " ",")
      ```

### Creating single array with paired reads

```shell
## Assumes there is only a single set of paired reads per sample

# Declare array
fastq_array=()

# Populate array
# Corresponding reads will be placed next to each other in array
# (e.g. sample01_R1.fq sample01_R2.fq sample02_R1.fq samples02_R2.fq)
fastq_array=(*.fq)
```

- Loop through single array of paired reads

    ```shell
    ## Assumes there is only a single set of paired reads per sample

    # Declare array
    fastq_array=()

    # Populate array
    fastq_array=(*.fq)

    # Loop through read pairs
    # Increment by 2 to process next pair of FastQ files
    for (( i=0; i<${#fastq_array[@]} ; i+=2 ))
      do
      echo "Read 1: ${fastq_array[i]}"
      echo "Read 2: ${fastq_array[i+1]}"
    done
    ```

- Create comma-separated lists of paired FastQ reads

    (E.g This is useful when running [`bowtie2`](https://github.com/BenLangmead/bowtie2) or [`Trinity`](https://github.com/trinityrnaseq/trinityrnaseq/wiki))

    ```shell
    # Create comma-separated lists of FastQ reads
    # Loop through read pairs
    # Increment by 2 to process next pair of FastQ files
    for (( i=0; i<${#fastq_array[@]} ; i+=2 ))
    do
      # Check array length for even number (i.e. paire end FastQs)
      if [[ $(( "${#fastq_array[@]}" % 2 )) -ne 0 ]]; then
        echo "FastQ array contains uneven number of files."
        exit
      fi

      # Handle "fence post" problem
      # associated with comma placement
      if [[ ${i} -eq 0 ]]; then
        R1_list="${fastq_array[${i}]},"
        R2_list="${fastq_array[${i}+1]},"

      elif [[ ${i} -eq $(( ${#fastq_array[@]} - 1 )) ]]; then
        R1_list="${R1_list}${fastq_array[${i}]}"
        R2_list="${R2_list}${fastq_array[${i}+1]}"

      else
        R1_list="${R1_list}${fastq_array[${i}]},"
        R2_list="${R2_list}${fastq_array[${i}+1]},"
      fi
    done
    ```

---

## File Transfers

### Backing up Mox files 

```
/volume2/web/seashell/bu-mox$ 
rsync -avz --exclude '*_to_*' --exclude 'CHG_*.txt' --exclude 'CHH_*.txt' --exclude 'CpG_*txt' \
--progress sr320@mox.hyak.uw.edu:/gscratch/scrubbed/sr320/ scrubbed/



/volume2/web/seashell/bu-mox$ 
rsync -avz --progress sr320@mox.hyak.uw.edu:/gscratch/srlab/sr320/ .
```


### Backing up Raven files 
```
/home/shared/8TB_HDD_01/sr320/github$ 
rsync -avz . \
sr320@gannet.fish.washington.edu:/volume2/web/seashell/bu-github/
```


### wget a lot of files from url 

```
wget -r \
--no-directories --no-parent \
-P . \
-A "*_001_val_1.fq.gz" https://gannet.fish.washington.edu/metacarcinus/Salmo_Calig/analyses/20190806_TrimGalore/
```

### git clone website

_when in public_html_

```
mkdir temp
cd temp
git clone https://github.com/sr320/lab-website.git
cd ..
cp -r temp/lab-website/docs/* .
rm -f -r temp
echo "now done"
```



### Transfer sequencing files to Owl

#### Standard `rsync` procedure:

```shell
rsync --archive --progress --verbose *.fastq.gz <owl_username>@owl.fish.washington.edu:/volume1/web/nightingales/<species_directory>
```

- Replace `<owl_username_>` with whatever username you use to login to owl (even replace the `<` and the `>`).

- Replace `<species_directory>` with whatever species you're working with  (even replace the `<` and the `>`). Example directory name format: `P_generosa`.

- If it doesn't work, Sam may need to change your user settings on Owl, so please post an issue in [https://github.com/RobertsLab/resources/issues/](https://github.com/RobertsLab/resources/issues/)

#### Using `rsync` list of files:

```shell
rsync -avP --files-from=:/volume1/web/nightingales/P_generosa/rsync_list.txt owl:/volume1/web/ .
```

```shell
head rsync_list.txt

nightingales/P_generosa/Geoduck-ctenidia-RNA-1_S3_L001_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-ctenidia-RNA-2_S11_L002_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-ctenidia-RNA-3_S19_L003_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-ctenidia-RNA-4_S27_L004_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-ctenidia-RNA-5_S35_L005_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-ctenidia-RNA-6_S43_L006_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-ctenidia-RNA-7_S51_L007_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-ctenidia-RNA-8_S59_L008_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-gonad-RNA-1_S1_L001_R2_001.fastq.gz
nightingales/P_generosa/Geoduck-gonad-RNA-2_S9_L002_R2_001.fastq.gz
```

### Confirm MD5 checksums

#### Multiple MD5 checksum files (Linux)

```shell
for checksum_file in *.md5
do
  md5sum --check ${checksum_file}
done
```

#### Multiple MD5 checksum files (Mac OS)

```shell
for checksum_file in *.md5
do
  # Gets filename without any suffixes
  filename=$(basename -s .md5 ${checksum_file})
  # Generates MD5 checksum and compares to provided checksum in MD5 file
  diff <(md5 "${filename}.fastq.gz" | awk '{print $4}') <(awk '  {print $1}' ${checksum_file})
done
```

### Download file from Google Drive

Install [`gdown`](https://github.com/wkentaro/gdown).

Ideally, a checksum for the file hosted on Google Drive exists and be can be
subsequently verified after downloading.

```
gdown -O PGA_assembly.fasta https://drive.google.com/uc?id=1Yanmb5yBXn-D4b_fzkR2GSxP
```

### Transfer files to/from Mox using Globus Connect Personal

1. Log into Mox.

2. Activate anaconda (this might fail, let me know if it does and don't bother going to the next step): `conda activate`

3. Setup Globus collection: `/gscratch/srlab/programs/globusconnectpersonal-3.1.4/globusconnectpersonal -setup --no-gui`

4. Follow the instructions (copy/paste URL into browser, get code from webpage, enter code in Mox terminal, provide name for collection).

5. Add desired Mox directory to config file and set permissions. Here's an example:

```
$cat ~/.globusonline/lta/config-paths

~/,0,1
/gscratch/scrubbed/samwhite/,0,1
```

The config file does two things:

-  `~/,0,1`: Makes your home directory readable/writeable by Globus.
-  `/gscratch/scrubbed/samwhite/,0,1`: Makes my directory on `/gscratch/scrubbed/` readable/writeable by Globus.

6. Start Globus Connect Personal: `/gscratch/srlab/programs/globusconnectpersonal-3.1.4/globusconnectpersonal -start`. Nothing will happen after you hit enter. The cursor will simply flash - this is good.

7. Login to your Globus Connect Personal account via a web browser.

8. Click on Collections and you should now see your collection (name provided in Step 4), and it should have a green stack of papers(?) next to it; the green indicates that the connection is activate.

9. Click on the collection name.

10. Click on "Open in File Manager" (on the right side of the screen).

11. Navigate to the directory you setup in Step 5. NOTE: You'll have to navigate up a directory out of your home directory in order to get to the `/gscratch` partition.

12. Transfer data from other Globus Endpoint to Mox!

---

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

---

## [`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

### Pass space-delimited list of FastQ files to FastQC

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


## [`BLAST`](https://www.ncbi.nlm.nih.gov/books/NBK279690/)

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

## Tips & Tricks

###  Remove spaces from filenames in a directory

 ```bash
 for file in *; do mv "$file" ${file// /}; done
 ```

Explanation:

- `for file in *;`

  - A for loop that looks at all files in the current directory. The word ```file``` is a variable that takes on the value of each file name in the directory (one file name per loop). The ```;``` is needed for bash for loop formatting.

- `do mv "$file" ${file// /};`

  - Tells bash to use the move command (`mv`) and use the current contents of the variable `$file` as the initial filename. The `${file// /}` is a substitution command that tells bash to use the contents of the `file` variable and replace all spaces (`//` ; note - there should be a space after the last slash here) with nothing (`/` - you can add text after this slash to replace with information of your choice). The `;` is needed for bash for loop formatting.

- `done`
  - Ends the for loop
