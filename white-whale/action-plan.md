# Action Plan for Systematic Dataset Identification

## Phase 1: NCBI Database Mining (Systematic Approach)

### 1.1 SRA Database Search
```bash
# Recommended search terms for NCBI SRA
# Primary species searches:
"Crassostrea gigas"[Organism] AND "RNA-Seq"[Strategy]
"Crassostrea gigas"[Organism] AND "Bisulfite-Seq"[Strategy]
"Magallana gigas"[Organism] AND "RNA-Seq"[Strategy]
"Magallana gigas"[Organism] AND "Bisulfite-Seq"[Strategy]

# Additional strategy searches:
"Crassostrea gigas"[Organism] AND ("transcriptome" OR "RNA-seq" OR "RNAseq")
"Crassostrea gigas"[Organism] AND ("methylation" OR "bisulfite" OR "MeDIP")
```

### 1.2 GEO Database Search
```bash
# Gene Expression Omnibus searches:
"Crassostrea gigas" AND ("RNA-seq" OR "transcriptome")
"Crassostrea gigas" AND ("methylation" OR "bisulfite")
"Magallana gigas" AND ("RNA-seq" OR "transcriptome")
"Magallana gigas" AND ("methylation" OR "bisulfite")
```

### 1.3 BioProject Database
- Search for umbrella projects containing multiple related studies
- Look for consortium projects and large-scale initiatives
- Identify project hierarchies and related datasets

## Phase 2: Literature Mining (Systematic Approach)

### 2.1 PubMed Search Strategy
```bash
# Comprehensive PubMed searches:
("Crassostrea gigas" OR "Magallana gigas") AND ("RNA-seq" OR "transcriptome" OR "transcriptomic")
("Crassostrea gigas" OR "Magallana gigas") AND ("methylation" OR "bisulfite" OR "epigenetic")
("Crassostrea gigas" OR "Magallana gigas") AND ("genome" OR "genomic") AND ("sequencing")
```

### 2.2 Journal-Specific Searches
- **Marine Biology journals**: Marine Environmental Research, Marine Biology, etc.
- **Genomics journals**: BMC Genomics, Molecular Ecology, G3, etc.
- **Aquaculture journals**: Aquaculture, Fish & Shellfish Immunology, etc.
- **Epigenetics journals**: Epigenetics, Environmental Epigenetics, etc.

### 2.3 Author-Based Searches
- Steven Roberts (University of Washington) - Known major contributor
- European oyster genomics researchers
- Asian aquaculture genomics groups
- Climate change impact researchers

## Phase 3: International Repository Search

### 3.1 European Nucleotide Archive (ENA)
- Search for European-funded studies
- Look for EMBARK consortium data
- Check for population genomics projects

### 3.2 DNA Data Bank of Japan (DDBJ)
- Asian Pacific oyster studies
- Japanese aquaculture research
- Korean and Chinese studies

### 3.3 Institutional Repositories
- Roberts Lab data servers
- European marine research institutes
- Asian aquaculture research centers

## Phase 4: Data Cataloging and Verification

### 4.1 Dataset Information Collection
For each identified dataset, collect:
- **Accession numbers**: SRA, GEO, BioProject IDs
- **Sample count**: Number of biological replicates
- **Tissue types**: Specific organs/tissues analyzed
- **Environmental conditions**: Experimental treatments
- **Technical details**: Sequencing platform, read length, depth
- **File sizes**: Actual or estimated data volume
- **Publication status**: Associated papers, citations

### 4.2 Data Quality Assessment
- **Completeness**: Full datasets vs. pilot studies
- **Technical quality**: Read depth, coverage metrics
- **Metadata quality**: Experimental design documentation
- **Access status**: Public, controlled access, or restricted

### 4.3 Size Estimation Verification
- **Download sample files**: Verify actual sizes
- **Calculate totals**: Sum across all identified datasets
- **Account for redundancy**: Remove duplicate samples
- **Update estimates**: Refine based on actual data

## Phase 5: Comprehensive Documentation

### 5.1 Dataset Inventory
Create structured database containing:
- Dataset catalog with all metadata
- Tissue type summary matrix
- Environmental condition categories
- Size estimates and totals
- Access instructions

### 5.2 Research Theme Analysis
- **Developmental biology**: Timeline and coverage
- **Environmental stress**: Stressor types and responses
- **Population genetics**: Geographic coverage
- **Epigenetics**: Methylation study types
- **Technical evolution**: Platform and method changes over time

### 5.3 Gap Analysis
Identify:
- **Underrepresented tissues**: Less-studied organ systems
- **Missing conditions**: Unstudied environmental factors
- **Technical gaps**: Missing methodological approaches
- **Temporal gaps**: Understudied life stages or time points

## Phase 6: Access Strategy Development

### 6.1 Prioritization Matrix
Rank datasets by:
- **Research relevance**: Alignment with research goals
- **Data quality**: Technical and experimental quality
- **Accessibility**: Ease of download and use
- **Completeness**: Full vs. partial datasets
- **Novelty**: Unique vs. redundant information

### 6.2 Download Planning
- **High-priority datasets**: Immediate download targets
- **Medium-priority datasets**: Secondary download list
- **Low-priority datasets**: Future consideration
- **Bandwidth planning**: Schedule large downloads appropriately

### 6.3 Storage Planning
- **Local storage**: Immediate analysis datasets
- **Archive storage**: Long-term reference datasets
- **Cloud storage**: Collaborative access options
- **Backup strategy**: Data preservation planning

## Expected Outcomes

### Quantitative Targets
- **Total datasets identified**: 50-100 unique studies
- **RNA-seq samples**: 400-600 individual samples
- **Methylation samples**: 200-400 individual samples
- **Total data volume**: 2-6 TB estimated
- **Publication coverage**: 2010-2024 time span

### Qualitative Outcomes
- **Comprehensive catalog**: Complete inventory of available data
- **Research roadmap**: Identified opportunities and gaps
- **Access strategy**: Practical plan for data acquisition
- **Collaboration opportunities**: Identified research connections

## Timeline Estimate
- **Phase 1-2**: 1-2 weeks (database and literature searches)
- **Phase 3**: 1 week (international repositories)
- **Phase 4**: 2-3 weeks (cataloging and verification)
- **Phase 5**: 1-2 weeks (documentation)
- **Phase 6**: 1 week (strategy development)
- **Total**: 6-9 weeks for comprehensive analysis

## Success Metrics
- **Completeness**: >90% of major datasets identified
- **Accuracy**: File size estimates within 20% of actual
- **Usability**: Clear access instructions for each dataset
- **Impact**: Enables new research through comprehensive resource

## Last Updated
December 2024