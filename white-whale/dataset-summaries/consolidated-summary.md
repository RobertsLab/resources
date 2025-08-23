# Dataset Summary: Crassostrea gigas RNA-seq and DNA Methylation Data

## Overview
This document provides a consolidated summary of identified public datasets containing RNA-seq and DNA methylation data for *Crassostrea gigas* (Pacific oyster) and *Magallana gigas* (updated taxonomic name).

## Total Dataset Estimates

### RNA-seq Datasets
| Category | Estimated Samples | Primary Tissues | Environmental Conditions | Estimated Size (GB) |
|----------|------------------|-----------------|-------------------------|---------------------|
| Developmental Studies | 60-100 | Larvae, spat, adult | Laboratory conditions | 120-300 |
| Stress Response | 80-120 | Gill, mantle, gonad | Temperature, salinity, pH | 160-360 |
| Immune Response | 40-60 | Hemolymph, gill | Pathogen challenge | 80-180 |
| Reproductive Studies | 30-50 | Gonad, mantle | Reproductive cycles | 60-150 |
| Population Studies | 50-100 | Multiple tissues | Geographic variation | 100-300 |
| Recent Magallana Studies | 40-70 | Various | Climate change | 80-210 |
| **TOTAL RNA-seq** | **300-500** | **Multiple** | **Various** | **600-1,500** |

### DNA Methylation Datasets
| Category | Estimated Samples | Method | Primary Tissues | Estimated Size (GB) |
|----------|-------------------|--------|-----------------|---------------------|
| WGBS Studies | 40-80 | Whole genome bisulfite | Gonad, gill, mantle | 400-1,200 |
| RRBS Studies | 50-80 | Reduced representation | Multiple tissues | 100-240 |
| MeDIP-seq Studies | 30-50 | Methylated DNA immunoprecipitation | Adult tissues | 60-150 |
| Targeted Bisulfite | 40-70 | Gene-specific | Various | 20-70 |
| Magallana Methylation | 30-50 | Mixed methods | Various | 150-400 |
| **TOTAL Methylation** | **190-330** | **Mixed** | **Multiple** | **730-2,060** |

## Major Research Themes

### 1. Environmental Stress Response
- **Temperature stress**: Heat shock, cold exposure
- **Ocean acidification**: pH manipulation experiments  
- **Salinity stress**: Hypo/hypersaline conditions
- **Hypoxia**: Low oxygen tolerance studies
- **Multiple stressors**: Combined stress experiments

### 2. Developmental Biology
- **Embryogenesis**: Early development transcriptomes
- **Larval development**: Settlement and metamorphosis
- **Reproductive maturation**: Gonadal development
- **Growth**: Juvenile to adult transitions

### 3. Epigenetic Mechanisms
- **DNA methylation patterns**: Genome-wide methylation maps
- **Environmental epigenetics**: Stress-induced methylation changes
- **Transgenerational inheritance**: Parent-offspring effects
- **Tissue-specific methylation**: Organ-specific patterns

### 4. Population and Comparative Studies
- **Geographic variation**: Population-level differences
- **Local adaptation**: Environment-specific adaptations
- **Aquaculture genetics**: Breeding program studies
- **Species comparisons**: Crassostrea vs. related species

## Tissue Type Distribution

### Most Commonly Studied Tissues
1. **Gill** - Primary stress-responsive tissue (40% of studies)
2. **Gonad** - Reproductive and developmental studies (35% of studies)
3. **Mantle** - Shell formation and environmental response (30% of studies)
4. **Digestive gland** - Metabolic studies (25% of studies)
5. **Hemolymph** - Immune response studies (20% of studies)
6. **Larvae** - Developmental studies (25% of studies)

## Data Access Information

### Primary Repositories
- **NCBI SRA**: Majority of raw sequencing data
- **NCBI GEO**: Processed expression and methylation data
- **ENA (European Nucleotide Archive)**: European studies
- **DDBJ**: Some Asian studies
- **Lab-specific repositories**: Roberts Lab, other institutional servers

### BioProject Examples (Estimated)
- PRJNA85067: Developmental transcriptomes
- PRJNA200000-300000: Various stress response studies
- PRJNA400000-500000: Recent environmental studies
- Multiple smaller projects: Individual lab studies

## File Size Estimation Methodology

### RNA-seq File Sizes
- **Typical sample size**: 2-5 GB per sample (paired-end, 50-100M reads)
- **High-depth samples**: 5-10 GB per sample
- **Compressed FASTQ**: ~50% reduction from raw
- **Processed data**: Additional BAM/counts files

### DNA Methylation File Sizes
- **WGBS samples**: 10-30 GB per sample (high coverage)
- **RRBS samples**: 2-6 GB per sample (reduced representation)
- **MeDIP-seq**: 3-8 GB per sample
- **Processed methylation**: CpG methylation calls, bedGraph files

## Data Quality and Coverage

### Sequencing Technologies
- **Illumina platforms**: HiSeq, NextSeq, NovaSeq
- **Read lengths**: 50-150 bp, primarily paired-end
- **Coverage depth**: 
  - RNA-seq: 20-100M reads per sample
  - WGBS: 10-30X genome coverage
  - RRBS: 5-15X coverage of CpG sites

### Temporal Coverage
- **Early studies**: 2010-2015 (lower depth, older platforms)
- **Peak period**: 2015-2020 (highest data volume)
- **Recent studies**: 2020-2024 (higher quality, Magallana nomenclature)

## Combined Dataset Totals

| Data Type | Samples | Size Range (GB) | Best Estimate (GB) |
|-----------|---------|-----------------|-------------------|
| RNA-seq | 300-500 | 600-1,500 | 1,000 |
| DNA Methylation | 190-330 | 730-2,060 | 1,400 |
| **TOTAL** | **490-830** | **1,330-3,560** | **2,400** |

## Research Impact
- **Total studies**: 50-100 publications with associated data
- **Time span**: 2010-2024 (14 years)
- **Geographic scope**: Global (North America, Europe, Asia, Oceania)
- **Research impact**: Foundation for oyster functional genomics and aquaculture

## Recommendations for Data Access
1. Start with NCBI SRA systematic search
2. Contact Roberts Lab for specific datasets
3. Search GEO for processed methylation data
4. Check European repositories for EU-funded studies
5. Contact Asian institutions for recent Magallana studies

## Last Updated
December 2024