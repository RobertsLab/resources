### Mass Spec Tutorial for the Roberts Lab

Different types of mass spec (MS) experiments - summary

#### Data dependent acquisition (DDA), also called shotgun proteomics

   1. DDA data are considered to be a broad survey of the sequenced proteome. All ionized peptides are analyzed in the MS1 scan and the top 5-20 of these peptides are further analyzed in the MS2 scan. The MS1 scan gives information on the peptide’s mass (m) to charge (z) ratio. The MS2 scan gives information on peptide fragment’s m/z, allowing for peptide sequence inference.
   2. Considered to be relatively low resolution, although broad, data sets. This is because only the top 5-20 peptides for each MS1 scan are fragmented for characterization.
   3. Analytical pipelines are well established and straightforward. Data are searched against a database of known protein sequences or de novo sequencing can be performed. Database searches perform considerably better with a proteome from the same species.
      
#### Data independent acquisition (DIA)
   1. DIA also broadly surveys the proteome, but does a much deeper sequencing than DDA, retaining the dynamic range of peptides.
   2. Essentially, the MS1 scan of the data is skipped and “all” ionized peptides within a desired scan window (e.g., 500-502 m/z) are fragmented, yielding a MS2 spectra.
   3. To sequence even more deeply, sample injections can be divided into shorter m/z scan windows. For example, a typical experiment will analyze all the data between 400-1000 m/z, but this could be divided into 3 injections of windows 400-600, 600-800, 800-1000 m/z. Using an instrument with a cycle time of 20Hz (i.e., 20 MS2 scans can be completed per second), each tandem MS2 produced would result from ions in a  10 m/z range fragmented at one time.
   4. Analytical pipelines are onerous for discovery-driven proteomics when the width of the window is wide.  Narrow windows that only isolate 2 m/z at a time, are standard searches because typically within a 2m/z wide window, only 1 peptide resides.
   5. Becuase DIA does not exclude any ion,  SRM assay development is easier from DIA data because it yields a higher resolution library, generating more peptides and transitions to choose from for the assay.

#### Selected reaction monitoring (SRM), also called targeted proteomics or parallel reaction monitoring
   1. SRM fully characterizes specific peptides that are provided in the instrument method.
   2. Analysis is executed on a triple quadrupole instrument. The MS is programmed to monitor specific peptide fragments, or transitions, that are diagnostic of a peptide or protein of interest. In a given chromatography gradient for a sample, the instrument will dwell on a peptide transition for the amount of time it has divided by the number of transitions in the method. Thus, fewer transitions results in higher resolution peptide measurements.
   3. Analytical pipelines are straightforward, but can be tedious given problems with Skyline’s automated peak picking.

### Pipeline for creating SRM assays (details for C and D can be found in this document) 
   1. Select proteins/peptides of interest
      1. This can be based on previous experimental data, literature reviews, or interest in specific pathways.
   1. Choose a library for instrument method development
      1. Library can be constructed from DDA or DIA data.
      2. The best quality library will be DIA data from the same sample cohort used for SRM analysis because the data is higher resolution, transitions peaks are more intense, and (typically) there are more peptides identified per protein to choose from
   1. Run PECAN
      1. PECAN was developed by Sonia Ting in the MacCoss lab. It takes a list of peptides of interest for a study (see A) and searches for those peptides in experimental data chosen for library construction (B). 
      2. Its output is a .blib file that can be imported into Skyline. When the .blib file and a corresponding background proteome are in Skyline, the program will identify those peptides of interest in experimental data.
   1. Develop instrument method in Skyline
      1. Skyline can be used to view peptide transition quality. This is helpful in choosing transitions that are informative and reliable for the SRM assay.
      2. For each protein in your assay, you ideally want at least 3 peptides; for each peptide, you want at least 4 transitions.
      3. Export the list of selected transitions from Skyline.
   1. Run SRM assay on a triple quadrupole MS
      1. The exported transition list can be uploaded to an instrument method. Do not exceed 150-200 transitions per method. If you have more transitions, you can make more than 1 method, but you will have to inject at least 1 ug of your sample for each method.
      2. Quality control standards (we use Pierce’s retention time calibration mix + BSA) should be present in a known quantity in each sample. This allows for quality checks of the instrument and method and for monitoring shifts in retention time.
      3. SRM assays can measure peptides down to the attomolar concentration. Accurate quantities of peptides can be achieved by spiking in a known amount of synthetic peptide into each sample (these peptides are very expensive).
   1. Analyze SRM data in Skyline
      1. SRM data can be imported into Skyline for peak area quantification.
