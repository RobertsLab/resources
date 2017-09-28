# SRM Analyses

Selected Reaction Monitoring, or SRM, assays quantify abundance of protein targets identified from a previous [DIA](https://github.com/RobertsLab/resources/blob/master/protocols/DIA-data-Analyses.md) mass spectrometer run, as opposed to a full proteome scan. This provides higher resolution data for proteins and peptides of interest.

### **Basic overview of the SRM pipeline**:

1. Identify SRM targets
2. Clean data in Skyline
3. Analyze data with multivariate methods

---

## Step 1: Identify SRM targets

Using information for a previous mass spectrometry run, identify protein, peptide and transition targets for SRM. Targets must have clean, high-quality peaks in Skyline with little to no interference. Data for each peak must be present in all samples. All protein targets should have three corresponding peptides, and each peptide should have three transitions. It is possible to use a protein target with only two peptides, as long as they are high-quality. 

### Step 1a. Filter out potential targets.

There are several options for initially filtering out possible SRM targets, listed below. It's possible you will have to use a combination of all these options.

#### Option A. Fold-change.

This option is used if you want to select targets that have a higher fold change in some treatments versus others.

1. Export Skyline report using "Protein & Area, by replicate" setting on Roberts Lab Windows machine.
2. Calculate fold change for each protein.
3. Select possible target proteins

#### Option B. MSstats

This option is used if you want to select targets that are differentially expressed between samples, based on [Condition and BioReplicate information](https://github.com/sr320/LabDocs/wiki/DIA-data-Analyses#step-4g-add-condition-and-bioreplicate-information-optional). An example of the code used for MSstats can be found [here](https://github.com/RobertsLab/project-oyster-oa/blob/master/analyses/DNR_Skyline_20170524/2017-06-22-MSstats/2017-06-22-MSstats.R).

1. Export Skyline report using "SkylinetoMSstats" setting on Roberts Lab Windows machine.
2. Install MSstats

```
source("http://bioconductor.org/biocLite.R")
biocLite("MSstats")
library(MSstats)
```

3. Import data and process using `SkylinetoMSstatsFormat`
  - Can use default settings, which include UseUniquePeptide = TRUE
  - May also be useful to use the argument removeProtein_with1Peptide = TRUE because a protein needs to have at least two peptides to be used as a target for SRM. 
4. Process data further using `dataProcess`
  - Can use default settings, which include log transformation using base 2, normalization by medians based on reference signals, and adding NA for missing peaks.
5. Create a contrast matrix: Specify which pairwise comparisons should be examined. Each pairwise comparison had its own row, where a value of -1 or 1 indicated which conditoins should be compared. The rows were then combined into a matrix using rbind.
6. Use `groupComparison`: Providing the contrast matrix and processed data, conduct pairwise comparisons for all proteins. Results can be exported after this step and proteins under a certain adjusted p-value can be used as the first filtering of targets.

MSstats has built in ways to visualize the results of pairwise comparisons using `groupComparisonPlots`. The Volcano Plot color-codes proteins based on their differential expression for each pair of conditions compared. The Comparison plot visually compares fold change for each protein across conditions examined. The Heatmap visualizes conditions and proteins at the same time.

#### Option C. Annotations

1. Merge list of proteins (either from Skyline directly, or from Options A or B) with annotations and e-values from blast.
2. Select proteins of interest for preliminary filtering

After preliminary filtering, you should have a list of about 100-150 proteins.

### Step 1b. Check targets in Skyline

SRM targets must be high-quality peaks, with data present for each sample from the previous mass spectrometry run. For this reason, it is important to check that potential targets from Step 1a are good in Skyline.

1. Make a copy the Skyline document from the previous mass spectrometry run used to identify potential targets
2. Check quality of potential targets. Delete a protein, peptide or transition if it is not good. To delete something, click on it, then press "Delete".
  - Remove all precursor ions
  - Remove a protein if it has less than two peptides associated with it
  - Remove a peptide if
    - It has less than four transitions
    - There are more than three peptides per protein, and it is one of the lower quality peptides (i.e. there is a lot of noise or interference from other peaks)
    - There are samples with missing data (no peak at all)
  - Remove a transition if
    - There is not a clear, single peak in both technical replicates collected in DIA
    - There are greater than five transitions per peptide, and it is one of the lower quality or lower abundance transitions

An example of an ideal peak:

![ideal](https://user-images.githubusercontent.com/22335838/28181239-bfa598b8-67bc-11e7-9d2e-2c9ac7f3ba57.png)

An example of peak interference that indicates the peptide should be deleted:

![noisy peptide](https://user-images.githubusercontent.com/22335838/28151874-3384909c-6752-11e7-8c5f-aedacc1669f8.png)

An example of a noisy transition (highlighted in red) that should be deleted:

![noisy transition](https://user-images.githubusercontent.com/22335838/28181196-91d0eeba-67bc-11e7-976a-2716159a9e58.png)

3. [Modify peak boundaries](https://github.com/sr320/LabDocs/wiki/DIA-data-Analyses#step-5b-spot-check-peptides) if needed.
4. Filter down list until there are 150 transition targets, including QC peptides.
5. When finished, export the target transitions using File >> Export, select "Transition List". Under "Instrument Type" specify the type of mass spectrometer you will use. Save the file as a .csv

<img width="485" alt="screen shot 2017-07-21 at 10 59 24 am" src="https://user-images.githubusercontent.com/22335838/28476130-b6199a4a-6e03-11e7-977a-b196388a00a3.png">

<img width="343" alt="screen shot 2017-07-21 at 10 59 18 am" src="https://user-images.githubusercontent.com/22335838/28476131-b755319e-6e03-11e7-80d4-d8b7c56213c7.png">

## Step 2: Data Cleaning in Skyline

### Step 2a: Collect necessary materials

Refer to [DIA analysis protocol](https://github.com/RobertsLab/resources/blob/master/protocols/DIA-data-Analyses.md) for specifics regarding materials.

- Skyline (preferably Skyline daily, but you need to get permission to download it)
- Skyline document used for DIA analysis

OR

- .blib file from `pecanpie`
- Undigested FASTA background proteome, including QC protein sequence
- RAW files from mass spectrometer (Demultiplexing is not necessary for SRM analysis since discrete m/z windows were provided in the isolation scheme)

### Step 2b: Create a new Skyline document

Create a copy of your [DIA Analysis Skyline Document](https://github.com/RobertsLab/resources/blob/master/protocols/DIA-data-Analyses.md), then consolidate with the settings below. Be sure to delete proteins from the analyte tree that are not used for target analysis. If making a Skyline document from scratch, see specifics on document creation in the DIA data Analysis protocol.

**Peptide settings**:

<img width="270" alt="screen shot 2017-09-13 at 2 01 25 am" src="https://user-images.githubusercontent.com/22335838/30981331-e377cc3a-a438-11e7-88b0-2921d41fec11.png">

<img width="271" alt="screen shot 2017-09-13 at 2 01 30 am" src="https://user-images.githubusercontent.com/22335838/30981335-e38efaa4-a438-11e7-9ab9-c67296e5e838.png">

<img width="268" alt="screen shot 2017-09-13 at 2 01 32 am" src="https://user-images.githubusercontent.com/22335838/30981333-e3849cd0-a438-11e7-8511-668b8dca4510.png">

<img width="271" alt="screen shot 2017-09-13 at 2 01 34 am" src="https://user-images.githubusercontent.com/22335838/30981332-e3817fa0-a438-11e7-93f7-4400021ad5aa.png">

<img width="271" alt="screen shot 2017-09-13 at 2 01 36 am" src="https://user-images.githubusercontent.com/22335838/30981334-e3864030-a438-11e7-9a13-56b0b774f9bc.png">

<img width="273" alt="screen shot 2017-09-13 at 2 01 37 am" src="https://user-images.githubusercontent.com/22335838/30981336-e3a0a9b6-a438-11e7-9a31-4e9b52f8f889.png">

**Transition settings**:

<img width="273" alt="screen shot 2017-09-13 at 2 01 52 am" src="https://user-images.githubusercontent.com/22335838/30981382-0ab2f784-a439-11e7-9123-23ffa406bae3.png">

<img width="271" alt="screen shot 2017-09-13 at 2 01 53 am" src="https://user-images.githubusercontent.com/22335838/30981383-0ab40d2c-a439-11e7-9ace-61871fb3efbd.png">

<img width="275" alt="screen shot 2017-09-13 at 2 01 55 am" src="https://user-images.githubusercontent.com/22335838/30981384-0ab70b4e-a439-11e7-8680-349a1fd18f16.png">

<img width="272" alt="screen shot 2017-09-13 at 2 01 57 am" src="https://user-images.githubusercontent.com/22335838/30981381-0ab24366-a439-11e7-9f37-23846c8cd2e9.png">

<img width="271" alt="screen shot 2017-09-13 at 2 01 58 am" src="https://user-images.githubusercontent.com/22335838/30981385-0ac3940e-a439-11e7-9c9a-095a1ea84fcd.png">

Under File > Import > Results, select "Add single-injection replicates in files". Navigate to the directory with RAW files. Select files to import and click "Open". Skyline gives you the option to remove common prefixes from file names when importing into Skyline. Removing these prefixes makes it easier to view filenames in Skyline, but it is not necessary.

### Step 2c: Examine dilution curve (optional)

If time permits, it is ideal to create a dilution curve with protein samples. The purpose of this is to verify the mass spectrometer methods are detecting the specific proteins desired. Peptide detection should decrease as the concentration of protein loaded decreases, and vice versa. If this is not the case, then the machine is not properly detecting the specific peptide, and that peptide should be removed from analysis.

Using the same Skyline settings as the SRM document in [Step 2b](https://github.com/RobertsLab/resources/blob/master/protocols/SRM-data-Analyses.md#step-2b-create-a-new-skyline-document), create a separate Skyline document for dilution curve analysis. Use predicted retention times from DIA data to identify the correct peptide peak in each sample. To select the proper peak, simply click on it. If the peak is not recognized as a peak, use the crosshair to select the peak on the x-axis (retention time). After selecting the correct peak, right click and select "Apply Peak to All." This may not correctly identify the proper peak for all samples, but for a good majority.

Once the proper peaks are selected, examine peak areas across the dilution curve. As the concentration of protein loaded decreases, so should peak area:

![30131820-0838676a-9303-11e7-9068-f5f26c802bd0](https://user-images.githubusercontent.com/22335838/30982905-abf5a318-a43d-11e7-97a1-aa166e0a6e67.png)

If this is not the case, then remove the peptide from the analysis. After checking the curve, all target proteins should have at least two associated peptides before proceeding. If not, the entire protein needs to be excluded.

### Step 2d: Check peaks in Skyline

*If [Step 2c](https://github.com/RobertsLab/resources/blob/master/protocols/SRM-data-Analyses.md#step-2c-examine-dilution-curve-optional) completed: Remove peptides and proteins from analyte tree if they do not meet the criteria outllined above*

Use predicted retention times from DIA data to identify the correct peptide peak in each sample. To select the proper peak, simply click on it. If the peak is not recognized as a peak, use the crosshair to select the peak on the x-axis (retention time). After selecting the correct peak, right click and select "Apply Peak to All." This may not correctly identify the proper peak for all samples, but for a good majority.

While checking every peptide peak is correctly selected for each sample, modify the peak boundaries so they properly encompass the entirety of the peak. If there is no peptide peak present in a sample, simply right click and select "Remove Peak." If there is no chromatogram present for any peptide in a sample, remove that sample from analysis. 

### Step 2e: Export Data

Under File > Export > Report, use the following settings to export Skyline data as a .csv.

![30132381-03f87a94-9305-11e7-8dfa-812e738abbd0](https://user-images.githubusercontent.com/22335838/30983237-ad0f3056-a43e-11e7-8d51-d99207d262e1.png)

Under File > Share, save the Skyline document as a "Complete" document and upload to OWL.

## Step 3: Analyze data

### Step 3a: Check technical replication

Create a nonmetric multidimentional scaling (NMDS) plot using data from all non-PRTC peptides to see if technical replicates from the mass spectrometer cluster together. If they do, the technical replication is sound, and replicates can be averaged for analyses.

[Sample R Code](https://github.com/RobertsLab/project-oyster-oa/blob/master/analyses/DNR_SRM_20170902/2017-09-06-NMDS-for-Technical-Replication.R)

### Step 3b: Analyze data as appropriate

Analysis methods will vary based on project.
