---
title: "Multi-Species Coral Transcriptomics via Tensor Decomposition"
subtitle: "Identifying Conserved Temporal Gene Expression Patterns Across Coral Species"
author: "Sam White"
date: "February 23, 2026"
---

# Project Overview

## Research Question

**How can we identify shared temporal gene expression patterns across evolutionarily divergent coral species?**

- Three coral species analyzed:
  - *Acropora pulchra*
  - *Porites evermanni*
  - *Pocillopora tuahiniensis*
- Multi-timepoint RNA-seq data (TP1-TP4)
- Focus on orthologous genes across species

---

# The Challenge

## Complexity of Multi-Species Transcriptomics

**Traditional approaches struggle with:**

1. **High dimensionality**: Thousands of genes × multiple species × multiple timepoints
3. **Biological variation**: Species-specific vs. conserved responses
4. **Temporal dynamics**: How patterns change over time
5. **Statistical power**: Limited biological replicates per species

**Need:** A unified framework that integrates all data dimensions simultaneously

---

# Why Tensor Decomposition?

## Advantages Over Traditional Methods

### Traditional Approaches (PCA, clustering, differential expression)
- **2D matrices**: Flatten data, losing structural information
- **Pairwise comparisons**: Species A vs B, Species A vs C, etc.
- **Separate analyses**: Time analyzed independently from species
- **Information loss**: Cannot capture 3-way interactions

### Tensor Decomposition
- **Native 3D structure**: Genes × Samples × Time
- **Unified framework**: All comparisons simultaneously
- **Latent factors**: Discover hidden patterns across all dimensions
- **Sparsity**: Focus on small subsets of genes/features
  - Most genes have near-zero loadings (inactive)
  - Few genes have strong loadings (active drivers)
  - Easier biological interpretation and hypothesis generation

---

# Why Barnacle Specifically?

## Method Selection Rationale

### Barnacle = Sparse CP Decomposition [@blaskowski2024]

**Key features:**
1. **Sparse regularization (λ)**: Identifies small sets of biologically relevant genes
   - L1 penalty shrinks most gene loadings to exactly zero
   - Only genes with strong, consistent signal remain
   - Transforms "all genes matter a little" → "these 50 genes matter a lot"
2. **Non-negativity constraints**: Biologically interpretable loadings
   - Positive values only (no negative expression contributions)
3. **Split-half bootstrap CV**: Optimized for limited replicates
4. **Factor stability metrics (FMS)**: Ensures reproducible patterns

**Alternative considered:** Standard CP decomposition lacks sparsity → harder biological interpretation

---

# Data Preparation Pipeline

## From Raw Counts to Tensor

1. **Ortholog Mapping**
   - Three-way ortholog groups via OrthoFinder
   - Filtered for complete matches across all species
   - Final: ~10,000 ortholog groups

2. **Sample Filtering**
   - Only samples with all 4 timepoints retained
   - Ensures temporal completeness

3. **Normalization**
   - sctransform (variance-stabilizing transformation)
   - Accounts for sequencing depth and gene-specific variation

4. **Tensor Construction**
   - Dimensions: Genes × samples × Timepoints
   - Missing values handled explicitly (filled with zeros)

---

# Model Optimization Strategy

## Two-Stage Parameter Selection via Bootstrap

### Stage 1: Rank Selection (λ=0.0)
- **Goal**: Determine optimal number of components (R)
- **Metric**: Cross-validation Sum of Squared Errors (SSE)
- **Selection rule**: 1SE rule (parsimony principle)
  1. Test all candidate ranks (e.g., 5, 10, 15, 20, 25, 30)
  2. Find rank with minimum mean SSE (e.g., rank=20)
  3. Calculate threshold: min_SSE + 1×SE
  4. Identify all ranks with SSE ≤ threshold (e.g., ranks 15, 20, 25)
  5. Choose **smallest rank** among those (e.g., rank=15)
  - Why smallest? Parsimony - prefer simpler model when performance is equivalent
  - Balances complexity vs. generalization

### Stage 2: Lambda Selection (fixed rank)
- **Goal**: Optimize sparsity parameter (λ)
- **Metric**: Factor Match Score (FMS)
- **Selection rule**: 1SE rule (maximum sparsity)
  - Maximum FMS - 1 standard error
  - Choose **maximum λ** within threshold
  - Maximizes interpretability while maintaining stability

---

# Cross-Validation Approach

## Split-Half Bootstrap Design

**Bootstrap features:**
- 50/50 train/test random splits
- Stratified by species (ensures balance)
- Multiple iterations (typically 20-100)
- Parallel execution for efficiency
- Incremental checkpointing (can resume if interrupted)

**Metrics tracked:**
- **SSE**: Prediction accuracy on held-out data
- **FMS**: Factor consistency across random initializations
- **Convergence rate**: Proportion of successful fits

---

# The 3D Tensor Structure

## Data Architecture

```
Tensor Shape: (n_genes, n_samples, n_timepoints)

Dimension 1 (Genes): 
  - Ortholog groups present in all three species
  - Filtered for expression data availability
  
Dimension 2 (Samples):
  - Combined species-sample units
  - Each sample labeled with species identity
  - Only complete temporal profiles included
  
Dimension 3 (Time):
  - 4 experimental timepoints (TP1, TP2, TP3, TP4)
  - Consistent across all species
```

---

# Decomposition Output

## Three Factor Matrices

### 1. Gene Factors (Genes × Components)
- Which ortholog groups contribute to each pattern
- Sparse loadings identify key gene modules
  - *Gene module* = set of co-expressed genes working together toward a biological function
  - Examples: "stress response module", "cell cycle module", "immune response module"
- Non-negative values ensure interpretability

### 2. Sample Factors (Samples × Components)
- Which species/samples exhibit each pattern
- Reveals species-specific vs. conserved responses
- Quantifies pattern strength per colony

### 3. Time Factors (Timepoints × Components)
- Temporal dynamics of each pattern
- Shows how patterns change over experimental time
- Identifies acute vs. sustained responses

**Component weights** indicate relative importance of each factor

---

# Key Results: Component Weights



---

# Key Results: Temporal Dynamics

## How Patterns Change Over Time

**Temporal profiles reveal:**


---

# Key Results: Species Patterns

## Conserved vs. Species-Specific Expression


---

# Key Results: Gene Modules

## Identification of Key Orthologs

**What is a gene module?**

A **gene module** is a coordinated set of genes that are:
- Co-expressed (turned on/off together)
- Functionally related (work toward common biological goal)
- Co-regulated (respond to same signals/transcription factors)

**Examples in biology:**
- "Heat shock response module": HSP70, HSP90, other chaperones activate together under stress
- "Cell cycle module": Cyclins, CDKs, checkpoint genes coordinately control division
- "Hypoxia response module": HIF-1α targets respond together to low oxygen

**In tensor decomposition:**
- Each component captures one gene module
- High-loading genes = core members of that module
- Sparsity ensures we identify true module members, not noise

---

**Top gene loadings per component identify:**


---

# Key Results: Sparsity Analysis

## Gene Loading Distribution

**Why sparsity matters for biological interpretation:**

### Without regularization (λ = 0):
- **Problem**: All ~2,500-4,000 genes have non-zero loadings
- Diffuse signal spread across many genes
- Which genes are actually important? Unclear.
- Difficult to design follow-up experiments
- "Everything is slightly correlated with everything"

### With sparse regularization (λ > 0):
- **Solution**: Penalty forces most loadings to exactly zero
- **Result**: 50-300 active genes per component
- Clear separation: active (>0.01) vs. inactive (≈0)
- **Biological value**: 
  - Tractable gene lists for functional enrichment
  - Candidate genes for experimental validation
  - Clearer mechanistic hypotheses

**The sparsity mechanism:**
1. λ penalty shrinks small loadings to zero
2. Only genes with strong, consistent signal survive
3. Focuses on genes that truly drive each pattern
4. Reduces noise while preserving biological signal

**Typical result:**
- 2-10% of genes active per component
- Component-specific variation in sparsity level
- Trade-off: more sparsity = simpler interpretation, but less variance explained


---

# Understanding Sparsity: A Visual Example

## Dense vs. Sparse Gene Loadings

### Scenario: Component representing "Stress Response"

**Without sparsity (λ = 0):**
```
Gene loadings distribution:
Gene 1: 0.15    Gene 501: 0.03   Gene 1001: 0.02
Gene 2: 0.12    Gene 502: 0.03   Gene 1002: 0.02
Gene 3: 0.11    Gene 503: 0.03   Gene 1003: 0.02
...             ...              ...
Gene 500: 0.04  Gene 1000: 0.02  Gene 2500: 0.01

Result: 2,500 genes all "matter" — which to study?
```

**With sparsity (λ = 0.5):**
```
Gene loadings distribution:
HSP70: 0.45         All other 10,000 genes: 0.00
HSP90: 0.38
SOD1: 0.32          
CAT: 0.28           
GPX: 0.25           
... (more genes with loading > 0)

Result: N genes clearly drive this pattern → functionally coherent
```


---

# Model Performance Metrics

## Convergence and Stability

### Convergence diagnostics:
- **Reconstruction error**: Monotonic decrease over iterations
- **Convergence status**: Achieved within max iterations
- **Final error**: Typically 1e-4 to 1e-6 range

### Stability metrics:
- **Factor Match Score (FMS)**: >0.85-0.95 indicates stable factors
- **Coefficient of variation**: <20% across bootstrap iterations
- **Cross-validation SSE**: Low variation indicates robust predictions

**Interpretation:**
- High FMS + low CV → Trustworthy biological patterns
- Poor convergence → May need different parameters or preprocessing

---

# Comparison: Why Not Just Use PCA?

## Tensor Decomposition vs. PCA

| Aspect | PCA | Tensor Decomposition |
|--------|-----|---------------------|
| **Data structure** | 2D matrix (flattened) | Native 3D structure |
| **Comparisons** | One dimension at a time | All dimensions simultaneously |
| **Gene × Time interaction** | Lost | Captured in factors |
| **Species patterns** | Separate analysis needed | Unified in sample factors |
| **Interpretability** | Linear combinations | Sparse, non-negative loadings |
| **Sparsity** | Dense PCs | Sparse factors (with λ) |
| **Biological relevance** | Harder to interpret | Direct gene/time/sample mappings |

**Bottom line:** Tensor decomposition preserves the natural structure of multi-way biological data

---

# Comparison: Why Not Just Use Clustering?

## Tensor Decomposition vs. K-Means/Hierarchical Clustering

| Aspect | Clustering | Tensor Decomposition |
|--------|-----------|---------------------|
| **Assignment** | Hard clusters (discrete) | Soft loadings (continuous) |
| **Multi-membership** | Genes in one cluster only | Genes contribute to multiple components |
| **Temporal dynamics** | Static clusters | Dynamic temporal profiles |
| **Cross-species** | Separate clusterings | Integrated sample factors |
| **Variance explained** | Not quantified | Component weights explicit |
| **Statistical framework** | Distance-based | Model-based with CV |

**Key advantage:** Genes can participate in multiple biological modules with varying strengths

---

# Comparison: Why Not Differential Expression?

## Tensor Decomposition vs. DESeq2/edgeR

| Aspect | Differential Expression | Tensor Decomposition |
|--------|------------------------|---------------------|
| **Scope** | Pairwise comparisons | Unified multi-way analysis |
| **Questions answered** | Which genes differ? | What are the latent patterns? |
| **Species integration** | Multiple comparisons | Single model |
| **Time as factor** | Discrete contrasts | Continuous temporal profiles |
| **Pattern discovery** | Hypothesis-driven | Hypothesis-generating |
| **Multiple testing** | Severe penalty | Built into model |

**Complementary approaches:**
- DE: Validate specific hypotheses
- Tensor: Discover unexpected patterns across all dimensions

---



# Biological Insights

## What We Can Learn

### Conserved responses:
- Identify evolutionarily conserved stress responses
- Universal coral gene modules under environmental change
- Candidate genes for climate resilience

### Species-specific adaptations:
- Which species have unique responses?
- Potential for differential thermal tolerance
- Species prioritization for conservation

### Temporal dynamics:
- Rapid vs. slow responses to stressors
- Recovery trajectories
- Critical timepoints for intervention

---

# Limitations and Considerations

## Important Caveats

### Biological:
- Limited to genes with three-way orthologs
- Species-specific genes excluded by design
- Temporal resolution limited to 4 timepoints
- Captive/experimental conditions

### Statistical:
- Relies on bootstrap stability with limited replicates
- Tensor decomposition assumes low-rank structure
- Model selection via cross-validation (not ground truth)
- Factors may not correspond to single biological processes

### Computational:
- Large parameter grids require substantial compute time
- Memory requirements for large tensors



---

# Key Takeaways

## Summary Points

1. **Tensor decomposition** preserves natural multi-way structure of transcriptomic data

2. **Barnacle (sparse CP)** provides interpretable, stable factors optimized for biological data

3. **Split-half bootstrap CV** enables robust parameter selection with limited replicates

4. **Three factor matrices** simultaneously reveal gene modules, species patterns, and temporal dynamics

5. **1SE rule** balances model complexity, sparsity, and generalization

6. **Sparsity regularization** identifies small sets of biologically relevant genes

7. **Unified framework** avoids multiple pairwise comparisons and information loss

8. **Complements traditional methods** (PCA, clustering, DE) rather than replacing them

---

# Software and Resources


### Barnacle Package:
- GitHub: [blasks/barnacle](https://github.com/blasks/barnacle)
- Dissertation: Blaskowski (2024) - *Tensor methods for integrative and interpretable multi-omics analysis*

---

# Acknowledgments

## Credits and References

### Method Development:
- **Barnacle sparse CP decomposition**: Blaskowski (2024)


### Software:
- sctransform, barnacle, tensorly, tidyverse
- R and Python communities

---

# Questions?

---

# References

Blaskowski, S. (2024). *Tensor methods for integrative and interpretable multi-omics analysis* [Doctoral dissertation]. Available via barnacle package documentation.

---
