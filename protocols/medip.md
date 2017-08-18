### <a name="medip"></a>MeDIP (Methylated DNA Immunoprecipitation)
#### Standard Operating Protocol (SOP)
Written 20130513 by Sam White

Adapted from:

http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2763296/

http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0013100

##### Reagents:
- DNAzol (Molecular Research Center) [(SOP)](https://github.com/sr320/LabDocs/wiki/Chemical-Standard-Operating-Protocols-(SOP)#dnazol)
- TE [(SOP)]()
- Ice cold 100% ethanol [(SOP)](https://github.com/sr320/LabDocs/wiki/Chemical-Standard-Operating-Protocols-(SOP)#ethanol)
- 70% ethanol [(SOP)](https://github.com/sr320/LabDocs/wiki/Chemical-Standard-Operating-Protocols-(SOP)#ethanol)
- phenol:chloroform:IAA (25:24:1) [(SOP)](https://github.com/sr320/LabDocs/wiki/Chemical-Standard-Operating-Protocols-(SOP)#phenol_chloroform_IAA)
- 5x MeDIP Buffer (50mM Na2HPO4, 700mM NaCl, 0.25% Triton-X 100)
- anti-methyl cytidine antibody (Diagenode; 5-mC monoclonal antibody cl. b)
- Protein A/G Plus Agarose beads (Santa Cruz Biotech)
- 3M sodium acetate (pH = 5.2)
- MeDIP Digestion Buffer (50mM Tris-HCl, pH=8.0, 10mM EDTA, pH=8.0, 0.5% SDS)
- Proteinase K [(SOP)](https://github.com/sr320/LabDocs/wiki/Chemical-Standard-Operating-Protocols-(SOP)#proteinase_k)

##### Personal Protective Equipment (PPE):
- Gloves

##### Equipment:
- Refrigerated microfuge
- Room temp microfuge
- Sonicator


#### Procedure
##### Total Time: 3 days
##### Cost/sample:

Notes:
- Both MeDIP Buffers should be made up from liquid stocks of each individual component, as each individual component are common molecular biology stock reagents that all lab members should have at their benches. Do NOT attempt to make the MeDIP Buffers by weighing out and dissolving powdered chemicals for each individual component; it cannot be done accurately with the small quantities required.

- This is a multi-day procedure. Read through the protocol thoroughly to plan your time properly.

- Isolate gDNA according to DNAzol protocol (Molecular Research Center), but resuspend final DNA pellet in TE or H2O. (Initial incubation with Proteinase K is dependent on tissue type and available time to perform procedure.)

- Quantify gDNA yield and quality. Procedure requires a minimum of 6ug, but more can't hurt.

DAY 1

1. Fragment gDNA with sonicator to a target size of 500bp.
2. Run 250ng of fragmented on an 2% agarose gel to verify successful fragmentation. Additionally, the fragmentation should be verified/quantified on an Agilent Bioanalyzer, if possible.

  If fragmentation is successful, proceed to Step 3.

3. Bring fragmented gDNA sample to a volume of 350uL with TE.
4. Heat sample at 95C, 10mins and immediately place on ice for 5mins.
5. Add 100uL of 5x MeDIP Buffer (50mM Na2HPO4, 700mM NaCl, 0.25% Triton-X 100), 45uL of TE, and 5uL (5ug) of anti-methyl cytidine antibody (Diagenode; 5-mC monoclonal antibody cl. b). Incubate O/N, @ 4C, rotating end-over-end.

DAY 2

1. Wash appropriate volume of Protein A/G Plus Agarose beads (Santa Cruz Biotech; need 20uL per sample) with 1x MeDIP Buffer. 
  1. Mix stock Protein A/G Plus Agarose beads well and transfer needed volume to clean tube. Pellet beads by spinning 1000g, 2mins, 4C. Discard supernatant. Resuspend beads in 1mL of 1x MeDIP Digestion Buffer. Repeat one time. Final resuspension in 1x MeDIP Buffer. Final resuspension volume is 40uL per sample. Add 40uL of resuspended Protein A/G Plus Agarose beads to each sample and continue incubation with end-over-end rotation @ 4C for 2hrs.
2. Pellet the Protein A/G beads 1000g, 2mins, 4C.
3. Remove and retain supernatant (to retain unmethylated DNA).
4. Wash beads with 1mL 1x MeDIP Digestion Buffer (50mM Tris-HCl, pH=8.0, 10mM EDTA, pH=8.0, 0.5% SDS) a total of three times. Save supernatant after each wash in its own tube (this will simplify DNA precipitation later on).
5. Resuspend beads in 250uL MeDIP Digestion Buffer.
6. Add 70ug of Proteinase K and incubate 24hrs @ RT with end-over-end rotation.
*Note*: The source protocols say to incubate the Proteinase K digest @ 55C. However, we don't have a means to do so, since we need a rotator to keep the agarose beads in suspension. According to various sources, Proteinase K retains >80% of it's enzymatic activity between 20C - 50C. So, allow the digest to run longer (24hrs) than recommended (O/N).

DAY 3

1. Add a volume of phenol:chloroform:IAA (25:24:1) equal to your sample volume, vortex thoroughly, and spin 16,000g, 10mins, RT.
2. Transfer aqueous phase to clean tube. If sample had cloudy interphase repeat Step 1 until interphase is no longer cloudy.
3. Precipitate your various DNAs. 
  1. Add 1/10th volume of 3M sodium acetate (pH = 5.2), 2.5 volumes of ice cold 100% ethanol, mix thoroughly, and incubate @ -20C for at least 20mins. Note: If expecting low yields, addition of 20ug of glycogen can help improve recovery.
4. Pellet DNA by spinning samples at 16,000g, 20mins, 4C.
5. Discard supernatant and wash pellet with 1000uL 70% EtOH.
6. Re-pellet DNA by spinning samples at 16,000g, 20mins, 4C.
7. Discard supernatant, pulse spin, remove residual supernatant, and briefly air dry pellet for 5mins at RT.
8. Resuspend methylated DNA in 50uL TE. Resuspend each unmethylated DNA fraction in 25uL and then pool.
9. Quantify DNAs.
