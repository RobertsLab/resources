## Resazurin metabolic assay 

Resazurin metabolic assays are used to measure the metabolic rate of marine organisms. This protocol has been developed for use in oysters, but can be adapted for other organisms.   

Contact: ashuff (at) uw (dot) edu

### Standard Operating Protocol (SOP)
Updated 20250813 by Ariana Huffmyer.  

#### Repository 

Example data sets, scripts, and resources can be found at [our GitHub repository here](https://github.com/RobertsLab/resazurin-assay-development). 

#### Overview 

This protocol details general approaches for resazurin metabolic rate measurements in oysters. The protocol can be adapted for various sizes, temperature profiles, or different stress exposures following this base protocol.  

#### Materials and preparing solutions

##### Stock resazurin solution 

To make the resazurin stock solution (10 mL) mix the following. We will use this solution for multiple trials.  

- [0.5 g resazurin salt](https://www.thermofisher.com/order/catalog/product/R12204)
- 10 mL DI water
- 10 µL DMSO

Store in a dark fridge or freezer.  

##### Containers 

Here are some suggested vessels for conducting trials. The animals should be fully submerged. 

- Small seed (<7mm length): trials conducted in 48 or 96 well plates 
- Medium seed (15-40 mm length): trials conducted in 12 or 24 well plates or small plastic cups 
- Large seed/adults (>40 mm length): trials can be conducted in tripour cups, beakers, or plastic cups. Scale volume appropriately. 

We recommend performing preliminary trials to ensure that a change in resazurin fluorescence can be detected over the time scale desired. 

##### Sample sizes 

Plan your sample sizes appropriately depending on your research question. Metabolic rates are variable, so we recommend at least n=20 per experimental group as a minimum (higher replication is best). 

When selecting containers and volume of solutions, remember to account for blanks. We recommend if you use plates that you include n=3-8 blanks per plate and if using cups, we recommend n=5-10 blanks per temperature/stress/experimental treatment. 

##### Working resazurin solution

First, determine the volume of resazurin required depending on the size of your organism, the number of blanks and samples, and the container size as described above. 

To prepare the working solution of resazurin, prepare the following. 

-   Desired working volume x 0.98666 = ___ mL filtered seawater (DI water with Instant Ocean adjusted to 23-25 ppt
    or filtered (\<1um) seawater) 

-   Desired working volume x 0.00222 = ___ mL resazurin stock solution as made above in step 1 

-   Desired working volume x 0.001 = ___ mL DMSO

-   Desired working volume x 0.01 = ___ mL  antibiotic solution [100x Penn/Strep & 100x Fungizone](https://us.vwr.com/store/product/4648458/null). This should be kept frozen in a dark freezer and thawed before use (thaw in the dark or cover with aluminum foil)
    
Store at 4°C in dark fridge until use. We recommend making a fresh batch of working stock within 7 days of use.  

For example, here is a recipe for 150 mL of working stock. 

- 148 mL seawater 
- 333 µL resazurin stock solution 
- 150 µL DMSO
- 1.5 mL antibiotic solution  

3. Supplies 

- Bench top incubators 
- [Temperature loggers](https://www.onsetcomp.com/products/data-loggers/mx2203) to be placed in incubators at treatment conditions 
- Paper towels and bench paper/pads 
- Tweezers, transfer pipettes, and forceps 
- Dissecting microscope 
- Spectrophotometer plate reader that detects fluorescence and associated software
- Plate reader filters (if required) with excitation wavelength of 530 and emission wavelength of 590 (we are currently using an excitation 528 wavelength filter with a bandpass of 20 and an emission 590 wavelength filter with a bandpass of 20)  
- Pipettes and tips 
- Scale bar/ruler
- Camera/phone camera
- Plastic cups, beakers, plates, or other vessel for incubations
- Plates, cups, or beakers 

Label plates with identifying number (e.g. "Plate 1", "Plate 2") or label cups with unique numbers/identifiers.    

#### Protocol

Conduct measurements at treatments desired. We typically conduct measurements at a control temperature and a high temperature. If multiple treatments are desired over multiple days, be sure to run a control treatment each day as reference. Ensure you account for tank effects or other batch effects by randomizing loading order, position in incubators, etc. 

For oysters, we have used the following treatments to detect metabolic responses to stress: 

- For acute stress and survival testing: control temperature (10-20°C) and acute high temperature (36-42°C)
- For thermal performance testing: control temperature (10-20°C), and a gradient of temperatures from 25°C-45°C. 
- Acute stress (40°C) for 2 hours followed by cooling/stabilizing temperatures (counter top or fridge for 2 hours) 
- Static measurements at non stressful temperatures to characterize metabolic rate variability between groups (e.g., 28°C) 

We strongly recommend preliminary testing to determine appropriate temperature treatments for your study system and research question.  

#### Time points 

Resazurin measurements should be collected on a timescale appropriate for your research question. Typically, we run assays over a 3-6 hour period with measurements collected every 30-60 minutes. For example, here is a typical schedule for a day in which we are conducting 5 hour incubations at a control and high temperature. 

08:00-09:00: Load plates with oysters, take size images, and load resazurin solution   
09:00: Time 0 measurement   
10:00: Time 1 measurement   
11:00: Time 2 measurement  
12:00: Time 3 measurement  
13:00: Time 4 measurement   
14:00: Time 5 measurement 
14:00-16:00: Clean up and assess survival (if needed)  

#### Load and prepare samples  

Before starting, set the incubator at the desired temperature or set up your treatments.  

1. Prepare animals for assays. Track the source tank, treatment, or other identifying information. 
2. Add animals into labeled plates or containers and placing them into the empty container.
3. Add blanks (see recommendations above). 
4. Write the location of wells on a plate map if using plates. 
5. Allocate the animals either into their designated cup or onto the lid of the plate. 
6. Take images of each animal with a scale bar with their identifying information in the photograph. See an example below.  
7. Move the animals into their respective wells in the plate if you placed them on the lid for a photograph. 
8. Fill each well with the desired amount of resazurin working stock at ambient temperature using a microchannel pipette or graduated cylinder. 

An example of photograph for size measurements:  

![](https://github.com/AHuffmyer/ASH_Putnam_Lab_Notebook/blob/master/images/NotebookImages/oysters/polyic/20250310/20240310_plate1.jpeg?raw=true)  

Measure size using ImageJ or other imaging software. We typically use maximum shell length (mm) for size normalization.  

For detailed protocols on standardized oyster size analysis from images, see [Oyster Size Analysis Protocol](protocols/oyster-size-analysis.md).  

#### Measurements 

1. Turn on the computer and plate reader. Open the plate reader software.
2. Create a new protocol that conducts end point measurements from the top of the plate using an excitation wavelength of 530 and emission wavelength of 590 nm. 
3. Name the protocol and save. This process may vary depending on your instrument.
4. Take a T0 initial measurement - this is critical! If using a plate, you can place the plate with the animals directly on the plate reader (do not have the lid on the plate). If you have animals in cups, take a small sample (250uL) of the resazurin liquid from each container, place into a 96-well plate, and then conduct the measurements. If you use this method, be sure to make a plate map of the location of the samples and identifying information. Conduct measurements for blanks and samples.  
6. Collect and export readings as directed in the plate software. 
7. Save the file with a descriptive name. For example,  `YYYYMMDD_TemperatureTreatment_Plate#_T0.xlsx`. 
8. Save the data to a flash drive and add to GitHub or data repository. 
9. Record the time of the measurement.
10. Repeat for any remaining plates or treatments. 
11. Take temperature measurements in wells or cups if relevant. 
12. Move the animals to the incubator at their respective temperatures and record the temperature in the incubators. 
13. Repeat at 1, 2, 3, 4, and 5 hours of incubation as necessary for your experiment.  

#### Survival measurements 

1. Either each hour (if you can easily see the animals in larger cups) or at the end of the incubation (for animals in 96 well plates), conduct survival assessments. Note that it is critical to perform survival assessments so that you can analyze resazurin metabolic response for those that survive and those that die during the trials. If performing trials in 96 well plates or other small containers, we recommend performing survival assessment at the end of the incubation. If you are conducting trials in larger cups where you can see the animals without removing the resazurin solution, you can assess survival at each time point.  
2. If using plates, prepare a plate map for recording the assessments - this is an easy method to keep track of the assessments. If you are not using plates, make a list of all samples with columns for recording survival at each time point.  
3. If working with shellfish, use tweezers/forceps to take each animal out and examine in a petri dish filled with DI water under a dissecting scope. Determine if the oyster is dead by placing the cup side of the oyster down and gently taping/moving the shell. If the shell is open and remains open after tapping, the oyster is dead. If the shell is closed tight or closes after tapping, the oyster is alive. Use other determination methods for other organisms. 
4. Record any notes of oysters that were damaged by the tweezers or record any other notes of interest. 
5. After examining each oyster, move it to a beaker. Discard oysters after the measurements are done. 
6. Generate a data frame that has columns for sample ID, treatments, date, and other relevant information. Add a column designated "mortality" and add a 0 for alive and 1 for dead animals. Edit as required for your specific analysis. 

#### Waste disposal 

Resazurin solution can be washed down the sink and flushed with plenty of water. Rinse containers thoroughly.   

#### Data preparation and analysis  

Prepare the following data frames (see examples at our repository): 

- Size measurements: columns for sample ID, date, treatment, and size measurement (e.g., length in mm)
- Mortality assessment: columns for sample ID, date, treatment, and mortality assessment (e.g., 0 for alive and 1 for dead)
- Metadata: columns for sample ID, date, treatment, tank or batch effects, species, well/cup ID, and sample type (i.e., "blank" or "sample") 
- Resazurin files: files exported from plate reader software that contain fluorescence readings for each well of the plate

Conduct the following analysis steps (see R scripts available for use in our repository):  

- Read in data
- Normalize all fluorescence values to the initial time point (fluorescence at time X divided by fluorescence at time 0) - do this for samples and blanks
- Calculate the mean value for normalized blanks within each unit (e.g., mean of all blanks in each plate at each time point)
- Subtract the mean blank value from the fluorescence value of each sample from the respective unit and time point
- Size normalize the data by dividing fluorescence values by size of each sample
- Proceed with visualization and statistical analyses, including testing for effects of treatment or other effects of interest and examining metabolic differences between animals that lived and animals that died during the trials. See examples in our GitHub repository. 

## Aquarium nitrogen testing kit protocols (AQI test kit) 

Written by Noah Ozguner and Madeliene Baird 20250401.  

This protocol is written based on the [manufacturer's instructions](https://apifishcare.com/pdfs/products-us/saltwater-master-test-kit/api-saltwater-mastert-test-kit-instruction-manual.pdf). 

Test kit was [ordered here](https://www.amazon.com/API-MASTER-Aquarium-Water-1-Count/dp/B001D6Z7QW/ref=asc_df_B001D6Z7QW?mcid=f12e42d7505a391c8f7d47fcc7373e19&hvocijid=11467865304186403471-B001D6Z7QW-&hvexpln=73&tag=hyprod-20&linkCode=df0&hvadid=721245378154&hvpos=&hvnetw=g&hvrand=11467865304186403471&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9033456&hvtargid=pla-2281435179778&psc=1)

### Standard Operating Protocol (SOP)

After testing, do not pour contents back into the tank. Make sure to rinse test tubes after use. 

#### pH (kit minimum 7.4, maximum 8.8) 

- Fill a clean test tube with 5 ml of water 
- Add 5 drops of High range pH Test Solution
- Cap the test tube and invert it multiple times to mix the solution
- Read results by comparing the color of the solution to the provided pH color chart (in a relatively well lit area). The closest color match indicates the pH value of the water sample. 
- Thoroughly wash test tube after use

#### Ammonia (ppm or mg/L) [two bottles]

- Fill a clean test tube with 5 ml of water 
- Add 8 drops of Ammonia Test Solution 1
- Add 8 drops of Ammonia Test Solution 2
- Cap the test tube and shake vigorously for 5 seconds
- Wait 5 minutes for color to develop
- Read results by comparing the color of the solution to the provided Ammonia color chart. (in a relatively well lit area). The closest color match indicates the Ammonia value of the water sample. 
- Thoroughly wash test tube after use

#### Nitrite (ppm or mg/L)

- Fill a clean test tube with 5mL of water
- Add 5 drops of Nitrite Test Solution
- Cap the test tube and shake for 5 seconds
- Wait 5 minutes for color to develop
- Compare the color of the solution to the Nitrite Color Chart in a well lit area. The closest match will indicate the ppm (mg/L) of the nitrite in the sample
- Thoroughly wash test tube after use

#### Nitrate (ppm or mg/L) [two bottles]
- Fill a clean test tube with 5mL of water
- Add 10 drops of Nitrate Test Solution #1
- Cap the test tube and invert several times to mix the solution
- Vigorously shake the Nitrate Test Solution #2 for at least 30 seconds
- Add 10 drops of Nitrate Test Solution #2
- Cap the test tube and shake vigorously for 1 minute
- Wait 5 minutes for the color to develop
- Compare the color of the solution to the Nitrate Color Chart in a well lit area. The closest match will indicate the ppm (mg/L) of the nitrite in the sample
- Thoroughly wash test tube after use

#### Reference values 

Ammonia (NH3): Ammonia is highly toxic to fish and should always be 0 ppm.  

Nitrite (NO2): Nitrite is also toxic and should be 0 ppm.  

Nitrate (NO3): While less toxic than ammonia and nitrite, nitrate can still be harmful to fish and corals at high levels. Aim to keep nitrate levels below 20 ppm, and ideally between 0-5 ppm.  










