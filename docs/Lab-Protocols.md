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



