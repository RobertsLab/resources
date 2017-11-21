## Titrator SOP

Orginally developed by Genevieve Bernatchez and Nyssa Silbiger 07/18/2016

---

*Put on your PPE: lab coat, protective glasses, and gloves*

Rondolino: Have the right blue dial on top of the Rondolino turned to position 1. This will not condition, but will rinse with DI water for 2 sec.

Starting the instrument (purging acid line)

1. Turn on the Computer next to the Titrator and open LabX
2. Turn the titrator ON (front button)
3. Turn the Rondolino ON (back switch)
4. Press the left blue button on top of the Rondolino arm (turns sample changer 180˚)
5. Take the DI water cup out from position zero
6. Place an empty cup in position zero
7. Press the left blue button to turn 180˚ back to position zero
      We want to purge the line from the acid bottle to the instrument of air bubbles
8. To purge, on the touchscreen of the instrument, click Burette Rinse, click START. Repeat this process 3 times and be certain that there are no bubbles left in the line
9. After the purging cycle, press the button to turn 180˚ and remove the acid cup
10. PUT THE ACID BACK in the brown bottle - open the cap and carefully dump the acid
11. ADD fresh DI water to the DI cup and place in position zero. Turn 180˚ again
12. Prepare the logging sheet of the day; enter the date, ...

pH Calibration

pH Probe Storage Procedures:
Temporary (No longer than a week) - can stay in the Rondolino in DI water
Medium-term (No longer than a month) - move to the pH probe holder on the titrator, close gray cap
Long-term (Longer than a month) - move to the pH probe holder on the titrator and place clear cap over the end containing KCl, close gray cap

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
12. Remove the buffers and put them back in their respective containers
13. Put the empty cups in the sink

Calculation and recording data

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

Measuring the CRM (CO2 Reference Materials) sample

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
The samples are processed the same way as the CRM, *refer to steps 1 through 18* in the measuring the CRM sample section.
The only difference is you can add up to 9 samples.
Once the samples have been analyzed, dump the waste in the waste container in the sink,
rinse all the cups with DI water and let them dry, and 
all the solid waste (serological pipet, and paper towels used to soak a big spill from samples or CRM) can be dumped in the cardboard box next to fume hood

Recommendations

When beginning a new series of samples, doing duplicate of the first 5 samples is recommended
