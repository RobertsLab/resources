# Glycogen-Glo Assay Protocol

## Standard Operating Protocol (SOP)
Written 20260115 by Sam White.

## Overview
The Glycogen-Glo Assay (Promega) is a luminescence-based assay used to quantify glycogen content in tissue samples. The assay converts glycogen to glucose using glucoamylase, then measures the resulting glucose through a luminescent glucose detection reaction. This protocol is optimized for use with marine invertebrate tissue (specifically _Magallana gigas_ ctenidia), but can be adapted for other tissue types.

## Reagents:

- Glycogen-Glo Assay Kit ([Promega](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/Promega_Glycogen_Glo_Assay.pdf)) containing:
    - Glucoamylase Buffer
    - Glucoamylase
    - Luciferin Detection Solution
    - Glycogen Standard (20 µg/µL)
    - Glucose Standard (100 mM)
    - 0.3N HCl
    - TRIS Buffer
- PBS (Phosphate Buffered Saline)
- 0.5mm glass beads
- DNase-free H₂O (NanoPure H₂O)

### Specific Hazards:

- 0.3N HCl is corrosive.
- Glass beads can be hazardous if inhaled.
- Dry ice and liquid nitrogen are cryogenic materials and can cause frostbite. Use caution when handling and wear appropriate gloves and eye protection (liquid nitrogen).
- The Bullet Blender is loud and can cause hearing damage if used without ear protection for extended periods.

### Personal Protective Equipment (PPE):

**REQUIRED:**

- Gloves
- Lab coat

**OPTIONAL:**

- Eye protection (when handling HCl)
- Ear protection (when using Bullet Blender for extended periods)

### Equipment:

- Pipettes (1-1000µL)
- Filtered pipette tips
- 1.5mL Safe-Lock snap-cap microfuge tubes ([Qiagen](https://www.qiagen.com/us/products/discovery-and-translational-research/lab-essentials/tubes/safe-lock-microcentrifuge-tubes-15-ml))
- 96-well white, opaque, flat-bottom plate (e.g., Costar)
- Bullet Blender 5E Gold+ with 1.5mL tube adapters (or equivalent homogenizer)
- Dry ice (for pre-cooling Bullet Blender)
- Repeater pipette (optional, e.g., Eppendorf Repeater M4)
- Plate reader capable of luminescence detection (e.g., Synergy HTX)
- Vortex mixer
- Microcentrifuge
- Aluminum foil
- Ice bucket

## Procedure

### Total Time: ~3.5-4.5 hours

---

## Part 1: Tissue Collection and Homogenization


1. Read the [manufacturer's protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/Promega_Glycogen_Glo_Assay.pdf) (PDF).
2. Read _this_ protocol.
3. Verify sufficient quantities of reagents and samples before beginning.
4. Wear clean gloves and lab coat.

### A. Homogenization Buffer Preparation

**Per sample:**

- 500µL PBS
- 250µL 0.3N HCl
- ~300µL 0.5mm glass beads

**Preparation:**

1. Calculate total number of samples needed.
2. Prepare a master mix of PBS and 0.3N HCl (in a 2:1 ratio) with 10% extra to account for pipetting error.
3. Mix master mix thoroughly.
4. Add ~300µL of 0.5mm glass beads to each pre-labeled 1.5mL Safe-Lock tube.
5. Distribute 750µL of master mix to each tube containing beads.

### B. Tissue Sample Preparation

1. Collect tissue samples and record weights to the nearest milligram.
   - **Recommended range:** 5-20 mg per sample for _M. gigas_ ctenidia
   - Samples can be diluted if needed; larger initial tissue amounts provide more flexibility
2. Place tissues in pre-labeled 1.5mL Safe-Lock tubes containing homogenization buffer and beads.

### C. Homogenization

1. Pre-cool Bullet Blender with dry ice (~2.5 lbs).
2. Add tissue samples to tubes containing homogenization buffer and beads.
3. Load tubes into 1.5mL tube adapters in Bullet Blender.
4. Balance tubes by placing them equally spaced across from each other.
5. Homogenize at Speed 12 for 4 minutes.
6. Remove tubes from Bullet Blender.
7. Add 250µL of TRIS Buffer to each tube to neutralize pH.
8. Vortex thoroughly for 10-15 seconds.
9. Store samples on ice until ready to assay, or at -20°C for future use.

---

## Part 2: Sample Preparation for Assay

### A. Sample Preparation

1. Thaw samples on ice if frozen.
2. Vortex samples thoroughly for 10-15 seconds to resuspend any settled material.
3. Centrifuge samples at ≥10,000 × g for 2 minutes to pellet insoluble debris.

**CRITICAL:** Always pellet insoluble material and use only the supernatant for pipetting to ensure accurate measurements.

### B. Sample Dilution (if necessary)

**Recommended tissue equivalent per well:** ~0.025 mg to ~20 mg (based on empirical testing with _M. gigas_ ctenidia).

**NOTE:** [Initial testing showed that tissue equivalents in this range fall within the linear range of the glycogen standard curve](https://robertslab.github.io/sams-notebook/posts/2026/2026-01-12-Glycogen-Assay---Glycogen-Glo-Dilution-Testing-with-M.gigas-Ctenidia-Homogenate/)(notebook entry). The theoretical minimum detection limit is approximately 0.0011 mg, while the maximum before dilution is needed is approximately 20mg. However, practical working ranges may vary depending on glycogen content of specific tissues.

For samples outside this range:

1. Prepare dilution buffer (2:1:1 mixture of PBS : 0.3N HCl : TRIS Buffer).
2. Perform dilution to fall within equivalent tissue range.
3. Keep dilutions on ice.

---

## Part 3: Assay Setup

### A. Reagent Preparation

**NOTE:** Kit components have been aliquoted into ~25 reaction volumes to minimize freeze/thaw cycles (≤3 cycles recommended). Aliquots are stored as follows:

- **Reductase:** -80°C freezer (middle), bottom shelf
- **All other components (except standards):** -20°C freezer in FTR 209, in dedicated boxes
- **Glycogen and Glucose standards:** -20°C freezer in original Glycogen-Glo kit box

**CAUTION:** Aliquot tubes are not labeled. Be careful not to mix up components when removing from storage.

1. Thaw all kit reagents according to manufacturer's instructions.
2. After thawing:
   - Keep Glucoamylase Buffer and Luciferin Detection Solution at room temperature
   - Keep all other components on ice.
3. Calculate total volume of Glucoamylase Digestion Solution needed:
   - Count total wells requiring glucoamylase enzyme (samples + glycogen standards, each in triplicate)
   - Each well requires 25µL
   - Add 10% extra to account for pipetting error
   - Example: (10 samples × 3 replicates + 5 glycogen standards × 3 replicates) × 25µL × 1.1 = 1,237.5µL
4. Prepare Glucoamylase Digestion Solution by mixing:
   - Glucoamylase
   - Glucoamylase Buffer
   
   (Follow manufacturer's ratio recommendations for calculated volume)

### B. Standard Curve Preparation

**Glycogen Standard Curve (in triplicate):**

- 20 µg/µL
- 2 µg/µL
- 0.2 µg/µL
- 0.02 µg/µL
- 0 µg/µL (blank)

Perform 1:10 dilutions: 10µL standard in 90µL dilution buffer.

**Glucose Standard Curve (in triplicate - OPTIONAL):**

- 100 µM
- 10 µM
- 1 µM
- 0.1 µM
- 0 µM (blank)

Perform 1:10 dilutions: 10µL standard in 90µL dilution buffer.

**NOTE:** [Initial testing suggests glucose levels in ctenidia tissue are below detection limits](https://robertslab.github.io/sams-notebook/posts/2026/2026-01-12-Glycogen-Assay---Glycogen-Glo-Dilution-Testing-with-M.gigas-Ctenidia-Homogenate/)(notebook entry), so glucose measurements may be skipped for these samples. However, glucose background should be assessed when working with new tissue types.

### C. Plate Setup

1. Plan plate layout to include:

   - Sample replicates (duplicates or triplicates recommended)
   - Glycogen standard curve (triplicate)
   - Glucose standard curve (triplicate, if needed)
   - Blanks (buffer only)

2. Label plate map clearly.

---

## Part 4: Assay Execution

### A. Initial Loading and Incubation

1. Add 25µL of sample or standard to designated wells.
2. For GLYCOGEN measurements:

   - Add 25µL of Glucoamylase Digestion Solution

3. For GLUCOSE measurements (optional):

   - Add 25µL of Glucoamylase Buffer only (no glucoamylase enzyme)

4. For blanks:

   - Add 25µL of dilution buffer, then 25µL of appropriate buffer (with or without enzyme)

5. Cover plate loosely with aluminum foil to prevent light exposure and contamination.
6. Gently shake plate by hand for 60 seconds.
7. Incubate at room temperature for 1 hour.

### B. Detection Reaction

1. Prepare glucose detection reagent immediately before use:

   - Calculate total volume needed: count ALL wells (samples + standards + blanks)
   - Each well requires 50µL
   - Add 10% extra to account for pipetting error
   - Example: 50 total wells × 50µL × 1.1 = 2,750µL
   - Mix Luciferin glucose detection reagent gently by inversion five times.

2. Add 50µL of glucose detection reagent to ALL wells.

   - Use repeater pipette for consistency if available
3. Cover plate loosely with aluminum foil.
4. Gently shake plate by hand for 60 seconds.
5. Incubate at room temperature for 1 hour.

### C. Luminescence Reading

1. After incubation, read luminescence on plate reader.

   - Integration time: 1 second per well
   - No filters needed

2. Export raw luminescence data for analysis.


---

## Data Analysis

### Quality Control

1. Check standard curve linearity (R² ≥ 0.95 recommended).
2. Verify replicate consistency (CV% < 15% recommended).
3. Ensure blank readings are low and consistent.

### Calculations

1. Generate standard curve using linear regression:

   - Plot luminescence (y-axis) vs. glycogen concentration (x-axis)
   - Calculate slope and intercept

2. Calculate sample concentrations from luminescence values:

   - Concentration = (Luminescence - Intercept) / Slope

3. If glucose was measured, subtract glucose values from total to obtain glycogen-specific values.

4. Calculate final glycogen content accounting for:

   - Dilution factors
   - Original tissue weight
   - Homogenization buffer volume

---

## Storage and Waste Disposal

### Sample Storage

- Homogenized samples: -20°C for up to several months
- Diluted samples: Use fresh; do not store

### Reagent Storage

- Follow manufacturer's storage recommendations
- Most reagents stable at -20°C
- Thawed reagents: Use immediately or store as directed

### Waste Disposal

- Dispose of tips in broken glass waste.
- Dispose of liquid waste containing HCl according to institutional chemical waste procedures.
- Plates should be washed, dried and reused.

---

## References

- [Promega Glycogen-Glo Assay Protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/Promega_Glycogen_Glo_Assay.pdf) (PDF)
- [Bullet Blender Protocol](protocol-bullet_blender.md)

## Version History

- v1.0 (20260115): Initial protocol development based on optimization with _Magallana gigas_ ctenidia tissue.
