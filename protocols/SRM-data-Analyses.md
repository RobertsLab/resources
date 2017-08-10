# SRM Analyses

Selected Reaction Monitoring, or SRM, assays quantify abundance of targets identified from a previous [DIA](https://github.com/sr320/LabDocs/wiki/DIA-data-Analyses) mass spectrometer run, as opposed to a full proteome scan. This provides higher resolution data for proteins and peptides of interest.

### **Basic overview of the SRM pipeline**:

1. Identify SRM targets
2. Analyze data 

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

## Analyze data