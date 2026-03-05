# Guava Muse SOP

The Guava Muse Cell Analyzer provides automated cell count and viability measurements. These protocols cover setup, daily operation, and maintenance.

It is highly recommend you read through the manufacturer's protocol prior to using the machine!

- [Cytek-muse-guava-cell-analyzer.pdf](https://github.com/RobertsLab/resources/blob/master/equipment_manuals/Cytek-muse-guava-cell-analyzer.pdf) (GitHub)

## Kits Used

- **Muse System Check Kit**: Verifies the performance of the system by assessing counting accuracy and fluorescence detection using a standardized fluorescent bead reagent. The kit contains a bead reagent and diluent.
- **Muse Count & Viability Kit**: Used to determine viability and total cell count. Accurate assessments can be made with a wide variety of cell lines, even those with unusual culture conditions or a tendency to aggregate.

---

If this is the first time the machine is _ever_ being used, please see [Instrument Setup Section](#instrument-setup-first-time-only).

## Daily Startup Procedure

1. **Turn On Unit**
   - Press power button if not auto-on. Wait for touchscreen to initialize.

2. **Prepare Fluids**
   - Empty waste bottle, rinse, and refill with 10 mL bleach.
   - Refill cleaning bottle with Guava ICF to indicator line.
   - Reconnect fluid tubing.

3. **Reset Fluid Levels**
   - On touchscreen: `Menu` → `System Check` → `Clean` → `Reset Fluid Levels`.

4. **Run Complete System Clean**
   - On touchscreen: `Menu` → `Muse System Cleaning` → `Complete System Clean`.
   - Load full tube of Guava Instrument Cleaning Fluid (ICF) → then DI water.
   - Run until log confirms success.

5. **Run System Check**
   - Mix beads prior to making solution.
   - Prepare 1:20 dilution of System Check Beads.
   - On touchscreen: `Menu` → `Essential Tools` → `System Check`.
   - Enter Lot #, Expiration, Check Code (found on bead kit card).
   - Mix beads, load tube, run 3 replicates.
   - Confirm **PASS** status and %CV ≤10%.
   - Export results (optional).

> **Note**: The values recorded during the replicates should be green/grey, meaning they fall within the expected range. If they are red, the values are too high/low, and the system check will fail. This check is temperamental. Values should be within $4.5 \times 10^4$ - $5.5 \times 10^4$.

---

## Daily Shutdown Procedure

1. **Run Complete System Clean**
   - Same as startup. Ends with DI water rinse.

2. **Leave DI Water Tube on Loader**
   - Never leave bleach or ICF on the system overnight.

3. **Power Down**
   - On touchscreen: `Menu` → `Power Options` → `Power Off`.

---

## Maintenance Log Example

| Date | User | Waste emptied | ICF refilled | System Clean | System check (p/f) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18/04/25 | Aakriti | No | Yes | Yes | Pass | First use so did not empty waste |
| 21/04/25 | Aakriti | Yes | Yes | Yes | Pass | |
| 24/04/25 | Aakriti | Yes | Yes | Yes | Pass | |

---

## Important Usage Notes

- **Quick Clean**: When running samples, need to run a quick clean every 20 acquisitions.

--

## Instrument Setup (First-Time Only)

1. **Unpack and Position**
   - Carefully remove the Muse from the shipping box and save all packaging.
   - Place it on a stable surface away from vibrations.

2. **Connect Fluid Bottles**
   - Connect color-coded fluid tubing to the back of the instrument.
   - Fill waste bottle: add ~10 mL bleach (to first fill line).
   - Fill cleaning solution bottle to the indicator line with Guava ICF.
   - Insert bottles into their matching receptacles and connect the tubing.

3. **Insert Flow Cell**
   - Open the access door and follow flow cell insertion.

4. **Power On**
   - Plug the Muse into a grounded outlet. It turns on automatically the first time.

5. **Log On as Administrator**
   - Select Administrator account on first login (p. 35).
   - **Important**: Add a new Admin-level user to avoid losing access to data.

6. **Initial Cleaning**
   - Run **Complete System Clean** → do this twice on first use (On touchscreen: `Essential Tools` > `Complete System Clean`) (p. 63).