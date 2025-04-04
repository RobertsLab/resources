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