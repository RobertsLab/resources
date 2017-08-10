# DIA Analyses

Data-Independent Mass Spectrometry is a bottom-up proteomics method that separately gathers MS/MS spectra and MS survey spectra. The following workflow describes how to analyze DIA data.

### **Basic overview of the DIA pipeline**:

1) Demultiplex raw data files using MSConvert if data were collected with overlapping windows.

2) Use PECAN to create a peptide spectral library from data 

3) Get peptide and protein abundance information from Skyline 

This wiki is based partly on the following [Evernote entry](https://www.evernote.com/shard/s347/sh/edcb06ab-d008-418f-b28f-52f6614f1c39/2984ab55f427fcfe). 

Note: this might be a little less intuitive than the [DDA pipeline](https://github.com/sr320/LabDocs/wiki/DDA-data-Analyses). Additionally, the pipeline relies on Windows-based programs.

---
## Step 1. Convert Raw files with MSConvert
Output files from a mass spectrometer are in the `.raw` format, but PECAN requires demultiplexed `.mzML` files. [MSConvert](http://proteowizard.sourceforge.net/tools.shtml) is a GUI used to generate these files with the appropriate centroid peaks using 64-bit and zlib compression. However, demultiplexing has not been incorporated into the GUI so if you are demultiplexing you must use command line.

Below are the settings required for MSConvert in the GUI, followed by the same settings for demultiplexing in the command line:

![MSConvert-settings](https://raw.githubusercontent.com/sr320/LabDocs/master/img/MSConvert-settings.png)

Note that these setting [might vary](https://github.com/sr320/LabDocs/issues/486) based on version.

msconvert.exe --zlib --64 --mzML --filter "peakPicking true 1-2" --filter "demultiplex optimization=overlap_only" *.raw 

After the `.raw` files are converted to demultiplexed `.mzML` files, upload the mzML files to the desired location. This information will be used to generate the mzML file path list, an input for the `pecanpie` command used later on.

---

## Step 2. Prepare Peptide Database
This is done be identifying "reference proteome" and performing in silico digestion. 

### Step 2a. Merge reference proteome with Quality Standards.
Essentially concatenate the fasta files. Here is an example of a reference proteome- [C. gigas proteome](http://owl.fish.washington.edu/halfshell/bu-git-repos/nb-2017/C_gigas/data/Cg_Gigaton_proteins.fa). A tabular version of the QC peptide list for the January 2017 Lumos run can be found [here](http://owl.fish.washington.edu/generosa/Generosa_DNR/Pierce_PRTC.tabular).

### Step 2b. Run in silico tryptic digestion of reference proteome with quality standards.
This is done with [Protein Digestion Simulator](https://omics.pnl.gov/software/protein-digestion-simulator), a Windows program.

Settings for the in silico tryptic digest, as discussed on [Issue #483](https://github.com/sr320/LabDocs/issues/483). Each screenshot refers to a different tab in the program window. The screenshots are sequential (Tab #1-Tab #4).

Ensure the output, a digested reference proteome, is in a .tabular format.

![PDS tab 1](https://github.com/RobertsLab/Paper-DNR-Proteomics/blob/master/images/2017-02-19_final-Digest-Settings1.png?raw=true)

*Note: "Delimited Input File Options" depends on the format of your fasta file. This one only has protein ID and sequence.*

![PDS tab 2](https://github.com/RobertsLab/Paper-DNR-Proteomics/blob/master/images/2017-02-19_final-Digest-Settings2.png?raw=true)

![PDS tab 3](https://github.com/RobertsLab/Paper-DNR-Proteomics/blob/master/images/2017-02-19_final-Digest-Settings3.png?raw=true)

*Note: Use default settings*

![PDS tab 4](https://github.com/RobertsLab/Paper-DNR-Proteomics/blob/master/images/2017-02-19_final-Digest-Settings4.png?raw=true)

*Note: Use default settings*

To execute digest, on select "Parse and Digest" on Tab #2.

### Step 2c. Modify .tabular digested proteome
The digested proteome will provide information unnecessary for PECAN.

![full-digested-proteome](https://cloud.githubusercontent.com/assets/22335838/23740214/790b2008-0457-11e7-8c26-e3aea0881759.png)

The only columns needed for PECAN are the first two: "Protein_Name" and "Sequence". These columns can be cut out using `awk` or in [Galaxy](usegalaxy.org). The final .tabular digested proteome should look like this:

![modified-digested-proteome](https://cloud.githubusercontent.com/assets/22335838/23740215/790e76e0-0457-11e7-911f-aa65f6069b61.png)

---

## Step 3. Run PECAN
[PECAN](https://bitbucket.org/maccosslab/pecan/overview) correlates your acquired peptide spectra to a database of known sequences and creates a library of proteins and peptides that you detected in your experiment. PECAN requires several inputs, each of which must be prepared before running PECAN in the command line.

### Step 3a. Create two text files that indicate path for 1) the reference peptide list (in silico protein digestion) and 2) spectra data (mzML files)

The background proteome should be a .txt list with protein names and sequences. It can be the same file as the one generated by the in silico protein digestion step above.

[example peptide path file](https://github.com/RobertsLab/project-oyster-oa/blob/master/analyses/DNR_PECAN_Run_3_20170308/2017-03-08-background-peptides-path-list.txt)

Similar to the peptide path file, this should be a .txt file with the path for each of your `.mzML` files you want to analyze.

[example .mzmL path file](https://github.com/RobertsLab/project-oyster-oa/blob/master/analyses/DNR_PECAN_Run_3_20170308/2017-03-08-mzML-file-path-list.txt)

### Step 3b. Generate isolation scheme file
The isolation scheme is a list of DIA precursor windows with m/z ratios used to analyze samples. The isolation schemes are experiment-dependent, so you need to look at your mass spectrometry method file to figure it out. The final isolation scheme should be formatted as a .csv file. The m/z ratios should be paired.

[example isolation scheme](https://github.com/RobertsLab/project-oyster-oa/blob/master/analyses/2018-02-28-PECAN/PECAN-inputs/2017-03-03-isolation-windows.csv)

### Step 3c. Add Background Proteome to Pecan
Pecan needs to be compiled with the background proteome. To do this:  

1. Copy background proteome to `/home/shared/pecan/PECAN/PecanUtil/`  

2. Add the background proteome to the config file via `gedit /home/shared/pecan/PECAN/PecanUtil/config`. It will be added to the end of the file and follow the format `speciesname = file name` ex: `geoduck = geoduck-background-proteome.csv`  

3. Recompile Pecan via `python /home/shared/pecan/setup.py install`  

### Step 3d. Create a peptide spectral library from your data
This will be done using the `pecanpie` command and the code below:

```
pecanpie -o [directory to create] \ # This is the directory you will navigate to afterwards to run a search.
-b [digested background proteome] \
-n [blib file name] \ # The name of the file you will use in Skyline. No need to include a .blib extension.
-s [species] \ # The species may need to be configured beforehand every time this command is run.
--isolationSchemeType BOARDER \ 
--pecanMemRequest [GB estimate] \ # PECAN will ask you to input a GB estimate of the memory you need. If your estimate is too low, the program will suggest a higher memory for you to use.
[filename for mzML file path list] \ 
[filename for peptide file path] \ 
[filename for isolation scheme file name] \
--fido --jointPercolator
```

This step will be fast because it is just setting up the real PECAN run. Navigate to your newly created directory (specified by the `-o` argument and run the actual search: 

```
cd [directory specified by the -o argument for pecanpie] \
./run_search.sh
```

The search takes a while to run, especially if you are looking for all possible peptides in your proteome. You can check the status of your job with the following code:

```
qstat -f
```

### Step 3e. Confirm creation of .blib file

When `pecanpie` is done running, navigate to the `pecan2blib` folder within your output directory. Inside that folder, you'll find the .blib file, the name of which is specified by `pecanpie -n`.

The .blib file you create will be used in the Skyline workflow (see below).

#Skyline

2. Get protein and peptide abundance information from Skyline.
You will need:

- Skyline (preferably Skyline daily, but you need to get permission to download it)

- your .blib file from pecan

- your fasta proteome, including QC protein sequence

- your demultiplexed mzML files or raw files if demultiplexing was not necessary

You should already have instructions on how to use Skyline. You will put all your data in Skyline and export the peak area integration values (your proxy for peptide/protein abundance). You are relying on Skyline to pick the correct peaks across all samples. I would check how well Skyline is doing by 1) ensuring that all your QC peptides are chosen correctly and 2) ensuring that a certain number (10? 20? 100?) of your peptides were chosen correctly across all samples. From this information you can derive an estimated error rate for Skyline.
You export your peak areas in a csv file.

3. Normalize your peak areas for experimental peptides/proteins by peak areas of your QCs.
I do this by calculating the coefficients of variation for all my QC peptides across all samples. Since the same amount of QC was spiked into each sample, peak areas should be the same. I then select the QC peptides with CV<10 and I normalize all experimental peak areas by the average of those QC peak areas. You will then have a normalized dataset to analyze. There is also an argument for normalizing by total ion current (TIC), which can be found on your raw files. TIC should correlate to amount of protein loaded into the mass spec and is probably an easier and more universal way of normalizing your data to differences in protein amount.