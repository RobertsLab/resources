#Bisulfite Sequencing PROTOCOL 
>  
>


* Extract DNA - DNAzol or Qiagen Plate format are what is commonly used.

>
>



* Check Quantity and Quality


> 
 
----


###MBD precipitation (optional)
Invitrogen - [MethylMiner Methylated DNA Enrichment Kit](http://www.lifetechnologies.com/order/catalog/product/ME10025) (ME10025) - [user guide](https://tools.lifetechnologies.com/content/sfs/manuals/methylminer_man.pdf)

_Before starting, DNA should be fragmented to an average size of less than 1,000bp (typically aim for a length of 500bp). To determine size distribution of DNA gel eletrophoresis can be performed._ 


>Claire sheared DNA
>
>Sam ran ~250ng (out of 3000ng, according to Claire) of LSU C.gigas oil spill gDNA on a gel that was previously sheared by >Claire to verify that shearing was successful.
>
>Ran unsheared side-by-side with sheared gDNA for comparison.
>
>Note: HB16 and NB3 did not have any unsheared gDNA left in their tubes, so nothing was run on a gel.
>
>Ladder used: O'GeneRuler 100bp Ladder (ThermoFisher)
>
><img src="http://eagle.fish.washington.edu/Arabidopsis/20141125_-_LSU_Claire_Sheared.png" width="600px" height="300px" />
>
>
>Well, it's rather obvious that the initial shearing did NOT work. Will re-shear the samples.
>
>Looking at the Biorupter (Diagenode) manual, it turns out that shearing samples in a 1.5mL tube (in which these were sheared) requires a minimum volume of 100uL. All the samples were far below this minimum volume. Additionally, the recommendations in the manual to reach the target size range are significantly longer (30 - 40 cycles) than what was applied (4 cycles). The combination of these two factors are likely the reason that shearing didn't take place.
>
>
>
Used the remainder of the "sheared" samples (~2750ng). Brought the volumes up to 80uL and transferred to 0.5mL snap cap tubes. The volume of 80uL was selected because it's above the minimum volume required for shearing in 0.5mL tubes (10uL according to the Biorupter 300 manual) and the MethylMiner Kit (Invitrogen) requires the input DNA volume to be <= 80uL.
>
DNA was sheared with the following parameters (based on recommendations in the Bioruptor 300 (Diagenode) manual:
>
Low power
>
30 cycles of:
>
30s on
>
30s off
>
>Target average fragment size is ~350bp.
>
>Ran ~250ng of sheared C.gigas gDNA from the above shearing on a 1xTAE 1%agarose + EtBr gel
>
>Ladder used: O'GeneRuler 100bp Ladder (ThermoFisher)


><img src="http://eagle.fish.washington.edu/Arabidopsis/20141126_-_Sheared_Oil_Spill_gDNA.png" width="600px" height="600px"/>

>The shearing is, surprisingly, very inconsistent across the samples. The target average fragment size was ~350bp. However, most of these samples are <250bp.
>


_Resuspend Dynabeads_ 
- Gently pipette Dynabeads up and down and avoid air bubble. Gently inverte the tube.



_Remove liquid from Dynabeads_
- Place the microcentrifuge tube containing the beads in a magnetic rack and allow it to stand for at least 1 minute. During this time, the beads will concentrate as a pellet along the inner surface of the tube wall. Open the microcentrifuge tube without displacing it from the rack or disturbing the bead pellet and carefully extract the liquid volume with a pipette tip without touching the bead pellet. After the liquid has been removed, remove the tube from the rack and quickly and gently resuspend the beads with the volume of appropriate  solution. Do not allow the beads dry out. Add the next solution within 1 minute. 



_Bead volume_
- For each ug of DNA use 10ul of Dynabeads M-280 Streptavidin and 3.5 ug (7 ul) of MBD-Biotin Protein.



_Prepare 1x Bind/Wash Buffer_
- Prepare 1X Bind/Wash Buffer by diluting 1 part of 5X Bind/Wash Buffer with 
4 parts of DNase-free water. For example, for each 5 ng–1 μg capture reaction, prepare 1.8 ml of 1X Bind/Wash Buffer by diluting 360 μl of 5X Bind/Wash Buffer with 1.44 ml of DNase-free water. Read through the entire protocol and then scale accordingly depending on the number and size of your capture reactions.


_Initial Bead Wash_ 
- In this step, you wash the Dynabeads M-280 Streptavidin prior to coupling them with the MBD-Biotin Protein. 
- Resuspend the stock of Dynabeads M-280 Streptavidin by gently pipetting up and down to obtain a homogenous suspension. Never mix the beads by vortexing.
- For each microgram (μg) of input DNA, add 10 μl of beads to a 1.7-ml DNase-free microcentrifuge tube. For input amounts of 5 ng to 1 μg, add 10 μl of beads. 
- For bead volumes <100 μl: Bring the volume up to 100 μl with 1X Bind/Wash Buffer. Mix by gentle pipetting; do not mix by vortexing. For bead volumes >100 μl: Proceed to Step 4. 
- Place the tube(s) on a magnetic rack for 1 minute to concentrate all of the beads on the inner wall of the tube. 
- With the tube in place on the magnetic rack, remove the liquid with a pipette without touching the beads with the pipette tip. Discard the liquid. 
- Remove the tube from the magnetic rack. 
- Add an equal volume (100–250 μl) of 1X Bind/Wash Buffer to the beads and resuspend by pipetting gently up and down.
- Repeat Steps 4–7 once more.



_Coupling the MBD-Biotin Protein to the Beads_
- In this step, you couple the Dynabeads M-280 Streptavidin with the MBDBiotin Protein. Do not add DNA in this step. 
- For each microgram (μg) of input DNA, add 7 μl (3.5 μg) of MBD-Biotin Protein to a 1.7-ml DNase-free microcentrifuge tube. For input DNA amounts less than 1 μg, use 7 μl of MBD-Biotin Protein. 
- If starting with ≤1 μg of input DNA: Add 1X Bind/Wash Buffer to the protein to a final volume of 100 μl. If starting with >1 μg–10 μg of input DNA: Add 1X Bind/Wash Buffer to the protein to a final volume of 200 μl. If starting with >10 μg–25 μg of input DNA: Add 1X Bind/Wash Buffer to the protein to a final volume of 500 μl. 
- Transfer the diluted MBD-Biotin Protein to the tube of resuspended beads from Step 8, Initial Bead Wash, previous page (total volume = 200–750 μl). 
- Mix the bead-protein mixture on a rotating mixer at room temperature for 1 hour.



_Wash the MBD-beads_
- After mixing the beads and protein for 1 hour, follow the steps below to wash the coupled MBD-beads: 
- Place the tube containing the MBD-beads on a magnetic rack for 1 minute to concentrate the beads on the inner wall of the tube. 
- With the tube in place on the magnetic rack, remove the liquid with a pipette without touching the beads with the pipette tip, and discard the liquid. Always avoid touching the beads with the pipette tip.
- Resuspend the beads with 100–250 μl of 1X Bind/Wash Buffer (the same volume used in Initial Bead Wash, Step 7). 
- Mix the beads on a rotating mixer at room temperature for 5 minutes. 
- Repeat steps 1–4 two more times. 
- Place the tube on the magnetic rack for 1 minute to concentrate all of the beads on the inner wall of the tube. 
- With the tube in place on the magnetic rack, remove the liquid with a pipette and discard the liquid. 
- Resuspend the beads in the same volume of 1X Bind/Wash Buffer as used above in Step 3. 
The beads are now ready for methylated DNA capture.



_Capture Reaction 5ng-1ug Input DNA_ 
- To a clean 1.7-ml DNase-free microcentrifuge tube, add 20 μl of 5X Wash/Bind Buffer. (Note: Be sure to use 5X buffer in this step, not 1X buffer.) 
- Add 5 ng–1 μg of fragmented sample DNA to the tube (added volume should be ≤ 80 μl). 
- Bring the final volume to 100 μl with DNase-free water. 
- Transfer the DNA/Buffer mixture to the tube containing the MBD-beads (from Wash the MBD-beads, Step 8). 
- Mix the MBD-beads with the DNA on a rotating mixer for 1 hour at room temperature (alternatively, you can mix overnight at 4ºC). If you will be eluting in a stepwise gradient of increasing NaCl concentration, prepare the buffers while the beads are mixing by proceeding to Preparing Buffers for a Step-wise Elution Series. Otherwise, continue to Removing the Non-Captured DNA.

_OR_

_Capture Reaction >1ug-10ug Input DNA_ 
- To a clean 1.7-ml DNase-free microcentrifuge tube, add 100 μl of 5X Wash/Bind Buffer. (Note: Be sure to use 5X buffer in this step, not 1X buffer.) 
- Add >1–10 μg of fragmented sample DNA at a concentration of 25 ng/μl to the tube (added volume will be 40–400 μl). 
- Bring the final volume to 500 μl with DNase-free water. 
- Transfer the DNA/buffer mixture to the tube containing the MBD-beads (from Wash the MBD-beads, Step 8). 
- Mix the MBD-beads with the DNA on a rotating mixer for 1 hour at room temperature (alternatively, you can mix overnight at 4ºC). If you will be eluting in a stepwise gradient of increasing NaCl concentration, prepare the buffers while the beads are mixing by proceeding to Preparing Buffers for a Step-wise Elution Series, page 20. Otherwise, continue to Removing the Non-Captured DNA.



_Control Caputure Reaction with 1ug of K-562 DNA_
- The following control reaction uses 1 μg of K-562 DNA, supplied in the kit. Note that the K-562 DNA is already fragmented. 
- To a clean 1.7-ml DNase-free microcentrifuge tube, add 20 μl of 5X Wash/Bind Buffer. (Note: Be sure to use 5X buffer in this step, not 1X buffer.) 
- Thaw and briefly vortex the K-562 DNA (50 μg/ml) provided in the kit, and add 20 μl (1 μg) to the tube. 
- Add 1 μl of the diluted Methylated DNA control (10 pg/μl) and 1 μl of the diluted Non-Methylated DNA control (10 pg/μl) to the tube. 
- Bring the final volume to 100 μl with DNase-free water 
- Transfer the DNA mixture to the tube containing the MBD-beads (from Wash the MBD-beads, Step 8). 
- Mix the MBD-beads with the DNA on a rotating mixer for 1 hour at room temperature (alternatively, you can mix overnight at 4ºC). If you will be eluting in a stepwise gradient of increasing NaCl concentration, prepare the buffers while the beads are mixing by proceeding to Preparing Buffers for a Step-wise Elution Series, next page. Otherwise, continue to Removing the Non-Captured DNA. 



_Removing Non-Captured DNA from the Beads_
- After mixing the DNA and MBD-beads (Methylated DNA Capture), place the tube on the magnetic rack for 1 minute to concentrate all of the beads on the inner wall of the tube. 
- With the tube in place on the magnetic rack, remove the supernatant liquid with a pipette without touching the beads with the pipette tip, and save it in a clean DNase-free microcentrifuge tube. This saved supernatant is the non-captured DNA supernatant fraction. Store this sample on ice. 
- Add 200 μl of 1X Bind/Wash Buffer to the beads to wash the beads of residual non-captured DNA. 
- Mix the beads on a rotating mixer for 3 minutes. 
- Place the tube on the magnetic rack for 1 minute to concentrate all of the beads on the inner wall of the tube. 
- With the tube in place on the magnetic rack, remove the liquid with a pipette without touching the beads with the pipette tip, and save it in a clean DNase-free microcentrifuge tube. This saved liquid is a noncaptured DNA wash fraction. Store this sample on ice. 
- For capture reactions of ≤1 μg of input DNA: Repeat steps 3–6 once more to obtain two wash fractions in total. Store each sample on ice. For capture reactions of >1 μg – 25 μg input DNA: Repeat steps 3–6 three 
more times to obtain four wash fractions in total. Store each sample on ice. Important: After collecting the final wash fraction, immediately proceed to Eluting the Captured DNA, and resuspend the beads in elution buffer to prevent the beads from drying out. Pool the first and second wash fractions together and label “Wash A”. If applicable, pool the third and fourth wash fractions and label “Wash B”. Note:Pooling the wash fractions is not mandatory, but is suggested as a matter of convenience prior to ethanol precipitation.



_Single Fraction Elution with 2000 mM NaCl_
- Immediately after removing the non-captured DNA from the beads (Removing Non-Captured DNA from the Beads, Step 7), follow the protocol below to elute the captured DNA as a single fraction using the High-Salt Elution Buffer. 
- For ≤1 μg of input DNA: Resuspend the beads in 200 μl of the High-Salt Elution Buffer (2000 mM NaCl) provided in the kit. For >1 μg–25 μg of input DNA: Resuspend the beads in 400 μl of the HighSalt Elution Buffer (2000 mM NaCl) provided in the kit. 
- Incubate the beads on a rotating mixer for 3 minutes. 
- Place the tube on the magnetic rack for 1 minute to concentrate all of the beads on the inner wall of the tube. 
- With the tube in place on the magnetic rack, remove the liquid with a pipette without touching the beads with the pipette tip, and save it in a clean DNase-free microcentrifuge tube. Store this sample on ice. 
- For ≤1 μg of input DNA: Repeat Steps 1–4 once, collecting the second sample in a different tube. Pool these two elution samples (the total volume will be 400 μl). Store the pooled sample on ice. For >1 μg–25 μg of input DNA: Repeat Steps 1–4 twice, collecting each sample in a different tube. This ensures complete (>95%) elution of the DNA that can be eluted at this ionic strength. Store each sample on ice. Proceed to Ethanol Precipitation.
 


_DNA Cleanup and Concentration by Ethanol Precipitation_
- To each non-captured, wash, and elution fraction from the previous steps, add the following components: 
• 1 μl Glycogen (20 μg/μl) (included in kit) 
• 1/10th sample volume of 3 M sodium acetate, pH 5.2 (e.g., 40 μl per 400 μl of sample) 
• 2 sample volumes of 100% ethanol (e.g., 800 μl per 400 μl of sample) 
- Mix well and incubate at –80°C for at least 2 hours. 
- Centrifuge the tube for 15 minutes ≥12,000 × g at 4°C or room temperature. 
- Carefully discard the supernatant without disturbing the pellet. 
- Add 500 μl of cold 70% ethanol. 
- Centrifuge the tube for 5 minutes ≥12,000 × g at 4°C or room temperature. 
- Carefully discard the supernatant without disturbing the pellet. 
- Repeat Steps 6–7 once and remove any remaining residual supernatant. 
- Air-dry the pellet for ~5 minutes (do not completely dry the pellet). 
- Resuspend the DNA pellet in 60 μl of DNase-free water (or other appropriate volume of buffer or water as needed for specific downstream applications). 
- Place the DNA on ice and proceed to any desired downstream applications, or store the DNA at –20°C or below until further use. 


---   

###Bisulfite conversion
Epigentek - [Methylamp DNA Modification Kit](http://www.epigentek.com/catalog/methylamp-dna-modification-kit-p-28.html) (P-1001-1) - [user guide](http://www.epigentek.com/docs/P-1001.pdf)

![ov](http://eagle.fish.washington.edu/cnidarian/skitch/www_epigentek_com_docs_P-1001_pdf_1A07DDD8.png)  


_Before starting, add 7 ml (for P-1001-1) or 15 ml (for P-1001-2) of 100% Ethanol to R5 to make the final cleaning buffer. Prepare the 90% Ethanol._ 


- Add DNA sample and distilled water into a vial with total volume of 24 µl and mix well. Add 1 µl of R1 to the above sample. Mix well and incubate the sample at 37°C for 10 minutes.



- Add 1.1 ml of R3 to 1 vial of R2. Vortex until solution is clear or saturated (about 2 minutes). Add 40 µl of R1 to the solution, lightly vortex.



- Add 125 µl of this mixed R1/R2/R3 solution to the sample. Vortex and incubate at 65°C for 90 minutes.



- Place a spin column into a 2 ml collection tube. Add 300 µl of R4 to the sample; mix, and transfer to the column. Centrifuge at 12,000 rpm for 15 seconds. Remove the column from the collection tube and discard the flowthrough. Replace column to the collection tube.


- Add 200 µl of R5 solution (final cleaning buffer) to the column, and centrifuge at 12,000 rpm for 15 seconds.


- Add 10 µl of R1 to 1.1 ml of 90% ethanol, and mix. Add 50 µl of the mixed R1/ethanol solution to the column; let it sit for 8 minutes at room temperature, then centrifuge at 12,000 rpm for 15 seconds.

- Add 200 µl of 90% ethanol to the column, centrifuge at 12,000 rpm for 15 seconds. Remove the column from the collection tube and discard the flowthrough. Replace the column to the collection tube. Add 200 µl of 90% ethanol to the column again and centrifuge at 12,000 rpm for 35 seconds.


- Place the column in a new 1.5 ml vial. Add 8-18 µl of R6 directly to the column filter, and centrifuge at 12,000 rpm for 20 seconds to elute modified DNA. 


_Modified DNA is now ready for methylation amplification or storage at –20°C for up to 2 months._

---

