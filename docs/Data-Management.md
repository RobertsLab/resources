This page is intended to document all aspects of data management, from the day-to-day, formal NGS and proteomics plans, and general archiving options. Inspiration for this has been provided by Tim Essington and Gordon Holtgrieve who have developed similar documentation.



Data must be 1) adequately described via metadata, 2) managed for data quality, 3) backed up in a secure manner, and 4) archived in an easily reproducible format.

# Metadata     
All research data must be accompanied with a thorough description of that data from the beginning of the work. Metadata describes information about a dataset, such that a dataset can be understood, reused, and integrated with other datasets. Information described in a metadata record includes where the data were collected, who is responsible for the dataset, why the dataset was created, and how the data are organized.   

# Data Quality Standards.     
Students must take care that protocols and methods are employed to ensure that data are properly collected, handled, processed, used, and maintained, and that this process is documented in the metadata.


# Backup and Storage     
Primary should be stored in several locations with canonical versions on Gannet (see below).

Data, including intermediate analysis, needs to have a url. This most often means it will live on a Network Attached Storage Device (NAS; aka a server).

Gannet is a Synology RS3618xs NAS :

- RS3618xs uses 16TB HDDs (n = 12)

## Data on Gannet is backed up in the following ways:

- #### Synology Hybrid RAID

    - Mirrors data across HDDs, which reduces total storage capacity by 50%
    - Allows for up to two concurrent HDD failures before data loss occurs


- #### Gannet/web folder

    - One-way sync from Gannet to [UW Google Drive](https://drive.google.com/open?id=1l0jc1Pj7gldNJRrfrM_Ld-T0it5LFyJG) via the Synology Cloud Sync app.
    - Backup frequency: Daily
    - Access: Public (read-only)


## Daily Data on Gannet


Using the Gannet NAS to store your data:

1. Ask Steven or Sam to generate a user account for you. A folder will be created for you in: ```gannet/web/``` Ask Steven/Sam for the name of the folder, as well as your username and password.
2. Upload data to your Gannet web folder:
    1. Navigate to <http://gannet.fish.washington.edu/>
    2. Click on `Web Browser login`.
        1. If it's your first time visiting this page, your browser will present you with a warning about an insecure site or bad certificate. That's OK. Click on the option to add an exception for this site.
    3. Enter username and password. (NOTE: If it's your first time accessing your account, please change your password by clicking on the silhouette in the upper right corner, then "Personal" in the dropdown menu).
    4. Navigate to File Station > web > your_folder (If you don't see the File Station icon, click on the icon of four squares in the upper left corner and select File Station from the subsequent menu).
    5. Click-and-drag files from your computer to your ```gannet/web``` folder.

Files that you have uploaded to your_folder are publicly viewable: http://gannet.fish.washington.edu/your_folder

You can use the URLs for your files for linking in your notebook.

### IMPORTANT!

_All folders need to contain a readme file._

The readme files should be plain text (i.e. do not create/edit the file with a word processor like Microsoft Word or LibreOffice Writer) and should describe the contents of the folder. If there are directories in the same folder as your readme file, the directory names should be listed and a brief description of their contents should be provided.

_Please refrain from using any non alpha-numeric (including spaces) in file and folder names._

---

## NGS Data Management Plan

**Raw Data**    
1. As sequencing facility provides data, files are downloaded to our local NAS (owl), in the correct species subdirectory within `nightingales`.  http://owl.fish.washington.edu/nightingales/

2. MD5 checksums are generated and compared to those supplied by the sequencing facility.

  1. Append the generated MD5 checksums to the `checksums.md5` file. If that file does not yet exist, create it, and add the generated checksums to the new `checksums.md5` file.

3. The [Nightingales Google Spreadsheet](https://docs.google.com/spreadsheets/d/1_XqIOPVHSBVGscnjzDSWUeRL7HUHXfaHxVzec-I-8Xk/edit) is updated.

  1. Each library (i.e. each sample with a unique sequencing barcode) is entered in its own row.
  2. `SeqID` is the base name of the sequencing file (i.e. no file extensions like ".fq.gz" or ".gz")
  2. Each library receives a unique, incremented `Library_ID` number.
  3. Each library receives a `Library_name`; this may or may not be unique.


**Backup**    
* The Google Docs spreadsheet [Nightingales Google Spreadsheet](https://docs.google.com/spreadsheets/d/1_XqIOPVHSBVGscnjzDSWUeRL7HUHXfaHxVzec-I-8Xk/edit) is backed up on a regular basis? by downloading tab-delimited file and pushing to LabDocs Repository, with the file name `Nightingales.tsv`

* `owl/nightingales` is automatically backed up to two locations, both managed by Synology apps:

  - Amazon Glacier: Backup task occurs weekly on Mondays at 00:00.

  - CloudSync to [UW Google Drive](https://drive.google.com/drive/folders/0BzKkDWZ6tIK4STQ5d2xQYVdyN28?usp=sharing): Backup occurs in real-time any time new files, or changes to existing files, are detected.



**SRA Upload**

* Sam will upload all high-throughput sequencing data to the [NCBI Short Read Archive (SRA)](https://submit.ncbi.nlm.nih.gov/about/sra/). Once submitted, the BioProject accession and a link to the NCBI BioProject will be added to the `SRA` column in the [Nightingales Google Spreadsheet](https://docs.google.com/spreadsheets/d/1_XqIOPVHSBVGscnjzDSWUeRL7HUHXfaHxVzec-I-8Xk/edit).


---

## Proteomics Data Management Plan

**Raw Data**    
1) As sequencing facility provides data, files are downloaded to our local NAS (owl), in the root `phainopepla` directory.  http://owl.fish.washington.edu/phainopepla/ These data are organized by species, then by mass spectrometer run date (e.g. YYYY-MM-DD). For each run date, all `RAW` files (including blanks, sample, and QC files) should be included in the directory with their original names. Inside of the YYYY-MM-DD directory there **should be a Readme file with the following information**: Description of each file (eg. treatment, blank, etc), experimental design, link to more information.

2) The [Spreadsheet](https://docs.google.com/spreadsheets/d/151KPj22gf1M11otKwLfFbSjfZrY2zXDKUE1N3_mopyw/edit?usp=sharing) is then updated. Each "mass spectrometer run date" will be a new row in the sheet.




---

## Histology Data Management Plan

1) Before histology cassettes are sent off for processing, fill out the [Histology-databank](https://docs.google.com/spreadsheets/d/1BIbDleJPEiKrmx7JwNIPwg2pM-thuZ39upmenldx4pA/edit#gid=0) with all relevant information at the sample(tissue) level. Reserve space for blocks and slides by adding block-location and slide-location information. Each sample should have a `unique-sample-ID` which is:

- `experiment-date_organism-label_tissue`

2) After histology blocks are returned, photograph blocks and slides and label such that the location of each sample(tissue) can be readily understood.

3) Image each sample(tissue). Use the following convention for saving images:

- `[FULLTIMESTAMP]-[unique-sample-ID]-[magnification].jpeg

  - e.g. `20180924-angasi013-10x.tif`

All images should be stored in the proper species directory at http://owl.fish.washington.edu/hesperornis/



---

# Data Archiving
The goal for data archiving is to make your research easily understandable and reproducible in the future. It is therefore incumbent upon the researcher that, by the end of a project, care and effort is given to providing a highly organized and traceable accounting of the research that is archived in perpetuity.  At a minimum, this archive should include: raw and full processed data, complete metadata, all computer code, and any research products (manuscripts, published articles, figures, etc.).
You will find that creating a usable data archive is much easier to do as you go, rather than waiting until the end of your project!


## Options include     
- GitHub -> Zenodo.     
- Figshare
- UW ResearchWorks
- Open Science Framework



---
# Easy file upload for Collaborators

![screencast_eagle](https://raw.githubusercontent.com/wiki/RobertsLab/resources/img/File_upload.gif)




---

Finally, data will be most usable if it is as flexible as possible.  So an excel spreadsheet with different information on different tabs is not very flexible.  Much better to have a text file, with the data in “long form”.  This means rather than have a ton of columns, have a ton of rows.

see    
Broman KW, Woo KH. (2017) Data organization in spreadsheets. PeerJ Preprints 5:e3183v1 [https://doi.org/10.7287/peerj.preprints.3183v](https://doi.org/10.7287/peerj.preprints.3183v)
