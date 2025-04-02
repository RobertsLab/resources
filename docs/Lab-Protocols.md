Protocols for benchwork in the lab (e.g. RNA isolation), for commonly used instruments and software (e.g. proteomics data analysis in Skyline), and for commonly performed hatchery practices and tissue sampling.

Foundational protocols can be found [here](https://github.com/RobertsLab/resources/tree/master/protocols). As they become prominent, they will be migrated here for posterity.

## RNA Extraction 
  We often use MRC RNA-zol RT ([protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/MRC_RNAzol-RT-march-2017.pdf)). Depending on downstream needs we might engage in DNAase treatment. 

---

## <a name="reverse_transcription"></a>Reverse Transcription
#### Standard Operating Protocol (SOP)
Written 20150702 by Sam White.

##### Reagents:
- M-MLV Reverse Transcriptase ([Promega: M1701](https://www.promega.com/products/pcr/rt-pcr/m_mlv-reverse-transcriptase/))
- Primers (oligo dT: [Promega: C1101](https://www.promega.com/products/pcr/routine-pcr/oligonucleotides-and-primers_-cdna-synthesis-and-cloning/) OR random: [Promega: C1181](https://www.promega.com/products/pcr/routine-pcr/oligonucleotides-and-primers_-cdna-synthesis-and-cloning/))
- 10mM dNTPs ([Promega: U1511](https://www.promega.com/products/pcr/routine-pcr/dntp-mix/))

##### Personal Protective Equipment (PPE):
- Gloves

##### Equipment:
- Pipettes (10 - 1000uL)
- Filtered pipette tips
- 0.5mL snap-cap microfuge tubes ([Genesee: 22-281A](https://geneseesci.com/shop-online/product-details/22-281A/olympus-plastics-22-281a-olympus-1.7ml-microtubes-assorted-polypropylene-large-cap-box-of-500-tubes-unit))
- Sterile 1.7mL snap-cap microfuge tubes ([Genesee: 22-281S](https://geneseesci.com/shop-online/product-details/22-281S/olympus-plastics-22-281s-olympus-1.7ml-microtubes-clear-sterile-polypropylene-large-cap-ster-5-bags-of-50-tubes-unit))
- Thermal cycler, water bath, or heating block capable of 37C OR 42C.
- vortexer
- ice

#### Procedure
##### Total Time: ~ 1.5 - 2.0hrs
##### Cost/sample: ~ $1.50
<em>IMPORTANT: A single reaction volume = 25uL. The volume of RNA, primer(s) and M-MLV RT used in this protocol are <em>variable</em> and will be specific to your current experiment. The directions below apply to a reaction using 1ug of total RNA. You may need to make changes to accommodate your own conditions.</em>

1. Read the [manufacturer's protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/Promega_MMLV_RT.pdf) (PDF).
2. Read <em>this</em> protocol.
3. Verify sufficient quantities of reagents and samples before beginning.
3. Wear clean gloves.
3. Thaw all RNA and reagents on ice. Prepare all reactions on ice.
3. Transfer 1ug of RNA to 0.5mL snap cap tubes or PCR plate. Adjust volumes of individual samples to 17.75uL with H2O.
4. Add 0.25ug primer per 1ug of RNA in sample (= 0.5uL of Promega oligo dT Cat#C1101 in this example). Total volume (RNA + primers) should equal 18.25uL.
5. Heat samples at 70C for 5 min in thermal cycler, heating block, or water bath.
6. Place samples on ice IMMEDIATELY.
7. Make Master Mix:

    Per Reaction

    * 5 uL 5x Buffer (M-MLV RT Buffer)

      - VORTEX THOROUGHLY TO DISSOLVE PRECIPTATE
 
    * 1.25 uL 10mM dNTPs

    * 0.5 uL M-MLV RT per ug of RNA

8. Mix well by flicking; do not vortex.
9. Add 6.75uL of master mix to each reaction.
10. Mix by pipetting; do not vortex.
11. Incubate @ 42C for 1hr for oligo dT primers OR @ 37C for random primers.
12. Heat inactivate @ 95C for 3 min.
13. Spot spin and store @-20C.

## qPCR 
One of the most used application is for gene quantification. Generally we will use SsoFast Evagreen Supermix (BioRad) ([protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/BioRad_Sso_Fast_EvaGreen_Supermix.pdf)). This requires that we start with cDNA.

### Standard Operating Protocol (SOP)
Written 20150702 by Sam White.

Reagents:
- SsoFast EvaGreen Supermix ([BioRad: 172-5203](https://github.com/sr320/LabDocs/blob/master/protocols/Commercial_Protocols/BioRad_Sso_Fast_EvaGreen_Supermix.pdf))
- Primer working stocks (10uM)
- DNase-free H2O (NanoPure H2O)

Personal Protective Equipment (PPE):
- Gloves

Equipment:
- Pipettes (10 - 1000uL)
- Filtered pipette tips
- White PCR plates, non-skirted, low profile ([USA Scientific: 1402-9590](http://www.usascientific.com/non-skirted-96-well-PCR-plate-low-profile-white.aspx))
- Optically clear strip caps ([USA Scientific: 1400-3800](http://www.usascientific.com/8-capstrip-0.2ml-tubes-flat-top.aspx))
- Sterile 1.7mL snap-cap microfuge tubes ([Genesee: 22-281S](https://geneseesci.com/shop-online/product-details/?product=22-281S))
- Real-time PCR machine
- ice

Procedure
Total Time: ~ 2.0 - 4.0hrs
Cost/sample: ~ $0.42

1. Read the [manufacturer's protocol](https://github.com/sr320/LabDocs/blob/master/protocols/Commercial_Protocols/BioRad_Sso_Fast_EvaGreen_Supermix.pdf).
2. Read <em>this</em> protocol.
3. Verify sufficient quantities of reagents and samples before beginning.
4. Wear clean gloves.
5. Prepare master mix. Be sure to make a master mix volume that will accommodate the following: all of your samples, two water (i.e. no template controls; NTC) samples, plus an extra 10% to accommodate pipetting errors. A single reaction is shown below:

    |Component  |Volume(uL)    |Final Concentration    |
    |----|----|----|
    |2x SsoFast EvaGreen Supermix    |10    |1x    |
    |Forward Primer (10uM)|0.5uL|0.2uM|
    |Reverse Primer (10uM)|0.5uL|0.2uM|
    |Water|Variable|Use to bring reaction volume up to 20uL (including template)|

6. Distribute appropriate amount of master mix (volume of master mix + template = 20uL) to white PCR plate.
7. Add template.
8. Cap with optical PCR caps.
9. Spin plate for 1min @ 3000g.
10. Put plate in real-time PCR machine.
11. Recommended cycling parameters (40 cycles) are listed below. They may need to be changed to accommodate your specific primers/samples. See manufacturer's protocol for recommendations.

    Step 1 - 98C 2mins

    Step 2 - 98C 5secs

    Step 3 - 60C 5secs

    Step 4 - Plate read

    Step 5 - Got to Step 2 39 more times

    Step 6 - Melt curve 65C - 95C, increment 0.5C, wait 2secs, plate read.
  
### qPCR Data Analysis

Step 1: Check for quality control of the qPCR data

Before starting the analysis, it is important to check the quality control of the qPCR data to ensure that the data is reliable. Quality control can be done using the following methods:

- Check for amplification curves: Ensure that amplification curves are present for all the samples. Absence of amplification curves might indicate poor quality RNA or experimental errors.     
- Check for amplification efficiency: Calculate the amplification efficiency for the target and reference genes. The efficiency should be between 90-110%.    
- Check for melting curves: Ensure that melting curves show a single peak for all the samples. Presence of multiple peaks might indicate non-specific amplification or primer-dimer formation.    
- Check for threshold cycle (Ct) values: Ensure that Ct values are consistent across all the samples.  

Step 2: Calculate the relative expression of the target gene    

To calculate the relative expression of the target gene, use the following formula:

ΔCt = Ct_target – Ct_reference

Where Ct_target is the cycle threshold of the target gene and Ct_reference is the cycle threshold of the reference gene (in this case, actin).

Step 3: Calculate the fold change of the target gene

To calculate the fold change of the target gene, use the following formula:   

Fold change = 2^(-ΔCt)

Step 4: Statistical analysis

After calculating the fold change, perform statistical analysis to determine the significance of the results. This can be done using t-tests or ANOVA. A p-value of less than 0.05 is considered significant.

Step 5: Interpretation of results

After obtaining the statistical results, interpret the results by comparing the fold change of the target gene in the experimental group to the control group. A fold change greater than 1 indicates upregulation, while a fold change less than 1 indicates downregulation.
  
### CFX Maestro Software

#### Plate Spreadsheet Import

1. Modify [cfx_plate_template.csv](../protocols/cfx_plate_template.csv) (CSV) to your desired `Target Name` and `Sample Name` and save as a CSV file.

2. In CFX Maestro, create a new plate: `File > New > Plate...`.

3. Highlight all wells.

4. Select `Sample Type` of `Unknown`.

5. In the `Target Names` section, click on the empty box next to `SYBR`.

6. Click on the `Spreadsheet View/Importer` tab along the top.

7. Click `Import`.

8. Find the file you saved in Step 1 and click `Open`.

9. Click `Okay`.

10. Update plate layout with any different `Sample Type` (e.g. NTC, Positive Control, etc.), `Technical Replicates` and/or `Trace Styles`.

11. Save the file.
  

## Common Physiological Assays of Interest

| Assay | Measurement | Reference |
|-|-|-|
| Oxygen consumption (OC) | Volume of O2 consumed animal-1 hour-1 | (J. Widdows and Johnson 1988) |
| Clearance rate (CR)  | Volume of water cleared of particles animal-1 hour-1 | (Pernet et al. 2007) |
| Filtration rate (FR) | (weight of faeces + pseudofaeces h-1) x [(weight total particulates per volume seawater) ÷ (weight inorganic matter per volume seawater)] | (Hawkins et al. 1996) |
| Excretion rate (ER) | Ammonia excreted hour-1 | (John Widdows, Donkin, and Evans 1985) |
| Net organic ingestion rate (NOIR) | FR x (organic fraction within total particulates available) | (Hawkins et al. 1996) |
| Net organic absorption rate (NOAR) | NOIR - [(weight of total faeces egested h-1) x (organic fraction of faces)] | (Hawkins et al. 1996) |
| Total carbohydrates | Total carbohydrate content of oyster meat | (Dubois et al. 1956) |
| Total lipids | Total lipid content of oyster meat | (Bligh and Dyer 1959) |
| Total protein | Total protein content of oyster meat | (Jeung et al. 2016) |
| Glycogen content | Total glycogen content as a fraction of total protein | (Krisman 1962) |
| Condition index (CI) | Dry meat weight (internal shell cavity volume)-1 x 100    | (Lawrence and Scott 1982) |
| Reproductive status | Stage of gonadal development determined through histological observation | (Matt and Allen 2021) |
| Ash free dry weight (AFDW) | Dry weight of oyster meat after incineration at 500℃ | (Ricciardi and Bourget 1998) |

_Associated Calculations_


| Parameter | Calculation | Reference |
|-|-|-|
| Protein synthesis rate (PR) | Mass of protein synthesized individual-1 hour-1 | (Pace and Manahan 2006) |
|Protein turnover rate |protein synthesis rate ÷ (total protein content)-1 x 100 |(Pan, Applebaum, and Manahan 2015) |
|Net absorption efficiency (AE) |NOAR ÷ NOIR |(Hawkins et al. 1996) |
|Standard metabolic rate (SMR) | |OC hour-1 mass-1 | (J. Widdows and Johnson 1988)|
|Consumption (C) | CR (l g-1 h-1) x POM (mg l-1) x 23 J mg-1 ash-free dry weight | (J. Widdows and Johnson 1988)|
|Respiration (R) | VO2 (ml 02 g-1 h-1) x 20.33 J ml-1O2 | (J. Widdows and Johnson 1988)|
|Energy lost to excreta (U) |mg NH4 g-1 h-1 x 19.4 J mg-1 NH4 |(J. Widdows and Johnson 1988)|
|Absorbed ration (A) |C x AE| (J. Widdows and Johnson 1988)|
|Production (P) |A - (R + U)| (J. Widdows and Johnson 1988)|
|Scope for growth (SFG) |SFG = A - (R + U), where A = energy absorbed; R = respiratory energy expenditure; U = energy lost through excreta | (J. Widdows and Johnson 1988)|

## Resazurin metabolic assay 

Resazurin metabolic assays are used to measure the metabolic rate of marine organisms. This protocol has been developed for use in oysters, but can be adapted for other organisms.   

Contact: ashuff (at) uw (dot) edu

### Standard Operating Protocol (SOP)
Written 20250401 by Ariana Huffmyer.  

#### Overview 

This protocol is written for small oyster spat, but can be adapted for other life stages. This protocol is based on [previous work in the lab by Colby E.](https://genefish.wordpress.com/author/colbyelvrum/) and as used in our analysis of oyster seed [metabolic response](https://ahuffmyer.github.io/ASH_Putnam_Lab_Notebook/Initial-analysis-of-resazurin-metabolic-rates-in-10K-Seed-oysters/) and [survival](https://ahuffmyer.github.io/ASH_Putnam_Lab_Notebook/10K-seed-resazurin-survival-analysis/).   

#### Materials and preparing solutions

##### 1. Stock resazurin solution 

To make the resazurin stock solution (10 mL) mix the following. We will use this solution for multiple trials.  

- [0.5 g resazurin salt](https://www.thermofisher.com/order/catalog/product/R12204)
- 10 mL DI water
- 10 µL DMSO

Store in a dark fridge or freezer.  

##### 2. Working resazurin solution

First, determine the volume of resazurin required depending on the size of your organism and the container size. Here are some examples that we have used before. We recommend performing preliminary trials to ensure that a change in resazurin fluorescence can be detected over the time scale desired. This protocol was developed to detect a change in resazurin fluorescence within 5 hours in small seed (<7mm) and larger seed (10-30mm).  

- Small seed (<7mm length): trials conducted in 96 well plates (300uL volume in each well)
- Medium seed (15-40 mm length): trials conducted in small plastic cups (20 mL volume)
- Large seed/adults (>40 mm length): trials can be conducted in tripour cups, beakers, or plastic cups. Scale volume appropriately. The animals should be fully submerged. 

To prepare the working solution of resazurin, prepare the following. 

This recipe is to make 150 mL of working stock. To run a single 96 well plate, approximately 35 mL will be required (allowing for extra for re-do's or errors). For example, if we are running 4 total plates, we will need to prepare 4 x 35 mL = 150 mL of working solution. Increase if more is required.  

- 148 mL seawater (DI water with Instant Ocean adjusted to 23-25 ppt or filtered (<1um) seawater) 
- 333 µL resazurin stock solution as made above in step 1 
- 150 µL DMSO
- 1.5 mL antibiotic solution [100x Penn/Strep & 100x Fungizone](https://us.vwr.com/store/product/4648458/null) - this should be kept frozen in a dark freezer and thawed before use (thaw in the dark or cover with aluminum foil) 

Store at 4°C in dark fridge until use. We recommend making a fresh batch of working stock within 7 days of use.    

##### 3. Supplies 

- Bench top incubators 
- [Temperature loggers](https://www.onsetcomp.com/products/data-loggers/mx2203) to be placed in incubators at treatment conditions 
- Paper towels and bench paper/pads 
- Tweezers, transfer pipettes, and forceps 
- Dissecting microscope 
- Spectrophotometer plate reader that detects fluorescence (e.g., FLx800) and software
- Plate reader filters with excitation wavelength of 530 and emission wavelength of 590 (we are currently using an excitation 528 wavelength filter with a bandpass of 20 and an emission 590 wavelength filter with a bandpass of 20)  
- P1000 pipette
- Scale bar/ruler
- Camera/phone camera
- Plastic cups, beakers, plates, or other vessel for incubations
- 96 well plate (for taking readings, you will need this regardless of container type) 

Label plates with identifying number (e.g. "Plate 1", "Plate 2") or label cups with unique numbers/identifiers.    

#### Protocol

Conduct measurements at treatments desired. We typically conduct measurements at a control temperature and a high temperature each day. If multiple treatments are desired over multiple days, be sure to run a control treatment each day as reference. Ensure you account for tank effects or other batch effects by randomizing loading order, position in incubators, etc. 

For oysters, we recommend the following treatments: 

- For acute stress and survival testing: control temperature (10-20°C) and acute high temperature (40-44°C)
- For thermal performance testing: control temperature (10-20°C), 36°C, 38°C, 40°C, 42°C

#### Schedule 

Each day, the schedule will be as follows. Note that this schedule is written for a single person. If there are 2-3 people, the time frame for loading and assessing survival will be shorter than written here. 

08:00-09:00: Load plates with oysters, take size images, and load resazurin solution   
09:00: Time 0 measurement   
10:00: Time 1 measurement   
11:00: Time 2 measurement  
12:00: Time 3 measurement  
13:00: Time 4 measurement   
14:00: Time 5 measurement 
14:00-16:00: Survival assessments and clean up   

Note that it is critical to perform survival assessments so that you can analyze resazurin metabolic response for those that survive and those that die during the trials. If performing trials in 96 well plates or other small containers, we recommend performing survival assessment at the end of the incubation. If you are conducting trials in larger cups where you can see the animals without removing the resazurin solution, you can assess survival at each time point.  

#### Load and prepare samples  

Before starting, set the incubator at the desired temperature.  

1. Prepare animals for assays. Track the source tank, treatment, or other identifying information. 
2. Add animals into labeled plates or containers and placing them into the empty container.
3. Have at least n=6 empty wells/containers at each temperature to serve as blanks. 
4. Write the location of wells on a plate map if using plates. 
5. Allocate the animals either into their designated cup or onto the lid of the plate. 
6. Take images of each animal with a scale bar with their identifying information in the photograph. See an example below.  
7. Move the animals into their respective wells in the plate if you placed them on the lid for a photograph. 
8. Fill each well with the desired amount of resazurin working stock at ambient temperature using a microchannel pipette or graduated cylinder. 

An example of photograph for size measurements:  

![](https://github.com/AHuffmyer/ASH_Putnam_Lab_Notebook/blob/master/images/NotebookImages/oysters/polyic/20250310/20240310_plate1.jpeg?raw=true)  

#### Measurements 

1. Turn on the computer and plate reader. Open the plate reader software.
2. Create a new protocol that conducts end point measurements from the top of the plate using an excitation wavelength of 530 and emission wavelength of 590 nm. 
3. Name the protocol and save. This process may vary depending on your instrument.
4. Take a T0 initial measurement - this is critical! If using a 96-well plate with small animals, you can place the plate with the animals directly on the plate reader (do not have the lid on the plate). If you have animals in cups, take a small sample (250uL) of the resazurin liquid from each container, place into a 96-well plate, and then conduct the measurements. If you use this method, be sure to make a plate map of the location of the samples and identifying information. Conduct measurements for blanks and samples.  
5. Put the first plate on the loading platform. 
6. Collect and export readings as directed in the plate software. 
7. Save the file as: `YYYYMMDD_TemperatureTreatment_Plate#_T0.xlsx`. For example, `20250128_40C_Plate#_T3.xlsx`. 
8. Save the data to a flash drive and add to GitHub or data repository. Here is an example of our files at the [GitHub repository here](https://github.com/RobertsLab/polyIC-larvae/tree/main/data/resazurin/plate-files/). 
9. Record the time of the measurement.
10. Repeat for any remaining plates or treatments. 
11. Move the animals to the incubator at their respective temperatures and record the temperature in the incubators. 
12. Repeat at 1, 2, 3, 4, and 5 hours of incubation. A minimum incubation time is 4 hours with 5-6 hours as optional time points.  

Here is an example of the plate maps from our work.    

![](https://github.com/AHuffmyer/ASH_Putnam_Lab_Notebook/blob/master/images/NotebookImages/oysters/analysis/20250128/nb3.jpeg?raw=true)

#### Survival measurements 

1. Either each hour (if you can easily see the animals in larger cups) or at the end of the incubation (for animals in 96 well plates), conduct survival assessments. 
2. If using plates, prepare a plate map for recording the assessments - this is an easy method to keep track of the assessments. If you are not using plates, make a list of all samples with columns for recording survival at each time point.  
3. In the plate maps, you will record which wells have dead oysters. Use an "X" to mark wells with dead oysters. You can also record "dead" and "alive" in a list format. 
4. Start with high temperature plates. 
4. If working with shellfish, use tweezers/forceps to take each animal out and examine in a petri dish filled with DI water under a dissecting scope. Determine if the oyster is dead by placing the cup side of the oyster down and gently taping/moving the shell. If the shell is open and remains open after tapping, the oyster is dead. If the shell is closed tight or closes after tapping, the oyster is alive. Use other determination methods for other organisms. 
5. Record any notes of oysters that were damaged by the tweezers or record any other notes of interest. 
6. After examining each oyster, move it to a beaker. Discard oysters after the measurements are done. 
7. Repeat for all plates and samples. 
8. Discard of resazurin in the appropriate waste bin labeled for hazardous waste. Empty plates into a tripour and pour into a labeled waste container. 
9. Rise plates thoroughly in the sink and allow to dry for the next trial. Cups and materials can be re used.
10. Generate a data frame that has columns for sample ID, treatments, date, and other relevant information. Add a column designated "mortality" and add a 0 for alive and 1 for dead animals. See examples below.    

Here is an example of the data sheet in the notebook from our work.  
![](https://github.com/AHuffmyer/ASH_Putnam_Lab_Notebook/blob/master/images/NotebookImages/oysters/analysis/20250128/nb5.jpeg?raw=true)

#### Size measurements 

From the images, measure the size of the organism. For oysters, we often use maximum length (mm). Other measurements may be more appropriate for other organisms. This will be used to normalize resazurin measurements.  

Record size from measurements of images (e.g., using ImageJ) in a data frame. See examples below.  

#### Data preparation and analysis  

Prepare the following data frames (see examples at the links below): 

- Size measurements: columns for sample ID, date, treatment, and size measurement (e.g., length in mm)
- Mortality assessment: columns for sample ID, date, treatment, and mortality assessment (e.g., 0 for alive and 1 for dead)
- Metadata: columns for sample ID, date, treatment, tank or batch effects, species, well/cup ID, and sample type (i.e., "blank" or "sample") 
- Resazurin files: files exported from plate reader software that contain fluorescence readings for each well of the plate

Conduct the following analysis steps (see R scripts available for use below):  

- Read in data
- Normalize all fluorescence values to the initial time point (fluorescence at time X divided by fluorescence at time 0)
- Calculate the mean value for blanks within each batch (e.g., mean of all blanks in plate 1 at high temperature on day 1)
- Subtract the mean blank value from the fluorescence value of each sample from the respective batch
- Size normalize the data by dividing fluorescence values by size of each sample
- Proceed with visualization and statistical analyses, including testing for effects of treatment or other effects of interest and examining metabolic differences between animals that lived and animals that died during the trials. See examples in our GitHub repositories linked below. 

#### Data sheet and script examples  

Data will be stored on GitHub. Links are available below for examples.   

[Size image examples](https://github.com/RobertsLab/polyIC-larvae/tree/main/data/resazurin/images/)  
[Size data sheet example](https://github.com/RobertsLab/polyIC-larvae/blob/main/data/resazurin/size.csv)  
[Resazurin plate reader file examples](https://github.com/RobertsLab/polyIC-larvae/tree/main/data/resazurin/plate_files)  
[Resazurin plate metadata example](https://github.com/RobertsLab/polyIC-larvae/blob/main/data/resazurin/metadata/metadata.xlsx)  
[Survival data example](https://github.com/RobertsLab/polyIC-larvae/blob/main/data/resazurin/survival.csv)  

Small seed project example: Scripts for analysis are available on GitHub [here](https://github.com/RobertsLab/polyIC-larvae/blob/main/scripts/resazurin/resazurin-analysis.Rmd) and figures of results are [available here](https://github.com/RobertsLab/polyIC-larvae/tree/main/figures/resazurin).    

Large seed project example: Scripts for analysis are available on GitHub [here](https://github.com/RobertsLab/10K-seed-Cgigas/blob/main/scripts/resazurin.Rmd) and figures of results are [available here](https://github.com/RobertsLab/10K-seed-Cgigas/tree/main/figures/resazurin).   

## Aquarium nitrogen testing kit protocols (AQI test kit) 

Written by Noah Ozguner and Madeliene Baird 20250401.  

This protocol is written based on the [manufacturer's instructions](https://apifishcare.com/pdfs/products-us/saltwater-master-test-kit/api-saltwater-mastert-test-kit-instruction-manual.pdf). 

Test kit was [ordered here](https://www.amazon.com/API-MASTER-Aquarium-Water-1-Count/dp/B001D6Z7QW/ref=asc_df_B001D6Z7QW?mcid=f12e42d7505a391c8f7d47fcc7373e19&hvocijid=11467865304186403471-B001D6Z7QW-&hvexpln=73&tag=hyprod-20&linkCode=df0&hvadid=721245378154&hvpos=&hvnetw=g&hvrand=11467865304186403471&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9033456&hvtargid=pla-2281435179778&psc=1)

### Standard Operating Protocol (SOP)

After testing, do not pour contents back into the tank. Make sure to rinse test tubes after use. 

#### pH (kit minimum 7.4, maximum 8.8) 

- Fill a clean test tube with 5 ml of water 
- Add 5 drops of High range pH Test Solution
- Cap the test tube and invert it multiple times to mix the solution
- Read results by comparing the color of the solution to the provided pH color chart (in a relatively well lit area). The closest color match indicates the pH value of the water sample. 
- Thoroughly wash test tube after use

#### Ammonia (ppm or mg/L) [two bottles]

- Fill a clean test tube with 5 ml of water 
- Add 8 drops of Ammonia Test Solution 1
- Add 8 drops of Ammonia Test Solution 2
- Cap the test tube and shake vigorously for 5 seconds
- Wait 5 minutes for color to develop
- Read results by comparing the color of the solution to the provided Ammonia color chart. (in a relatively well lit area). The closest color match indicates the Ammonia value of the water sample. 
- Thoroughly wash test tube after use

#### Nitrite (ppm or mg/L)

- Fill a clean test tube with 5mL of water
- Add 5 drops of Nitrite Test Solution
- Cap the test tube and shake for 5 seconds
- Wait 5 minutes for color to develop
- Compare the color of the solution to the Nitrite Color Chart in a well lit area. The closest match will indicate the ppm (mg/L) of the nitrite in the sample
- Thoroughly wash test tube after use

#### Nitrate (ppm or mg/L) [two bottles]
- Fill a clean test tube with 5mL of water
- Add 10 drops of Nitrate Test Solution #1
- Cap the test tube and invert several times to mix the solution
- Vigorously shake the Nitrate Test Solution #2 for at least 30 seconds
- Add 10 drops of Nitrate Test Solution #2
- Cap the test tube and shake vigorously for 1 minute
- Wait 5 minutes for the color to develop
- Compare the color of the solution to the Nitrate Color Chart in a well lit area. The closest match will indicate the ppm (mg/L) of the nitrite in the sample
- Thoroughly wash test tube after use

#### Reference values 

Ammonia (NH3): Ammonia is highly toxic to fish and should always be 0 ppm.  

Nitrite (NO2): Nitrite is also toxic and should be 0 ppm.  

Nitrate (NO3): While less toxic than ammonia and nitrite, nitrate can still be harmful to fish and corals at high levels. Aim to keep nitrate levels below 20 ppm, and ideally between 0-5 ppm.  










