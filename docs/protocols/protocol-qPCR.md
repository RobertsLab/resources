# qPCR

Quantitative (real-time) PCR is one of the most-used techniques in the lab, usually for measuring gene expression from cDNA (see [Reverse Transcription](protocol-reverse_transcription.md)). This page has four parts:

1. **[Principles](#part-1-how-qpcr-works)**: how qPCR works, SYBR Green/EvaGreen versus dual-labelled probes, controls, and efficiency.
2. **[Bench protocol](#part-2-bench-protocol-sop)**: the lab SOP for setting up and running a plate on the Bio-Rad CFX.
3. **[Data quality control](#part-3-data-quality-control-step-by-step)**: a step-by-step check of every run, including baseline and threshold settings.
4. **[Notebook documentation](#part-4-documenting-a-qpcr-run-in-your-lab-notebook)**: what to record for every run, with a template you can copy.

!!! tip "The short version"
    Every qPCR plate needs: no-template controls (NTCs), technical replicates, and a reference gene. For cDNA you also need a no-RT control. Before you calculate anything, check the curves, the controls, the melt curve (SYBR only), and replicate agreement. Then record your baseline and threshold settings, and any wells you excluded, in your notebook.

---

## Part 1: How qPCR works

### Measuring PCR as it happens

In end-point PCR you only see the product after 30–40 cycles, once the reaction has plateaued, so the amount of product says little about how much template you started with. qPCR measures fluorescence **at every cycle**. That fluorescence is proportional to the amount of double-stranded product (SYBR/EvaGreen) or to the number of probes cleaved (hydrolysis probes).

In an efficient reaction the product doubles each cycle, so:

- A sample with **twice** as much starting template crosses a fluorescence threshold **1 cycle earlier**.
- A **10-fold** difference in template is about **3.32 cycles** (log₂10).

Every amplification curve goes through four phases:

| Phase | What is happening | Use for quantification? |
|---|---|---|
| **Baseline** (background) | Product is present but its signal is below background noise | No. This region defines the baseline. |
| **Exponential** | Product doubles each cycle (efficiency ≈ 100%) | **Yes. Set the threshold here.** |
| **Linear** | Reagents start to run out and efficiency drops | No |
| **Plateau** | The reaction has stopped | No. End-point values tell you nothing about starting amount. |

<figure>
<svg viewBox="0 0 640 300" width="100%" style="max-width:640px" role="img" aria-label="Two sigmoidal amplification curves crossing a threshold line in the exponential phase; the earlier curve has the lower Cq">
<g fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.8">
<line x1="60" y1="250" x2="610" y2="250"/>
<line x1="60" y1="250" x2="60" y2="30"/>
</g>
<rect x="60" y="30" width="200" height="220" fill="currentColor" opacity="0.05"/>
<path d="M60.0,250.0 L188.2,250.0 L215.2,249.8 L242.2,249.3 L262.5,248.1 L276.0,246.4 L289.5,243.1 L303.0,237.0 L316.5,226.2 L330.0,208.3 L343.5,182.2 L357.0,150.0 L370.5,117.8 L384.0,91.7 L397.5,73.8 L411.0,63.0 L424.5,56.9 L438.0,53.6 L458.2,51.3 L485.2,50.4 L519.0,50.1 L600.0,50.0" fill="none" stroke="var(--md-primary-fg-color, #3f51b5)" stroke-width="3"/>
<path d="M60.0,250.0 L255.8,250.0 L282.8,249.8 L309.8,249.3 L330.0,248.1 L343.5,246.4 L357.0,243.1 L370.5,237.0 L384.0,226.2 L397.5,208.3 L411.0,182.2 L424.5,150.0 L438.0,117.8 L451.5,91.7 L465.0,73.8 L478.5,63.0 L492.0,56.9 L505.5,53.6 L525.8,51.3 L552.8,50.4 L586.5,50.1 L600.0,50.0" fill="none" stroke="#e8710a" stroke-width="3"/>
<line x1="60" y1="225" x2="610" y2="225" stroke="#d32f2f" stroke-width="2" stroke-dasharray="6 4"/>
<text x="606" y="218" font-size="13" fill="#d32f2f" text-anchor="end">threshold</text>
<line x1="318" y1="225" x2="318" y2="250" stroke="var(--md-primary-fg-color, #3f51b5)" stroke-width="1.5" stroke-dasharray="3 3"/>
<line x1="386" y1="225" x2="386" y2="250" stroke="#e8710a" stroke-width="1.5" stroke-dasharray="3 3"/>
<text x="318" y="268" font-size="12" fill="currentColor" text-anchor="middle">Cq ≈ 18</text>
<text x="386" y="268" font-size="12" fill="currentColor" text-anchor="middle">Cq ≈ 23</text>
<text x="160" y="45" font-size="12" fill="currentColor" text-anchor="middle" opacity="0.8">baseline cycles</text>
<text x="300" y="120" font-size="12" fill="currentColor" text-anchor="middle">exponential</text>
<text x="500" y="40" font-size="12" fill="currentColor" text-anchor="middle">plateau</text>
<text x="335" y="292" font-size="13" fill="currentColor" text-anchor="middle">Cycle</text>
<text x="22" y="140" font-size="13" fill="currentColor" text-anchor="middle" transform="rotate(-90 22 140)">Fluorescence (RFU)</text>
</svg>
<figcaption>Two samples that differ by 5 cycles (Cq 18 vs 23) differ about 2⁵ = 32-fold in starting template, assuming 100% efficiency.</figcaption>
</figure>

### Key terms

- **Cq (quantification cycle)**, also called **Ct** (threshold cycle) or **Cp** (crossing point): the fractional cycle at which a well's fluorescence crosses the threshold. MIQE recommends the term *Cq*. Bio-Rad CFX Maestro uses it too.
- **Baseline**: the background fluorescence in early cycles. It is subtracted from each curve before the threshold is applied.
- **Threshold**: a fluorescence level set in the exponential phase of all curves for a target. **A Cq value only means something relative to the threshold it was measured at.**
- **RFU**: relative fluorescence units.
- **Efficiency (E)**: the fraction of templates copied each cycle. 100% means perfect doubling.

### Detection chemistries

#### SYBR Green / EvaGreen (intercalating dyes)

The lab's standard mix, **SsoFast EvaGreen Supermix**, uses this chemistry.

- **How it works:** The dye fluoresces strongly only when bound to double-stranded DNA. As amplicon builds up, more dye binds and the signal rises. EvaGreen is a newer dye of the same kind. It inhibits PCR less, so it can be used at a higher, saturating concentration, which gives sharper melt curves.
- **The catch:** The dye binds **any** dsDNA: your amplicon, primer-dimers, and off-target products. Specificity comes only from your primers, so **every SYBR/EvaGreen run must end with a melt curve** (see [QC step 6](#step-6-check-the-melt-curve-sybrevagreen-only)).
- **Melt curve:** After cycling, the instrument slowly heats the products from about 65 °C to 95 °C. Each product denatures ("melts") at a characteristic Tm and the dye is released, so fluorescence drops sharply. Plotted as −d(RFU)/dT, a single specific product gives **one sharp peak**.
- **Pros:** Cheap, flexible (any primer pair works), and the melt curve tells you about specificity.
- **Cons:** No multiplexing. Primer-dimers and non-specific products add to the signal. Primers need careful design and validation.

#### Dual-labelled hydrolysis probes (TaqMan® / 5′-nuclease assays)

- **How it works:** As well as the two primers, the reaction has an oligonucleotide **probe** that binds inside the amplicon. The probe has a **reporter** fluorophore (e.g. FAM, HEX, Cy5) on the 5′ end and a **quencher** (e.g. BHQ-1, or ZEN/Iowa Black in IDT double-quenched probes) on the 3′ end. While the probe is intact, the quencher absorbs the reporter's emission (FRET). During extension, the **5′→3′ exonuclease activity of Taq polymerase** cleaves the bound probe. This separates reporter from quencher, and the reporter fluoresces. Each cleaved probe adds signal permanently, so fluorescence tracks how many amplicons were made.
- **Specificity:** You need three oligos to bind (two primers plus the probe), so primer-dimers and most off-target products do **not** produce signal. **No melt curve is needed**, and you can't run one: cleaved probe doesn't re-anneal.
- **Multiplexing:** Using a different reporter dye for each target (e.g. FAM target + HEX reference gene), you can measure several targets in one well. Each dye needs its own CFX channel and validation for cross-talk.
- **Pros:** High specificity, multiplexing, and good for SNP genotyping and pathogen detection.
- **Cons:** Each probe costs more and takes more design work. You get no melt curve information.
- **Typical design rules:** Amplicon 70–150 bp. Probe Tm about 6–10 °C higher than the primers' Tm. Probe should not start with a 5′ G, because G quenches FAM.

#### Side-by-side

| | SYBR Green / EvaGreen | Dual-labelled probe |
|---|---|---|
| Signal comes from | Dye binding any dsDNA | Cleavage of a sequence-specific probe |
| Specificity | Primers only | Primers + probe |
| Melt curve | **Required** | Not possible / not needed |
| Primer-dimers give signal? | Yes | No |
| Multiplexing | No | Yes (different reporter dyes) |
| Cost per assay | Low | Higher (probe synthesis) |
| Lab default mix | SsoFast EvaGreen (Bio-Rad 172-5203) | Probe mix, e.g. SsoAdvanced Universal Probes (Bio-Rad) or equivalent |
| Best for | Screening many genes, new targets | Validated assays, multiplexing, low-abundance or diagnostic targets |

### Controls every plate needs

| Control | What it is | What it tells you | Pass criterion |
|---|---|---|---|
| **NTC** (no-template control) | Master mix + water instead of template | Contamination or primer-dimers | No amplification, *or* Cq ≥ 35 and ≥ 5 cycles later than your latest sample. For SYBR, its melt peak must **not** match the product peak. |
| **No-RT (NRT, −RT)** | RNA put through the RT step without reverse transcriptase | Genomic DNA contamination | No amplification, or ≥ 5 cycles later than the matching +RT sample (≥ 32-fold less signal) |
| **Reference gene(s)** | A gene expected to be stable across your treatments | Lets you normalize for input amount and RT efficiency | Stable Cq across treatments ([QC step 10](#step-10-check-reference-gene-stability)) |
| **Positive control / inter-run calibrator (IRC)** | One cDNA sample run on every plate | Run-to-run variation, so you can compare plates | Cq within ~0.5 cycles of its previous runs |
| **Technical replicates** | The same cDNA in 2–3 wells | Pipetting precision | SD ≤ 0.3 cycles (see [QC step 7](#step-7-check-technical-replicate-agreement)) |
| **Biological replicates** | Independent organisms or samples | Biological variation. **Your statistics run on these.** | n determined by your experimental design |

### Efficiency and standard curves

The 2^(−ΔΔCq) method assumes **100% efficiency** for both target and reference. Check this for every new primer pair before using it for real samples:

1. Make a **5-point, 5- or 10-fold dilution series** of pooled cDNA (pool a little from all samples).
2. Run each dilution in triplicate.
3. Plot Cq against log₁₀(relative input). Fit a line.
4. Efficiency **E = 10^(−1/slope) − 1**. A slope of −3.32 means E = 100%.

| Metric | Acceptable |
|---|---|
| Slope | −3.1 to −3.6 |
| Efficiency | 90–110% |
| R² | ≥ 0.98 |
| Dynamic range | Your samples' Cq values fall inside the range of the standard curve |

If efficiency is outside 90–110%, redesign the primers or use an efficiency-corrected analysis ([Pfaffl method](#step-2-calculate-relative-expression)). CFX Maestro computes slope, efficiency, and R² automatically when you mark the dilution wells as `Std` with starting quantities.

---

## Part 2: Bench protocol (SOP)

### SYBR/EvaGreen qPCR (lab default)

Written 20150702 by Sam White. Updated 2026-10 with probe-assay notes and data QC.

Generally we use SsoFast EvaGreen Supermix (BioRad) ([protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/BioRad_Sso_Fast_EvaGreen_Supermix.pdf)). This requires starting with cDNA.

**Reagents:**

- SsoFast EvaGreen Supermix ([BioRad: 172-5203](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/BioRad_Sso_Fast_EvaGreen_Supermix.pdf))
- Primer working stocks (10 µM)
- DNase-free H2O (NanoPure H2O)

**Personal Protective Equipment (PPE):**

- Gloves

**Equipment:**

- Pipettes (10 - 1000 µL)
- Filtered pipette tips
- White PCR plates, non-skirted, low profile ([USA Scientific: 1402-9590](http://www.usascientific.com/non-skirted-96-well-PCR-plate-low-profile-white.aspx))
- Optically clear strip caps ([USA Scientific: 1400-3800](http://www.usascientific.com/8-capstrip-0.2ml-tubes-flat-top.aspx))
- Sterile 1.7 mL snap-cap microfuge tubes ([Genesee: 22-281S](https://geneseesci.com/shop-online/product-details/?product=22-281S))
- Real-time PCR machine (Bio-Rad CFX)
- Ice

**Procedure**

Total Time: ~ 2.0 - 4.0 hrs
Cost/sample: ~ $0.42

1. Read the [manufacturer's protocol](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/BioRad_Sso_Fast_EvaGreen_Supermix.pdf).
2. Read *this* protocol, including [Part 3](#part-3-data-quality-control-step-by-step). Plan your controls before you start.
3. Plan the plate layout and fill in the [plate template CSV](#plate-spreadsheet-import). Save it with your notebook entry.
4. Verify sufficient quantities of reagents and samples before beginning.
5. Wear clean gloves. Set up in a clean area away from PCR products. Use filter tips.
6. Thaw reagents on ice. Mix the supermix gently by inversion (do not vortex hard) and spin it down. Keep the supermix protected from light.
7. Prepare master mix. Make enough for all samples in technical replicate, the NTCs (at least 2 wells per primer pair), the no-RT controls, and the inter-run calibrator, **plus 10% extra** for pipetting error. A single reaction is shown below:

    |Component  |Volume (µL)    |Final Concentration    |
    |----|----|----|
    |2x SsoFast EvaGreen Supermix    |10    |1x    |
    |Forward Primer (10 µM)|0.5|0.25 µM|
    |Reverse Primer (10 µM)|0.5|0.25 µM|
    |Water|Variable|Brings reaction volume up to 20 µL (including template)|

8. Distribute master mix to the white PCR plate (master mix + template = 20 µL).
9. Add template. Use a fixed template volume, typically 1–2 µL of diluted cDNA. Add water to the NTC wells last.
10. Cap with optical PCR caps. Don't write on or touch the cap tops: the instrument reads fluorescence through them.
11. Spin plate for 1 min @ 3000 g. Check for bubbles; they distort fluorescence readings.
12. Put plate in the real-time PCR machine. Load or import the plate layout and save the run file (`.pcrd`) using the [naming convention below](#file-naming-and-storage).
13. Recommended cycling parameters (40 cycles) are listed below. They may need to be changed to suit your primers or samples. See the manufacturer's protocol for recommendations.

    | Step | Temperature | Time | |
    |---|---|---|---|
    | 1. Initial denaturation | 98 °C | 2 min | |
    | 2. Denature | 98 °C | 5 s | |
    | 3. Anneal/extend | 60 °C | 5 s | **Plate read** |
    | 4. | | | Go to step 2, 39 more times |
    | 5. **Melt curve** | 65 °C → 95 °C | +0.5 °C increments, 2–5 s each | **Plate read** at each step |

### Dual-labelled probe qPCR

Use a probe-specific master mix: intercalating-dye mixes like SsoFast EvaGreen will *not* work. The general setup is the same as above. These things differ:

| Component | Per 20 µL reaction | Final concentration |
|---|---|---|
| 2x probe master mix (e.g. SsoAdvanced Universal Probes Supermix) | 10 µL | 1x |
| Forward primer (10 µM) | 0.8–1.8 µL | 0.4–0.9 µM (check the mix's manual) |
| Reverse primer (10 µM) | 0.8–1.8 µL | 0.4–0.9 µM |
| Probe (5 µM) | 1.0 µL | 0.25 µM |
| Template + water | to 20 µL | |

- Store probes in the dark, in small aliquots, at −20 °C. Avoid repeated freeze–thaw.
- **Cycling:** 95 °C for 2–3 min, then 40 cycles of 95 °C for 5–15 s and 60 °C for 30 s (plate read). **No melt curve.**
- **In CFX Maestro:** Under plate setup, assign the correct **fluorophore** (e.g. FAM, HEX/VIC) to each target in each well. Only channels assigned in the plate layout are analyzed.
- **Multiplexing:** Before using a multiplex for real samples, show that each assay gives the same Cq run alone (singleplex) as in the multiplex. Put the less abundant target on the brightest dye (FAM).

---

## Part 3: Data quality control, step by step

Do these steps **in order for every run**, before you calculate any expression values. The instructions use **Bio-Rad CFX Maestro**. Other instruments have the same settings under different names. Record what you find at each step in your notebook ([Part 4](#part-4-documenting-a-qpcr-run-in-your-lab-notebook)).

!!! warning "Golden rules"
    - **Never overwrite the raw `.pcrd` file.** If you change analysis settings, save a copy with a suffix (e.g. `_analyzed.pcrd`).
    - **Decide your QC criteria before you look at results**, and apply them the same way to all samples. Excluding wells because the result "looks wrong" biologically is not QC.
    - **Every excluded well needs a written reason** in your notebook.

### Step 1: Confirm the run completed and the plate map is correct

1. Open the `.pcrd` file. Check the **Run Information** tab: protocol, number of cycles, and that no errors were logged.
2. In **Plate Setup**, confirm each well has the correct `Sample Type` (Unknown, NTC, NRT, Std, Pos Ctrl), target, sample name, and fluorophore. A wrong plate map is the most common cause of results that "make no sense."

### Step 2: Look at the raw amplification curves

1. On the **Quantification** tab, select all wells.
2. View the curves in **both linear and log scale**. Right-click the graph and choose `Log Scale` to switch.
3. Check one target at a time by filtering in the well selector. **Look for:**
    - Smooth, sigmoidal curves with a clear exponential phase and a plateau.
    - Replicate curves that lie on top of each other.
    - Curves that are roughly **parallel** in the exponential phase on the log scale. Parallel curves mean similar efficiency across samples.
4. **Flag wells with:**
    - Jagged or spiky curves (bubbles, condensation, or a poorly sealed cap).
    - Gradual linear drift without a real exponential rise. This is not amplification.
    - Curves that plateau unusually low or with a much shallower slope (inhibition, a different product, or pipetting error).
    - "Amplification" that is a single-cycle jump (instrument artifact).

### Step 3: Check the baseline

The baseline is the stretch of early cycles used to estimate background. CFX Maestro sets this automatically (**Baseline Subtracted Curve Fit**, the default under `Settings > Baseline Setting`). This works well in most cases.

1. In log view, the baseline-subtracted curves should be **flat and noisy around the bottom** before rising. They should not slope up or down.
2. **Adjust the baseline manually when** a highly abundant sample (Cq < ~15) starts rising *inside* the auto-baseline window. In that case its curve dips or looks oddly shaped. Use `Settings > Baseline Setting` and set the baseline cycles for the affected wells so the window **ends at least 2 cycles before that well's curve starts to rise**. A common default window is cycles 3–15. Shorten it for early-Cq wells.
3. Write down the baseline mode and any manual changes.

### Step 4: Set the threshold

The threshold is the line used to calculate every Cq. It needs to cross **all** curves for a target in their exponential phase.

1. **Work one target at a time**: select only that target's wells. CFX Maestro allows a different threshold per fluorophore. With SYBR/EvaGreen everything is in one channel, so think about each primer pair separately.
2. Switch to **log scale**. On a log axis the exponential phase looks like a straight, steep, parallel section of each curve.
3. Start from the auto-calculated threshold (`Settings > Cq Determination Mode > Single Threshold`, threshold *auto-calculated*). Then check it:
    - It must be **above the baseline noise** of every well, including NTCs that show only noise.
    - It must be **within the exponential (straight, parallel) part** of all curves. It must be below where they start to bend over into the linear/plateau phase.
    - If those two conditions conflict for some wells, those wells have a curve-shape problem. Go back to Step 2.
4. To adjust it, drag the threshold line or type a value under `Settings > Baseline Threshold > User Defined`. Small moves within the exponential phase should barely change ΔCq values between samples, which is a quick check that the position is good. If moving the threshold changes the *differences* between samples a lot, the curves are not parallel. Investigate efficiency.
5. **Use the same threshold value for a given target on every plate you plan to compare.** Record the exact value in RFU. If plates differ in overall fluorescence, use the inter-run calibrator to correct for it, rather than tuning thresholds plate by plate to make the calibrator match.
6. *Regression mode* (`Cq Determination Mode > Regression`) fits each curve individually without a single threshold. It's acceptable, but whichever mode you use, **use it consistently across a whole experiment** and record it.

!!! note "Why the threshold matters"
    Moving the threshold shifts every Cq for that target. Comparisons (ΔCq) stay valid only if all samples are measured at the same threshold *and* their curves are parallel at that point. This is why the threshold value has to be in your notebook. Without it, nobody (including you in six months) can reproduce your Cq values from the raw file.

### Step 5: Check the controls

1. **NTCs:** Ideally show no Cq ("N/A"). If an NTC has a Cq:
    - Cq ≥ 35 **and** ≥ 5 cycles later than the latest sample → generally acceptable. Note it.
    - Earlier than that → contamination or primer-dimer. For SYBR, check the NTC's melt peak in Step 6. If it matches your product's Tm, it's **contamination**: the target data from that plate are suspect, so remake reagents and rerun. If its Tm is lower (primer-dimer), see Step 6.
2. **No-RT controls:** Should be ≥ 5 cycles later than the matching +RT sample (or show no amplification). If not, DNase-treat the RNA ([DNase protocol](https://github.com/RobertsLab/resources/blob/master/protocols/dnase_rna.md)), redo the RT, or redesign primers to span an exon–exon junction.
3. **Inter-run calibrator / positive control:** Compare its Cq to previous plates. A shift of > ~0.5–1 cycle means the run differs (reagent lot, pipetting, instrument). Note it, and correct using the calibrator if you're combining plates.

### Step 6: Check the melt curve (SYBR/EvaGreen only)

Open the **Melt Curve** tab and view the **Melt Peak** plot (−d(RFU)/dT vs temperature).

| What you see | Meaning | Action |
|---|---|---|
| One sharp peak, same Tm (±0.5 °C) in all sample wells | Single specific product | ✅ Pass |
| Extra small peak at lower Tm (~70–78 °C), mostly in NTCs or low-template wells | Primer-dimer | OK if absent or minor in sample wells. If present in sample wells, lower primer concentration, raise annealing temperature, or redesign. |
| Two clear peaks, or a big shoulder, in sample wells | Non-specific product, or two products | Do **not** trust the Cq for those wells. Run products on a gel to check. |
| Peak Tm shifted in some wells | Different product, or a SNP in the amplicon | Investigate. Exclude if it's a different product. |
| NTC peak at the same Tm as the product | Contamination | Fails. See Step 5. |

If you're unsure, run a few wells on a 2% agarose gel. You should see one band of the expected size.

### Step 7: Check technical replicate agreement

1. On the **Quantification Data** tab, look at the `Cq Std. Dev` column for each sample–target pair.
2. Criteria (set these before the run and apply them consistently):
    - **SD ≤ 0.3 cycles** (≤ 0.2 is excellent) → pass.
    - SD > 0.3 with triplicates: if **one** replicate is clearly the outlier (> 0.5 cycles from the other two, which agree with each other) **and** there is a technical reason (bubble, odd curve in Step 2, bad melt in Step 6), exclude that one well and write down why.
    - If replicates disagree with no clear outlier, or you'd be left with fewer than 2 wells → **rerun that sample**.
3. Expect more replicate scatter at high Cq (> 32), because of stochastic sampling of few template molecules. This is one reason late Cqs are less reliable.
4. To exclude a well in CFX Maestro, right-click it → `Well > Exclude Well(s) from Analysis`. It stays in the raw file.

### Step 8: Check that Cq values are in a usable range

| Cq | Interpretation |
|---|---|
| < 10–12 | Very abundant. Check the baseline (Step 3). Consider diluting the cDNA. |
| 15–30 | Ideal range |
| 30–35 | Low abundance. Usable, but more variable. Make sure NTCs are clearly later. |
| > 35 | Near the detection limit. Treat as "detected, not quantifiable" unless your standard curve shows the assay is linear there. |
| No Cq | Not detected. **Do not** substitute 40 without a stated rule. Record as not detected and explain how you handled it in the analysis. |

### Step 9: Check efficiency (when a standard curve is on the plate)

On the **Standard Curve** chart, check slope, efficiency (E), and R² against the criteria in [Part 1](#efficiency-and-standard-curves). Record them. If you don't run a standard curve on every plate, cite the notebook entry where you validated that primer pair.

### Step 10: Check reference gene stability

Normalization only works if the reference gene doesn't respond to your treatment.

1. Plot the raw reference-gene Cq for every sample, grouped by treatment.
2. The groups should be similar. A difference of more than ~0.5 cycles between treatments, or a significant treatment effect in a quick ANOVA, means that gene is **not a valid reference** for this experiment.
3. Use 2+ reference genes where possible. Evaluate stability with geNorm/NormFinder (e.g. the R packages [`ctrlGene`](https://cran.r-project.org/package=ctrlGene) or `NormqPCR`) and normalize to the geometric mean of the stable ones.

### Step 11: Export data and save files

1. Export the results. In CFX Maestro: `Export > Export All Data Sheets` (CSV), or at minimum the **Quantification Cq Results** and, for SYBR, **Melt Curve Peak Results** sheets.
2. Also export the **raw amplification data** (`Quantification Amplification Results`). MIQE 2.0 encourages sharing raw fluorescence so others can re-analyze it.
3. Save a screenshot or PDF report of the amplification plot (log view, with threshold) and the melt peaks for each target.
4. Put the `.pcrd`, the exports, and the images in your project repository or data directory ([Data Management](../Data-Management.md)). Link them from your notebook entry.

#### File naming and storage

Use a consistent, sortable name, for example:

```
YYYYMMDD_<initials>_qPCR_<project>_<targets>_plate<N>.pcrd
20261003_SR_qPCR_oyster-heat_HSP70-EF1a_plate1.pcrd
20261003_SR_qPCR_oyster-heat_HSP70-EF1a_plate1_Cq-results.csv
```

#### Optional: QC check in R

This flags replicate SD, late Cqs, and NTC problems in a CFX export. It assumes the CFX Maestro `Quantification Cq Results` CSV. Check the column names in your file, because they vary slightly between software versions.

```r
library(tidyverse)

cq <- read_csv("20261003_SR_qPCR_oyster-heat_HSP70-EF1a_plate1_Cq-results.csv") %>%
  select(Well, Target, Content, Sample, Cq) %>%
  mutate(Cq = as.numeric(Cq))          # "NaN"/blank = no amplification

# 1. Controls: any NTC/NRT with amplification?
cq %>%
  filter(str_detect(Content, "NTC|NRT")) %>%
  filter(!is.na(Cq))

# 2. Technical replicate summary and flags
rep_qc <- cq %>%
  filter(str_detect(Content, "Unkn")) %>%
  group_by(Target, Sample) %>%
  summarise(n = sum(!is.na(Cq)),
            mean_Cq = mean(Cq, na.rm = TRUE),
            sd_Cq   = sd(Cq, na.rm = TRUE),
            .groups = "drop") %>%
  mutate(flag = case_when(n < 2          ~ "too few replicates",
                          sd_Cq > 0.3    ~ "replicate SD > 0.3",
                          mean_Cq > 35   ~ "late Cq (> 35)",
                          TRUE           ~ "pass"))

rep_qc %>% count(Target, flag)
rep_qc %>% filter(flag != "pass")
```

### Quick troubleshooting table

| Symptom | Likely cause | Fix |
|---|---|---|
| Amplification in NTC at product Tm | Contaminated reagents or water, or aerosol carryover | Fresh aliquots, clean bench/pipettes, set up away from PCR products |
| Primer-dimer peak in sample wells | Primer concentration too high or poor primer design | Titrate primers, raise annealing temperature, redesign |
| High replicate SD | Pipetting, bubbles, too little template | Reverse pipetting, a master mix that includes template where possible, spin the plate |
| Curves not parallel / shallow slope | Inhibitors (e.g. carry-over from extraction), poor efficiency | Dilute cDNA (inhibition shows as Cq not shifting by the expected amount with dilution), re-clean RNA |
| No amplification anywhere | Missing component, wrong mix, wrong fluorophore or channel | Check the plate setup's fluorophore. Check the master mix recipe. |
| No-RT amplifies | gDNA contamination | DNase treatment, intron-spanning primers |
| Late Cq in all samples | Low expression or too little cDNA | Use more cDNA, or accept as low abundance (see Step 8) |

---

## qPCR data analysis

Only analyze wells that passed QC.

### Step 1: Average technical replicates

Use the mean Cq of the passing technical replicates for each biological sample × target.

### Step 2: Calculate relative expression

**ΔCq (normalize to the reference gene, per sample):**

ΔCq = Cq(target) − Cq(reference)

If you use more than one reference gene, use the mean of their Cqs. That is equivalent to the geometric mean of their quantities.

**Relative expression of a sample:** 2^(−ΔCq). This is often used for plotting individual samples.

**ΔΔCq fold change (Livak method, assumes ~100% efficiency for both genes):**

ΔΔCq = ΔCq(treated sample) − mean ΔCq(control group)

Fold change = 2^(−ΔΔCq)

**Efficiency-corrected (Pfaffl method), when efficiencies differ from 100% or from each other:**

Ratio = (E_target)^(ΔCq_target(control − treated)) / (E_ref)^(ΔCq_ref(control − treated))

Here E is the amplification factor: 2.0 for 100% efficiency, 1.95 for 95%, and so on. MIQE 2.0 recommends efficiency-corrected quantities as the default.

### Step 3: Statistics

- Run statistics on **ΔCq values** (log scale, roughly normally distributed). Do **not** run them on fold changes, which are skewed.
- Use biological replicates as n, not technical replicates.
- Use a t-test for two groups. Use ANOVA or a linear (mixed) model for more groups or designs with plates or tanks as blocks. Report the test, the n, and the p-value.

### Step 4: Interpretation

Fold change > 1 means higher expression in the treatment than in the control. Fold change < 1 means lower. Report fold changes with confidence intervals back-transformed from the ΔCq scale.

---

## Part 4: Documenting a qPCR run in your lab notebook

Your notebook entry should let someone else **regenerate your Cq values from the raw file and understand every decision you made**. See [Lab Notebooks](../Lab-Notebooks.md) for general expectations. Copy the template below into your notebook for each plate.

!!! example "What reviewers (and future you) will ask for"
    The plate layout, primer IDs and sequences, master mix lot, cycling program, **baseline mode, threshold value per target**, which wells were excluded and why, and links to the raw `.pcrd` and exported CSVs.

```markdown
## qPCR – <project> – <targets> – plate <N>

**Date:** 2026-10-03  **Operator:** <name>
**Objective:** <one sentence: what question is this plate answering?>

### Samples
- cDNA source: <link to RT notebook entry>, RNA input per RT: ___ ng
- cDNA dilution used: 1:___ ; template volume per well: ___ µL
- Sample IDs: <list or link to sample sheet>

### Assays
| Target | Primer IDs (lab primer DB #) | Chemistry | Amplicon (bp) | Expected Tm / probe dye | Efficiency (link to validation) |
|---|---|---|---|---|---|
| HSP70 | SR_123 / SR_124 | EvaGreen | 112 | 82.5 °C | 98%, R² 0.995 (<link>) |
| EF1a (ref) | SR_045 / SR_046 | EvaGreen | 97 | 80.0 °C | 101%, R² 0.998 (<link>) |

### Reagents
- Master mix: <name, cat #, lot #>
- Primer working stock prep date: ___
- Water: ___

### Plate setup
- Plate layout: <link to plate CSV / image>
- Controls included: NTC (wells ___), No-RT (wells ___), IRC/positive (wells ___), standards (wells ___)
- Technical replicates: ___ per sample

### Run
- Instrument: Bio-Rad CFX <model/ID>
- Protocol: 98 °C 2 min; 40× (98 °C 5 s, 60 °C 5 s + read); melt 65–95 °C +0.5 °C
- Raw file: <link to .pcrd>
- Exports: <links to Cq results CSV, melt peak CSV, amplification CSV>

### Analysis settings
- Software / version: CFX Maestro ___
- Baseline: Baseline Subtracted Curve Fit (auto) | manual changes: <wells, cycles>
- Cq determination: Single Threshold | Regression
- Threshold (RFU): HSP70 = ___ ; EF1a = ___  (auto / user-defined)

### QC checklist
- [ ] Run completed, plate map verified
- [ ] Amplification curves: sigmoidal, replicates overlap — notes:
- [ ] Baseline appropriate — notes:
- [ ] Threshold in exponential phase for all curves (log view screenshot: <link>)
- [ ] NTCs: <no amp / Cq values + melt Tm>
- [ ] No-RT: <no amp / ΔCq vs +RT>
- [ ] Melt curve: single peak at expected Tm (screenshot: <link>)
- [ ] Technical replicate SD ≤ 0.3 — samples failing:
- [ ] Cq range acceptable — samples > 35:
- [ ] Efficiency / standard curve: slope ___, E ___ %, R² ___
- [ ] Reference gene stable across treatments — notes:
- [ ] IRC Cq vs previous plates: ___

### Excluded wells
| Well | Sample / Target | Reason |
|---|---|---|
| B4 | oyster_07 / HSP70 | bubble; jagged curve; 1.2 cycles from other two replicates |

### Results summary
<brief summary, figure, link to analysis script/Rmd>

### Next steps
<rerun samples X, Y; validate new primer; etc.>
```

---

## CFX Maestro software

### Plate spreadsheet import

1. Modify [cfx_plate_template.csv](https://raw.githubusercontent.com/RobertsLab/resources/master/protocols/cfx_plate_template.csv) (CSV) with your `Target Name` and `Sample Name` values and save it as a CSV file.
2. In CFX Maestro, create a new plate: `File > New > Plate...`.
3. Highlight all wells.
4. Select `Sample Type` of `Unknown`.
5. In the `Target Names` section, click on the empty box next to `SYBR`. For probe assays, use the box next to the probe's fluorophore (e.g. `FAM`).
6. Click on the `Spreadsheet View/Importer` tab along the top.
7. Click `Import`.
8. Find the file you saved in Step 1 and click `Open`.
9. Click `Okay`.
10. Update the plate layout with any other `Sample Type` (e.g. NTC, NRT, Std, Positive Control), `Technical Replicates`, and `Trace Styles`.
11. Save the file.

---

## References and further reading

- Bustin SA, Ruijter JM, van den Hoff MJB, et al. (2025). MIQE 2.0: Revision of the Minimum Information for Publication of Quantitative Real-Time PCR Experiments Guidelines. *Clinical Chemistry* 71(6):634–651. [doi:10.1093/clinchem/hvaf043](https://doi.org/10.1093/clinchem/hvaf043)
- Bustin SA, Benes V, Garson JA, et al. (2009). The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments. *Clinical Chemistry* 55(4):611–622. [doi:10.1373/clinchem.2008.112797](https://doi.org/10.1373/clinchem.2008.112797)
- Livak KJ, Schmittgen TD (2001). Analysis of relative gene expression data using real-time quantitative PCR and the 2^(−ΔΔCT) method. *Methods* 25(4):402–408. [doi:10.1006/meth.2001.1262](https://doi.org/10.1006/meth.2001.1262)
- Pfaffl MW (2001). A new mathematical model for relative quantification in real-time RT-PCR. *Nucleic Acids Research* 29(9):e45. [doi:10.1093/nar/29.9.e45](https://doi.org/10.1093/nar/29.9.e45)
- Taylor SC, Nadeau K, Abbasi M, et al. (2019). The ultimate qPCR experiment: producing publication quality, reproducible data the first time. *Trends in Biotechnology* 37(7):761–774. [doi:10.1016/j.tibtech.2018.12.002](https://doi.org/10.1016/j.tibtech.2018.12.002)
- [IDT qPCR Application Guide](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/IDT_qPCR_Application_Guide_20100823.pdf) (PDF, in this repo). Good background on probe design and chemistries.
- [SsoFast EvaGreen Supermix manual](https://github.com/RobertsLab/resources/blob/master/protocols/Commercial_Protocols/BioRad_Sso_Fast_EvaGreen_Supermix.pdf) (PDF, in this repo)
