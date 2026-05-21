## Total antioxidant capacity (TAOC) assay

This page simplifies the single-plate analysis used for the Cell Biolabs total antioxidant capacity assay. It is based on Sam Gurr's original analysis notebook and the accompanying metadata in the [NEFSC/EAD-ASEB-Cvirginica_Thermal_Performance](https://github.com/NEFSC/EAD-ASEB-Cvirginica_Thermal_Performance) repository.

### Key calculation steps

1. Calculate **net absorbance** for each well as:

   `final absorbance - initial absorbance`

2. Build a **uric acid standard curve** from the TAOC standards.
3. Interpolate each sample's **uric acid equivalent (UAE)** from that curve.
4. Convert UAE to **copper reducing equivalents (CRE)** using the kit conversion:

   `CRE = UAE × 2189`

5. Build a **protein standard curve** from the paired BCA plate.
6. Convert each sample to **µg protein loaded into the TAOC well**.
7. Normalize TAOC output as:

   `CRE / µg protein loaded`

---

## Plate layout inferred from Sam's metadata

### TAOC plate

Sam's plate map uses a 96-well plate with:

- `A1:A12` = uric acid standards `1:6`, each in duplicate
- `B1:B6` = uric acid standards `7:9`, each in duplicate
- `B7:B8` = blanks
- `B9:H12` = samples, usually loaded in side-by-side duplicate wells

In other words, the TAOC plate starts with standards and blanks in the upper-left corner, and the remaining wells are samples.

### Protein plate

The paired total protein plate uses:

- `A1:A12` = BCA standards `A:F`, each in duplicate
- `B1:B4` = BCA standards `G:H`, each in duplicate
- `B5:B6` = zero-protein blank / standard `I`
- remaining wells = samples in duplicate

This means the two assays follow the same general idea: standards first, then blanks, then duplicated samples.

---

## Minimum files needed for a single plate

For one TAOC plate, prepare:

- one exported text file for the **initial** TAOC read
- one exported text file for the **final** TAOC read
- one exported text file for the paired **BCA protein** plate
- one CSV plate map for the TAOC plate
- one CSV plate map for the BCA plate

The two plate-map CSV files can be very simple. Use these columns:

### `taoc_plate_map.csv`

- `well`
- `sample_type` (`standard`, `blank`, or `sample`)
- `standard_id`
- `sample_id`

### `bca_plate_map.csv`

- `well`
- `sample_type` (`standard`, `blank`, or `sample`)
- `standard_id`
- `sample_id`

Use the same `sample_id` values in both files so the TAOC and protein results can be joined at the end.

---

## Simplified single-plate R workflow

```r
library(dplyr)
library(tidyr)
library(readr)
library(ggplot2)

read_plate_export <- function(path, plate = 1) {
  raw <- read.delim(
    path,
    header = FALSE,
    skip = 3,
    fileEncoding = "latin1"
  )

  values <- as.matrix(raw[1:8, 3:14])
  dimnames(values) <- list(LETTERS[1:8], as.character(1:12))

  as.data.frame.table(values, responseName = "absorbance") |>
    transmute(
      plate = plate,
      well = paste0(Var1, Var2),
      absorbance = as.numeric(as.character(absorbance))
    )
}

uric_acid_levels_mM <- c(
  `1` = 1,
  `2` = 0.5,
  `3` = 0.25,
  `4` = 0.125,
  `5` = 0.0625,
  `6` = 0.03125,
  `7` = 0.0156,
  `8` = 0.0078,
  `9` = 0.0039
)

bca_levels_ug_mL <- c(
  A = 2000,
  B = 1500,
  C = 1000,
  D = 750,
  E = 500,
  F = 250,
  G = 125,
  H = 25,
  I = 0
)

taoc_before <- read_plate_export("20240709_TAOC_Plate1_beforeCu.txt")
taoc_after  <- read_plate_export("20240709_TAOC_Plate1_afterCu.txt")
bca_plate   <- read_plate_export("Total_Protein_TAOC_Plate1.txt")

taoc_map <- read_csv("taoc_plate_map.csv", show_col_types = FALSE) |>
  mutate(sample_type = tolower(sample_type))

bca_map  <- read_csv("bca_plate_map.csv", show_col_types = FALSE) |>
  mutate(sample_type = tolower(sample_type))

taoc <- taoc_map |>
  left_join(rename(taoc_before, abs_before = absorbance), by = "well") |>
  left_join(rename(taoc_after, abs_after = absorbance), by = "well") |>
  mutate(net_abs = abs_after - abs_before)

bca <- bca_map |>
  left_join(bca_plate, by = "well")

taoc_standards <- taoc |>
  filter(sample_type == "standard") |>
  mutate(uric_acid_mM = unname(uric_acid_levels_mM[as.character(standard_id)])) |>
  group_by(standard_id, uric_acid_mM) |>
  summarise(net_abs = mean(net_abs), .groups = "drop") |>
  arrange(net_abs)

taoc_curve <- approxfun(
  x = taoc_standards$net_abs,
  y = taoc_standards$uric_acid_mM,
  ties = mean,
  rule = 1
)

bca_blank_mean <- bca |>
  filter(sample_type == "blank") |>
  summarise(blank = mean(absorbance)) |>
  pull(blank)

bca_standards <- bca |>
  filter(sample_type == "standard") |>
  mutate(
    protein_ug_mL = unname(bca_levels_ug_mL[as.character(standard_id)]),
    net_abs = absorbance - bca_blank_mean
  ) |>
  group_by(standard_id, protein_ug_mL) |>
  summarise(net_abs = mean(net_abs), .groups = "drop") |>
  arrange(net_abs)

bca_curve <- approxfun(
  x = bca_standards$net_abs,
  y = bca_standards$protein_ug_mL,
  ties = mean,
  rule = 1
)

protein_by_sample <- bca |>
  filter(sample_type == "sample") |>
  mutate(
    net_abs = absorbance - bca_blank_mean,
    protein_ug_mL = bca_curve(net_abs)
  ) |>
  group_by(sample_id) |>
  summarise(protein_ug_mL = mean(protein_ug_mL, na.rm = TRUE), .groups = "drop")

taoc_by_sample <- taoc |>
  filter(sample_type == "sample") |>
  mutate(
    uric_acid_equiv_mM = taoc_curve(net_abs),
    cre_uM = uric_acid_equiv_mM * 2189
  ) |>
  group_by(sample_id) |>
  summarise(cre_uM = mean(cre_uM, na.rm = TRUE), .groups = "drop")

results <- taoc_by_sample |>
  left_join(protein_by_sample, by = "sample_id") |>
  mutate(
    # 20 µL TAOC sample volume = 0.020 mL
    protein_ug_in_taoc_well = protein_ug_mL * 0.020,
    taoc_uM_cre_per_ug_protein = cre_uM / protein_ug_in_taoc_well
  )

write_csv(results, "taoc_single_plate_results.csv")

ggplot(taoc_standards, aes(uric_acid_mM, net_abs)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  theme_bw() +
  labs(x = "Uric acid (mM)", y = "Net absorbance at 490 nm")

ggplot(bca_standards, aes(protein_ug_mL, net_abs)) +
  geom_point() +
  geom_line() +
  theme_bw() +
  labs(x = "Protein (µg/mL)", y = "Net absorbance at 562 nm")
```

---

## What this script keeps from Sam's workflow

- TAOC net absorbance is still calculated as `after - before`
- UAE is still converted to CRE with the `× 2189` factor
- final TAOC values are still normalized to the amount of protein loaded into the TAOC well
- duplicate wells are averaged to one result per sample

## What this script simplifies

- one plate at a time instead of combining multiple plates
- no hard-coded plate-specific regression coefficients
- no dependence on tank number or temperature number
- no manual algebra to invert standard curves

---

## Recommended quality checks

Before trusting the output:

- inspect both standard-curve plots
- confirm sample duplicates are reasonably close
- confirm blanks are low
- confirm sample absorbances fall inside the standard-curve range

If a plate has very weak standards or samples outside the standard range, do not force the interpolation. Re-run the plate or rebuild the standard curve using a valid concentration range.

## References

- [Sam Gurr's original TAOC R Markdown analysis](https://github.com/NEFSC/EAD-ASEB-Cvirginica_Thermal_Performance/blob/main/RAnalysis/Scripts/TAOC.Rmd)
- [Cell Biolabs STA-360 Total Antioxidant Capacity Assay Kit](https://github.com/user-attachments/files/25913628/STA-360-total-antioxidant-capacity-assay-kit.2.pdf)
