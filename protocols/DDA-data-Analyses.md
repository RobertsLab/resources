Guidelines for analysis of **data dependent** acquisition acquired mass spectra (or, shotgun proteomics). 

> Instructions are written for use on the Roberts Lab computer called Emu. Emu runs Linux (Ubuntu 16.04LTS).

---
### 1) Convert mass spec (MS) .raw files to .mzXML files for use in Comet


  - Requires wine (Windows emulator)
  - Requires [ReAdW](http://tools.proteomecenter.org/wiki/index.php?title=Software:ReAdW).    


Examples of code:    

```
WINEPREFIX=~/.wine32 ReAdW.2016010.msfilereader.exe \
20161205_Sample_1.raw \
20161205_Sample_1.mzXML	
```

```
for file in *.raw
    do
    no_path=${file##*/}
    no_ext=${no_path%.raw}
    WINEPREFIX=~/.wine32 ReAdW.2016010.msfilereader.exe "$file" "$no_ext".mzXML
    done
```

Explanation:

```for file in *.raw``` - Runs a for loop that looks for any ```.raw``` files in the current directory. Each file is stored in the variable called ```file```.

```no_path=${file##*/}``` - This removes the path from the current .raw file and stores just the filename in the variable called ```no_path```

```no_ext=${no_path%.raw}``` - This removes the ```.raw``` extension from the filename stored in the ```no_path``` variable. It saves this extension-less filename in a new variable called ```no_ext```.

```WINEPREFIX=~/.wine32 ReAdW.2016010.msfilereader.exe "$file" "$no_ext".mzXML``` - Calls the ```wine``` program to run the ```ReAdW``` program. Operates on the current file (```$file```), and writes the output to a new file using the value stored in the variable ```$no_ext``` and appends a new extension, ```.mzXML```

---

### 2) Search files against a protein sequence database using Comet. 

For this step you will need three items:

- A protein database for your target organism, [i.e. Crassostrea gigas proteome (contigs.fasta.transdecoder.pep) with the addition of three contaminant files ([contam.other](https://github.com/sr320/nb-2017/blob/master/C_gigas/data/contam.other.fa), [contam.human](https://github.com/sr320/nb-2017/blob/master/C_gigas/data/contam.human.fa), and [contam.bovin](https://github.com/sr320/nb-2017/blob/master/C_gigas/data/contam.bovin.fa).]

- .mzXML files in one directory (_excluding blanks and QCs_)

- A comet.params file.
Downloaded from this website. I chose the comet.params.high-low high res MS1 and low res MS2 e.g. Velos-Orbitrap.

All these files need to be in the same directory. Comet will produce pep.xml files for all your samples.

Examples code to conduct searches:
_Note: this step is multi-threaded_
```
/home/shared/comet/comet.2016012.linux.exe \
-Pcomet.params.high-low \
-Ddatabase_CgCont.fa \
20161205_Sample_1.mzXML
```

```
/home/shared/comet/comet.2016012.linux.exe \
-Pcomet.params.high-low_de \
-DCg-Giga_cont_AA.fa \
*.mzXML \
&>> output.error.comet.log
```

Notes: Make sure your parameters reflect the type of data you have and that the database path is correct. More details can be found on the UWPR website. It is good practice to include a decoy search.

A bit of what comet parameter file looks like:
```
# comet_version 2016.01 rev. 0
# Comet MS/MS search engine parameters file.
# Everything following the '#' symbol is treated as a comment.

database_name = /home/steven/bioinfo/021017b/Cg_Giga_cont_AA.fa
decoy_search = 1                       # 0=no (default), 1=concatenated search, 2=separate search

num_threads = 0                       # 0=poll CPU to set num threads; else specify num threads directly (max 64)

#
# masses
#
```

---
### 3) Calculate statistics associated with peptide and protein IDs using the Trans Proteomic Pipeline (Peptide and Protein Prophet). 
What you will need:

- TPP installed
- pep.xml search results from Comet

Notes: Commonly run TPP in the same directory as my Comet searches. You need to run it on each file individually, but each analysis is relatively fast. Common to use p-value cut-off for peptide probability of 0.9, but this can be changed depending on what you want. For each file, run: `xinteract -p0.9 -OAp -dDECOY_ -N[file name without pep.xml] file name.pep.xml`

[xinteract man page](https://gist.github.com/sr320/39f620271896a380f87086d4b61aabd8)

Examples:    
```
/usr/tpp_install/tpp/bin/xinteract \
-dDECOY_ \
-N20161205_Sample_1 \
20161205_Sample_1.pep.xml \
-p0.9 \
-OAp
```

```
find *xml | \
xargs basename -s .pep.xml | \
xargs -I {} /usr/tpp_install/tpp/bin/xinteract \
-dDECOY_ \
-N{} \
{}.pep.xml \
-p0.9 \
-OAp \
&>> output.error.xin.log
```

---

### 4) [ABACUS](http://onlinelibrary.wiley.com/doi/10.1002/pmic.201000650/abstract) will correlate protein inferences across your sample files so that a single protein will be associated with each peptide.

The output will be a compiled single .tsv file with corresponding spectral counts and normalized spectral abundance factor (NSAF) which is a proxy for protein abundance.


You will need:

- [ABACUS installed](https://sourceforge.net/projects/abacustpp/files/)

- interact -....pep.xml files from TPP

- An Abacus parameters file

Example usage be found on the [UWPR tools page](http://proteomicsresource.washington.edu/protocols06/Abacus/) (note: the usage is specific to UWPR and may not be directly applicable to our usage). You can change the output format so that the file is formatted for use in Qspec (the subsequent step). To do this, change this line in the Abacus parameters file:
```output=Default``` to ```output=ProtQspec``` (per the [Abacus Google Group thread](https://groups.google.com/forum/#!topic/abacus-support/-KbwDlRA284)).
Once ABACUS runs, you will have a .tsv file with all your files joined together and corresponding spectral counts and normalized spectral abundance factor (NSAF), which will be your proxy for protein abundance.



Example:     

```
/usr/tpp_install/tpp/bin/ProteinProphet \
interact*.pep.xml \
interact-COMBINED.prot.xml \
&>> output.error.PP.log
```

Make Abacus parameter file, then

`java -Xmx16g -jar /home/shared/abacus/abacus.jar -p ~/Documents/rhonda/Abacus_parameters.txt`

or

```
java -Xmx16g -jar /home/shared/abacus/abacus.jar -p \
Abacus.params
```

`head` of example abacus parameter file:

```
#
# ABACUS parameter file
# Generated on: 2017Feb07_1919
#

# Name to give the database
dbName=ABACUSDB

# Name of protXML file corresponding to merged/combined results
combinedFile=/home/steven/bioinfo/021217/interact-COMBINED.prot.xml

# The directory that contains the pepXML and protXML files
srcDir=/home/steven/bioinfo/021217

# The name of the file where results will be saved to
outputFile=/home/steven/bioinfo/021217/ABACUS_output.tsv

```

**Following ABACUS there are two directions that data should be examined. First is considering all the data in analysis such as NMDS, heat maps, Excel etc. Similarly NMDS should be used to confirm technical replicates are tight.**

### 5) NMDS 

Technical replicates should be examined. Example _might_ be available using [this R code](https://github.com/sr320/supp-geoduck-proteomics/blob/master/R-code/geoduck-gonad-nmds.R) see line 68. Original table [here](https://github.com/sr320/supp-geoduck-proteomics/blob/master/data/Detected-geoduck-proteins.csv). For NMDS, heat maps, etc: the `ADJNSAF` data column should be used. 

### 6) Qspec 

Qspec compares two treatment. For qpsec use the `NUMSPECSTOT` column from Abacus. Input files need to be in .txt file format. This program finds differentially abundant proteins by giving you a log fold change and z-statistic for each protein. A protein is generally considered significant if it has a log fold change of at least absolute value of 0.5 and a z-stat of at least absolute value of 2.


