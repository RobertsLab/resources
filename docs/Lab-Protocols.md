Protocols for benchwork in the lab (e.g. RNA isolation), for commonly used instruments and software (e.g. proteomics data analysis in Skyline), and for commonly performed hatchery practices and tissue sampling.

Foundational protocols can be found [here](https://github.com/RobertsLab/resources/tree/master/protocols). As they become prominent, they will be migrated here for posterity.

## RNA Extraction 
  We often use MRC RNA-zol RT ([protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/MRC_RNAzol-RT-march-2017.pdf)). Depending on downstream needs we might engage in DNAase treatment. 

---

## Reverse Transcription

### <a name="reverse_transcription"></a>Reverse Transcription
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
- 0.5mL snap-cap microfuge tubes ([Genesee: 22-178A](https://geneseesci.com/shop-online/product-details/923/?product=22-178A))
- Sterile 1.7mL snap-cap microfuge tubes ([Genesee: 22-281S](https://geneseesci.com/shop-online/product-details/?product=22-281S))
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



