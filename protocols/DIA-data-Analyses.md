# DIA Analyses

Data-Independent Mass Spectrometry is a bottom-up proteomics method that separately gathers MS/MS spectra and MS survey spectra. The following workflow describes how to analyze DIA data.

### **Basic overview of the DIA pipeline**:

1) Convert raw files using MSConvert. Simultaneously demultiplex raw data files if data were collected with overlapping windows.

2) Use PECAN to create a peptide spectral library from data 

3) Get peptide and protein abundance information from Skyline 

This wiki is based partly on the following [Evernote entry](https://www.evernote.com/shard/s347/sh/edcb06ab-d008-418f-b28f-52f6614f1c39/2984ab55f427fcfe). 

Note: this might be a little less intuitive than the [DDA pipeline](https://github.com/sr320/LabDocs/wiki/DDA-data-Analyses). Additionally, the pipeline relies on Windows-based programs.

---

## Step 1: Convert RAW files

Based on data collection methods, you will choose either Step 1a OR Step 1b.

### Step 1a. Convert Raw files with MSConvert (No demultiplexing)
Output files from a mass spectrometer are in the .raw format, but PECAN requires demultiplexed .mzML files. [MSConvert](http://proteowizard.sourceforge.net/tools.shtml) is a GUI used to generate these files with the appropriate centroid peaks using 64-bit and zlib compression. However, demultiplexing has not been incorporated into the GUI so if you are demultiplexing you must use command line (see Step 1b).

Below are the settings required for MSConvert in the GUI:

![MSConvert-settings](https://raw.githubusercontent.com/sr320/LabDocs/master/img/MSConvert-settings.png)

Note that these setting [might vary](https://github.com/sr320/LabDocs/issues/486) based on version.

### Step 1b. Convert Raw files with MSConvert (With demultiplexing)

If data were collected with overlapping m/z windows, they need to be demultiplexed. This allows us to parse out peptide abundance data from each individual window. Demultiplexing requires use of the MSConvert command line interface. Before demultiplexing, check for any irregularities in the isolation scheme that will require additional arguments (one example of such a case is found [here](https://github.com/RobertsLab/project-oyster-oa/blob/master/notebooks/2017-04-12-Demultiplex-Raw-Files.ipynb)).

If there are no irregularities, the following code can be used to both convert .raw to .mzML and simultaneously demultiplex:

```
[path to msconvert.exe] --zlib --64 --mzML --filter "peakPicking true 1-2" --filter "demultiplex optimization=overlap_only" *.raw 
```

After the .raw files are converted to demultiplexed .mzML files, upload the .mzML files to the desired location. This information will be used to generate the mzML file path list, an input for the `pecanpie` command used later on.

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

---

## Step 4: Add files to Skyline

The workflow below was adapted from [these tutorial slides](https://github.com/RobertsLab/project-pacific.oyster-larvae/blob/master/Skyline-example-files-ETS.sky/slides01.pdf).

### Step 4a: Collect necessary materials.

- Skyline (preferably Skyline daily, but you need to get permission to download it)
- .blib file from `pecanpie` (see Step 3)
- Undigested FASTA background proteome, including QC protein sequence
- Demultiplexed mzML files, or RAW files if demultiplexing was not necessary

### Step 4b: Import spectral library (.blib)

1. Open a new Skyline file
2. Under Settings >> Peptide Settings >> Library, click "Edit List". If your .blib is already on the list, select it. 
3. If your .blib is not already on the list, click "Add"
  - Name your library and select the .blib file
  - After clicking "OK", select the correct library from the list
4. Under "Pick peptides matching", select "Library"

<img width="363" alt="screen shot 2017-07-21 at 9 00 25 am" src="https://user-images.githubusercontent.com/22335838/28471776-181be092-6df3-11e7-9086-3a8eb037fb78.png">

### Step 4c: Add background proteome

Remember, this background is the fast version of the background proteome from `pecanpie`, undigested.

1. Settings >> Peptide Settings >> Digestion
2. Select "Add" under "Background proteome"
3. Name background
4. Click "Create" under "Proteome file" to choose where to save the background
5. Click "Add file" under "FASTA files", and select your background proteome fasta file
6. Under Prediction tab, make sure "none" is selected for retention time predictor

<img width="475" alt="screen shot 2017-07-21 at 9 02 58 am" src="https://user-images.githubusercontent.com/22335838/28471874-6ac91fa8-6df3-11e7-845f-69c9b43c52e6.png">

### Step 4d: Populate the target analyze tree

1. Open the background proteome fast file and copy all of the protein sequences
2. Paste the sequences into the lefthand, long window in the main Skyline view

Skyline will keep the proteins, peptides, and transitions that match what it finds in the library provided in Step 4b.

<img width="246" alt="screen shot 2017-07-21 at 9 04 28 am" src="https://user-images.githubusercontent.com/22335838/28471929-a1037bb8-6df3-11e7-8c97-a1a47929d4d2.png">

### Step 4e: Adjust transition settings in Skyline

1. Settings >> Transition Settings >> Filter
2. Precursor charges: 1, 2, 3, 4, 5
3. Ion charges: 1 (this is the prevalent fragment, additional charges will increase interference)
4. Ion types: y, p
5. Product ions
  - From: ion 3
  - To: last ion -2

<img width="370" alt="screen shot 2017-07-21 at 9 06 28 am" src="https://user-images.githubusercontent.com/22335838/28472004-e6770df4-6df3-11e7-94b8-2c53c7984e92.png">

6. Settings >> Transition Settings >> Library
7. Ion match tolerance: 0.5 m/z
8. Unselect "if a library spectrum is available, pick its most intense ion"

<img width="421" alt="screen shot 2017-07-21 at 9 07 44 am" src="https://user-images.githubusercontent.com/22335838/28472096-219f3726-6df4-11e7-8d67-00cc4869714a.png">

9. Settings >> Transition Settings >> Full Scan
10. MS1 Filtering
  - Isotope peaks included: Count
  - Precursor mass analyzer: Pick the one that matches the instrument used for mass spectrometry
  - Resolving power: 60,000 at 200 m/z (Experiment-specific, consult methods)
11. MS/MS Filtering
  - Acquisition method: DIA
  - Product mass analyzer: Centroided
  - Mass accuracy: 15 ppm (Experiment-specific, consult methods)
  - Isolation scheme: Copy and paste list of isolation targets from Step 3b.
12. Retention Time Filtering
   - Use scans within 1 minute of MS/MS IDs

<img width="523" alt="screen shot 2017-07-21 at 9 12 55 am" src="https://user-images.githubusercontent.com/22335838/28472275-cdea9872-6df4-11e7-843c-bcf85b0f5d2b.png">

### Step 4f: Import DIA data into Skyline

Under File > Import > Results, select "Add single-injection replicates in files". Navigate to the directory with either demultiplexed mzML files or RAW files. Select files to import and click "Open". 

![27004495-e73e1462-4dbe-11e7-9650-c0a3ef39fa84](https://user-images.githubusercontent.com/22335838/28472442-6d64b9c8-6df5-11e7-883a-193852891444.png)

![27004498-e742c70a-4dbe-11e7-9dd8-3fdb06ac13e3](https://user-images.githubusercontent.com/22335838/28472455-73d93dce-6df5-11e7-9494-ec1c2cca7df2.png)

![27004497-e7427fa2-4dbe-11e7-9061-643f0d53c7cd](https://user-images.githubusercontent.com/22335838/28472462-7b905e62-6df5-11e7-86b5-22517be92712.png)

Skyline gives you the option to remove common prefixes from file names when importing into Skyline. Removing these prefixes makes it easier to view filenames in Skyline, but it is not necessary.

![27004499-e7431fac-4dbe-11e7-898f-7d4909e54729](https://user-images.githubusercontent.com/22335838/28472490-9c29e832-6df5-11e7-85e7-f18fdfe1b723.png)

![27004496-e741535c-4dbe-11e7-9f8e-8bc2559d9c8e](https://user-images.githubusercontent.com/22335838/28472491-9d87046c-6df5-11e7-8516-1a241a89dee1.png)

### Step 4g: Add Condition and BioReplicate information (optional)

Condition and BioReplicate information is necessary if you want to use MSstats to analyze differential protein and peptide abundances. Condition refers to the treatment information, while BioReplicate indicates which replicate the file is.

Under Settings >> Document Settings >> Annotations, check to see if Condition and BioReplicate are listed. If not, click "Add" and select them from the list.

![1](https://user-images.githubusercontent.com/22335838/27007800-8b58b1d8-4e14-11e7-88cb-b3d9405ca0e7.png)

![2](https://user-images.githubusercontent.com/22335838/27007798-8b54dd10-4e14-11e7-8362-2496d1a2f3f4.png)

Then, go to View >> Results Grid and add Condition and BioReplicate information.

![3](https://user-images.githubusercontent.com/22335838/27007799-8b56f2b2-4e14-11e7-9596-2d4bdda2edfa.png)

![4](https://user-images.githubusercontent.com/22335838/27007797-8b538d34-4e14-11e7-88ad-921b7b4f009d.png)

---

## Step 5: Within-Skyline Analyses

### Step 5a: Check that all QC peptides are chosen correctly

### Step 5b: Spot check peptides

1. Randomly select about 100 peptides
2. See if Skyline chose the correct peak for all samples. The peak Skyline chose has a black arrow next to it.
3. If the wrong peak was chosen, select the correct peak
  - Click on the correct peak
  - Right click, the select "Apply peak to all"
4. Shift peak boundaries so the entire peak is selected
  - Select the dashed lines around the peak, and drag to the correct location

Skyline picked the right peak:

![right-peak](https://cloud.githubusercontent.com/assets/22335838/26095588/fe990ed2-39d2-11e7-884e-47ad4eb78e2f.png)

Skyline chose the wrong peak:

![wrong-peak](https://cloud.githubusercontent.com/assets/22335838/26095636/26fcdaca-39d3-11e7-8421-4978949643e6.png)

Skyline identified noise as a peak:

![noise](https://cloud.githubusercontent.com/assets/22335838/26095664/3d39dcc0-39d3-11e7-9509-812cea8e71b2.png)

5. Using this information, generate per-peptide and per-sample error rates.

### Step 5c: Export Skyline data

Peak area integration values serve as a proxy for peptide and protein abundance, so it is important to export this information. Click File >> Export >> Report, select the export settings needed. Ensure the information is exported as a .csv file.

The RobertsLab Windows computer has several presets already established, including "Protein & Area, by replicate" and "SkylinetoMSstats". If analysis will not include MSstats, "Protein & Area, by replicate" may suffice.

![presets](https://user-images.githubusercontent.com/22335838/27842651-aa492a46-60c0-11e7-9f16-c7e0098fd022.png)

### Step 5d: Normalize peak areas

There are a few ways to do this:

1. From Emma: I do this by calculating the coefficients of variation for all my QC peptides across all samples. Since the same amount of QC was spiked into each sample, peak areas should be the same. I then select the QC peptides with CV<10 and I normalize all experimental peak areas by the average of those QC peak areas. You will then have a normalized dataset to analyze.
2. TIC: There is also an argument for normalizing by total ion current (TIC), which can be found on your raw files. TIC should correlate to amount of protein loaded into the mass spec and is probably an easier and more universal way of normalizing your data to differences in protein amount.
3. In MSstats, using the dataProcess function