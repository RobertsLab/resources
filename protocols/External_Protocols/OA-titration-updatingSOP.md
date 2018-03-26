# Titrator SOP

Orginally developed by Genevieve Bernatchez and Nyssa Silbiger 07/18/2016

---

##### Reagents:
- Distilled (DI) water
- pH Buffer 4.0 (Fisher SB101-4)
- pH Buffer 7.0 (Fisher SB107-4)
- pH buffer 10.0 (Fisher SB115-4)
- 0.1M Hydrochloric acid from Dickson Lab ()
- CO<sub>2</sub> Reference Materials from Dickson Lab (CRMs)

##### Personal Protective Equipment (PPE):
- gloves
- lab coat

##### Equipment:
- Excellence Titrator T5 (Mettler-Toledo)
- Rondolino Sample Changer (Mettler-Toledo)
- Scale: Capable of measuring to 0.0001g
- Rondolino Sample cups (Mettler-Toledo)
- Serological pipettes & pipettor
- Hazardous waste jug
- Aquarium air pump
- Rotameter (Omega  FL-2010-SS; 0.04-0.5LPM)

## 1. DAILY STARTUP PROCEDURES

#### Check Reagents
1. Check the volume of DI water in the rinse bottle. You need at least 300mL to process a full carousel of samples.
2. Check the hose in the rinse bottle to ensure it reaches the bottom of the bottle.
3. Check the volume of HCl in the amber bottle. You will need at least 50mL to process a single sample (30mL for initial purging procedure and ~5mL for each subsequent sample).

*__IMPORTANT__*: If the volume of HCl is below the halfway mark, please submit a purchase request for more acid, as there is significant lead time for receiving new orders of HCl.

#### Start LabX Software, Titrator, and Rondolino
1. Login in to the ```srlab``` acount on the computer next to the titrator and open LabX.
2. Turn the titrator on (button on front of cube).
3. Turn the Rondolino on (switch on rear, lower right). It will perform a brief system check, where the probes will raise and the carousel will rotate, before returning the probes and carousel to their original positions.
4. Ensure the right blue dial on top of the Rondolino is turned to position 1. This enables the probe-rinsing feature.
4. Press the left blue button on top of the Rondolino (rotates carousel 180˚)
5. Place an empty cup in position zero.
6. Press the left blue button on top of the Rondolino to turn carousel 180˚ back to position zero.

---

## 2. pH CALIBRATION


1. Place each buffer (Mettler Toledo Technical buffers: 4.01, 7.00, 9.21) in cups and place the cups in positions 1, 2, and 3 respectively
2. CAREFULLY open the small gray cap on the pH probe, add KCl if needed
3. Insert the probe behind the Temperature Sensor and either across from, or in front of the acid line
     The stirrer stirs clockwise, so in order to get accurate readings, the acid line should not be directly behind the pH probe
4. On the LABX main page, click on analysis (bottom left of the screen), select the calibration method (pH Cal), click on the green start button at the top of the screen
5. On the LABX main page, top left - click on the Work Bench to see the sample being measured
6. FOR THE BUFFERS a variation between 0 and 0.3 is acceptable. If it is greater than that, use newer buffers and repeat the calibration process
7. When the calibration is completed, on the LABX mainscreen, open the DATA and click on MY LATEST RESULTS
8. In the results details section you will have the values for the slope and zero point, record this on the logging sheet
9. In the measured values section you will have the results pH 4.01, 7.00, 9.21 record these values on the logging sheet
10. Record the temperature of the buffers measured during the calibration
11. Refer to the calculation and recording data section before going any further

## Calculation and recording data

1. On the desktop open the pH calibration excel sheet
2. On the CALIBRATION sheet, Highlight from the date row all the way to the end of the graph, COPY and PASTE lower
3. In the copied portion, enter today's date, the new values from the pH (the ones on the logging sheet), graph the new data and use the slope term to calculate the pH values of 3 and 3.5
4. Record the pH values for 3.5 and 3 on the logging sheet
5. On the LOG sheet, you can now enter the values for all the pH, the slope and zero point and the temperature
6. On the CRM sheet you can enter the date, batch #, CRM batch
7. You can also prepare the folder for the analysis, on the desktop open the TAcalculations folder
8. In the DATA folder, create a new folder, with name of the samples and date, a name that will help you identify easily the samples you are measuring
9. In that folder, create two more folders: Mass and TitrationFiles
10. In the Mass folder create an excel spreadsheet with two columns, in column A you will enter the sample names and column B titled Mass you will enter the weight of the samples. Save it as an CSV file, this is really important and named: Mass08012016 for example (Mass plus the date without any space in the name)
11. In the TitrationFiles folder you will put the results from the titrator for each samples always save the files as CSV
12. Open R, you only need to change the files name for the path and massfile (row 20 and 21)   the date (row 23)  and the values for pH 3.5 and pH 3 (row 26 and 27) DO NOT CHANGE ANYTHING ELSE and at the end of the day DO NOT SAVE THE R file

## 3. Measuring the CRM (CO2 Reference Materials) sample

#### Purge Acid Line

1. On the touchscreen of the titrator, press ```PURGE 3x```, press ```START```.
2. After the purging cycle, press the left blue button on top of the Rondolino to turn carousel 180˚and remove the acid cup.
3. Discard the acid in the hazardous waste jug.
4. Rinse the acid cup with DI water and leave inverted on drying rack above sink.
5. Add 60mL of fresh DI water to the DI cup and place in position zero.
6. Press the left blue button on top of the Rondolino to rotate carousel 180˚ back to position zero.

## Measuring the CRM (CO2 Reference Materials) sample

1. Using the serological pipet, measure between 99.5 and 100.5 g of CRM in a cup
2. Record the mass on the logging sheet
3. Place the cup in position 1
4. On the LABX mainsheet, highlight the CSUN method option, this is the correct method to measure samples
5. Click on start
6. Click on TitratorSorte
7. On the next page enter the number of samples you are running, in this case 1
8. Enter the name of the sample CRM
9. Enter the weight of the sample and press OK
10. Open the workbench sheet to see the sample being measured
11. Enter the time of the beginning of the analysis on the logging sheet
12. It will take about 12 minutes
13. At the end, on the main page, open the results and click on the most recent result sets
14. Under the measured values, close the graph and open the sheet with the values, click on the second set of double values
15. Right click on the mouse and copy all as a text
16. Open a new excel sheet, paste the values and save it as a CSV file in the TitrationFiles folder with the name of the sample, example, CRM.csv
17. In the Mass folder in your current mass excel spreadsheet, ex: Mass08012016, enter the weight of the CRM samples
18. In the R program click on source and a new excel sheet will appear in your data folder of the day
19. In the excel sheet you will have the TA value of the CRM
20. Enter the CRM value on the logging sheet
21. Enter the CRM value on the pHCalibration excel sheet in the CRMsheet, calculate the % off, anything less than +/- 1% it is acceptable between the measured value and the actual value of the CRM batch

You are now ready to start processing samples.
The samples are processed the same way as the CRM, **refer to steps 1 through 18** in the measuring the CRM sample section.
The only difference is you **can add up to 9 samples**.
Once the samples have been analyzed, dump the waste in the waste container in the sink,
rinse all the cups with DI water and let them dry, and
all the solid waste (serological pipet, and paper towels used to soak a big spill from samples or CRM) can be dumped in the cardboard box next to fume hood

Recommendations

When beginning a new series of samples, doing duplicate of the first 5 samples is recommended

Rondolino:

*pH Probe Storage Procedures:*
- Temporary (No longer than a week) - can stay in the Rondolino in pH 4.0 Buffer
- Medium-term (No longer than a month) - move to the pH probe holder on the titrator, close gray cap
- Long-term (Longer than a month) - move to the pH probe holder on the titrator and place clear cap over the end containing KCl, close gray cap
