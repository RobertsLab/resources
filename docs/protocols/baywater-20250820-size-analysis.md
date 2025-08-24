# 20250820 Baywater 10K Seed Size Analysis - Quick Reference

This document provides quick reference information for the specific analysis requested in Issue #2282.

## Analysis Overview

- **Images to analyze:** 28 total from 20250820 Baywater assessment
- **Image source:** [GitHub repository](https://github.com/RobertsLab/polyIC-larvae/tree/main/data/outplant/sequim/size)
- **Data recording:** [Google Sheet](https://docs.google.com/spreadsheets/d/1lMRYigEF_9f2LICe4q8nRxW6kDCUw_nqdVwaQIxlThg/edit?gid=0#gid=0)

## Required Data Format

Google Sheet columns (exactly as specified):

| Image | Date | Tag | Oyster | Length.mm | Width.mm |
|-------|------|-----|--------|-----------|----------|
| `tag309_20250820.jpeg` | `20250820` | `309` | `1` | `26.2` | `14.5` |

## Key Points

1. **Date:** All entries should use `20250820` 
2. **Tag numbers:** Extract from yellow tags in images or from filename
3. **Oyster numbering:** Sequential (1, 2, 3...) per image
4. **Measurements:** Record to one decimal place in mm
5. **Scale reference:** Use yellow scale bar in each image
6. **Coordination:** Multiple people working - coordinate to avoid overlap

## Essential Steps

1. Open image in ImageJ (or similar software)
2. Calibrate scale using yellow scale bar
3. Measure maximum length and width for each oyster
4. Mark oysters as analyzed to avoid double-counting
5. Record data immediately in Google Sheet
6. Use sequential oyster numbers starting from 1 for each image

## Quality Control

- Double-check tag numbers match between image and filename
- Verify scale calibration for each image
- Review measurements for obvious errors
- Ensure all visible oysters are measured

## For Complete Protocol

See the full [Oyster Size Analysis Protocol](oyster-size-analysis.md) for detailed procedures, troubleshooting, and best practices.

---

**Contact:** ashuff (at) uw (dot) edu for questions about this analysis.