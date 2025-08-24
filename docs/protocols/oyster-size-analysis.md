# Oyster Size Analysis from Images

Protocol for standardized measurement of oyster length and width from digital images, including procedures for field assessments such as the 10K seed assessments at Baywater.

Contact: ashuff (at) uw (dot) edu

## Standard Operating Protocol (SOP)

Written 20250127 for Issue #2282.

### Overview

This protocol provides standardized procedures for measuring oyster dimensions from digital photographs. It is designed for field assessments, outplant monitoring, and size-based growth studies. The protocol ensures consistent measurement approaches across multiple researchers and analysis sessions.

### Equipment and Software

**Required:**
- Computer with internet access
- Access to Google Sheets (or equivalent spreadsheet software)
- Image analysis software (ImageJ recommended, or similar)
- Digital images with scale reference (yellow scale bar)

**Optional:**
- Multiple monitors for efficient workflow
- Color-coded markers for tracking analyzed oysters

### Data Recording Standards

#### Google Sheets Setup

Create a Google Sheet with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| Image | Full filename of analyzed image | `tag309_20250820.jpeg` |
| Date | Date from filename (YYYYMMDD format) | `20250820` |
| Tag | Yellow tag ID or bag identifier | `309` |
| Oyster | Sequential oyster number per image | `1`, `2`, `3`, etc. |
| Length.mm | Maximum length measurement in mm | `26.2` |
| Width.mm | Maximum width measurement in mm | `14.5` |

**Important Notes:**
- Use consistent naming: `Length.mm` and `Width.mm` (note the period before mm)
- Record all measurements to one decimal place
- Use sequential oyster numbering starting from 1 for each image
- When multiple people are working simultaneously, coordinate to avoid analyzing the same images

### Image Analysis Procedure

#### Step 1: Image Preparation

1. Open the image in your analysis software (ImageJ recommended)
2. Locate the yellow scale bar in the image
3. Identify the tag number from either:
   - Yellow tag visible in the image
   - Tag number written on paper in the image
   - Filename (most reliable source)

#### Step 2: Scale Calibration

1. Use the line tool to measure the known length of the yellow scale bar
2. Set the scale in your software (Set Scale function in ImageJ)
3. Ensure measurements will be recorded in millimeters
4. Verify calibration accuracy by measuring the scale bar again

#### Step 3: Oyster Identification and Marking

1. Survey the entire image to count total oysters present
2. Plan your measurement strategy to avoid measuring the same oyster twice
3. Consider marking oysters as you measure them (if using annotation tools)
4. Start with larger, clearly visible oysters and work toward smaller ones

#### Step 4: Measurement Protocol

For each oyster:

1. **Length Measurement:**
   - Identify the longest dimension of the oyster shell
   - Draw a line from one end to the other along this maximum length
   - Record measurement to one decimal place

2. **Width Measurement:**
   - Identify the widest dimension perpendicular to the length
   - Draw a line across the maximum width
   - Record measurement to one decimal place

3. **Data Entry:**
   - Enter measurements immediately into the Google Sheet
   - Use the sequential oyster number (oyster1, oyster2, etc.)
   - Double-check tag number and image filename

#### Step 5: Quality Control

1. Review measurements for obvious errors (extremely large or small values)
2. Ensure all visible oysters in the image have been measured
3. Verify that oyster count matches the data entries
4. Check that scale calibration remained consistent throughout analysis

### Best Practices

#### Measurement Consistency

- **Length Definition:** Always measure the longest visible dimension of the shell
- **Width Definition:** Always measure the widest dimension perpendicular to length
- **Overlapping Oysters:** If oysters overlap, measure only clearly visible portions
- **Broken Shells:** Only measure complete shells; note damaged shells in comments if needed
- **Orientation:** Measurements should be independent of oyster orientation in image

#### Workflow Efficiency

- **Multiple Images:** Process images in filename order to maintain organization
- **Batch Processing:** Complete scale calibration for similar images together
- **Regular Breaks:** Take breaks every 30-45 minutes to maintain accuracy
- **Data Backup:** Save Google Sheet frequently during analysis

#### Team Coordination

- **Image Assignment:** Use a separate tracking sheet to assign images to team members
- **Progress Updates:** Update team on completed images regularly
- **Quality Checks:** Have experienced team member spot-check measurements periodically
- **Communication:** Use consistent communication channel for questions and issues

### Troubleshooting

#### Scale Bar Issues

- **Scale bar not visible:** Check image orientation; may need to rotate
- **Scale bar damaged:** Use known size reference objects if available
- **Multiple scale bars:** Use the yellow scale bar when available

#### Measurement Challenges

- **Clustered oysters:** Focus on clearly separated individuals
- **Image quality:** Skip obviously blurred or unusable images
- **Size extremes:** Double-check very large (>50mm) or very small (<5mm) measurements

#### Software Issues

- **ImageJ crashes:** Save measurements frequently; restart and re-calibrate
- **Google Sheets access:** Ensure proper sharing permissions are set
- **Data entry errors:** Use Find & Replace to correct systematic errors

### Data Export and Sharing

#### File Management

1. **Naming Convention:** Use descriptive names for analysis sessions
   - Example: `Baywater_20250820_SizeAnalysis_InitialsDate`
2. **Data Backup:** Export CSV copies of completed data
3. **Version Control:** Use Google Sheets revision history for tracking changes

#### Final Data Review

1. Check for missing entries or obvious outliers
2. Verify total oyster counts match expectations
3. Ensure all images have been analyzed
4. Generate summary statistics (mean, range, count by tag)

### Integration with Existing Protocols

This protocol complements existing lab protocols:

- **Resazurin Assay Protocol:** Size measurements for metabolic rate normalization
- **Outplant Monitoring:** Growth tracking over time
- **Survival Assessments:** Size-mortality relationships

For additional protocols and examples, see:
- [Resazurin Assay Protocol](resazurin-assay.md)
- [Size measurement examples](https://github.com/RobertsLab/polyIC-larvae/blob/main/data/resazurin/size.csv)

### Example Data Sheet

```
Image,Date,Tag,Oyster,Length.mm,Width.mm
tag309_20250820.jpeg,20250820,309,1,26.2,14.5
tag309_20250820.jpeg,20250820,309,2,28.9,16.5
tag309_20250820.jpeg,20250820,309,3,27.4,13.1
tag310_20250820.jpeg,20250820,310,1,15.3,9.8
tag310_20250820.jpeg,20250820,310,2,22.1,12.4
```

### Analysis Notes

- **Expected Range:** Oyster lengths typically range from 5-50mm for seed populations
- **Size Distribution:** Expect normal distribution with some skewing toward smaller sizes
- **Measurement Precision:** Aim for ±0.5mm accuracy in measurements
- **Time Requirements:** Allow 2-5 minutes per oyster depending on image complexity

### Reporting

Include in analysis reports:
- Total number of images analyzed
- Total number of oysters measured
- Size distribution summary statistics
- Any systematic issues encountered
- Quality control measures applied

This protocol ensures standardized, reproducible measurements across different researchers and analysis sessions while maintaining efficiency and accuracy.