
# Annotation

## Intro (Blast)
Blast is a key component of working with lesser studied taxa. Here are some resources to help with this.

**First off, you should be familar with the command line interface and bash**

- [Introducing the Shell](https://swcarpentry.github.io/shell-novice/index.html)
- [Introduction to the Command Line for Genomics](https://datacarpentry.org/shell-genomics/)
- <https://explainshell.com/>

---


### Blast Notebooks
- <https://robertslab.github.io/tusk/modules/04-blast.html> - Blast and annotation on **tusk**.    
- <https://rpubs.com/sr320/1026094> - Blast tutorial from FISH 546 (2023)
- <https://github.com/RobertsLab/code/blob/master/09-blast.ipynb> - An example of how one might take a multi sequence fasta file and using NCBI Blast, compare the sequences with the Swiss-Prot Database on their own computer.

- <https://github.com/RobertsLab/code/blob/master/10-blast-2-slim.ipynb> - A notebook to seamlessly take blast output to GO Slim list

- <https://github.com/RobertsLab/code/blob/master/script-box/complete_go_annotation_notebook.Rmd> -

- https://github.com/sr320/ceabigr/blob/main/code/17-Swiss-Prot-Annotation.Rmd -  Blasting C virginica to Swiss-Prot. Author: Steven Roberts ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/ceabigr)

---

## Gene Ontology (GO)

### Retrieve GO terms from UniProt Using SwissProt IDs

The following steps will use the UniProt Python API to create a tab-delimited file of data retrieved from UniProt.

1. Create newline-delimited file of SwissProt IDs. (e.g. `SPIDS.txt`)

    ```bash
    cat SPIDS.txt

    Q86IC9
    P04177
    Q8L840
    Q61043
    A1E2V0
    P34456
    P34457
    O00463
    Q00945
    Q5SWK7
    ```

2. Create Python file (e.g. `uniprot-retrieval.py`) with the following:

    ```python
    import re
    import zlib
    import gzip
    import requests
    from requests.adapters import HTTPAdapter, Retry
    import sys
    import shutil
    import os
    
    re_next_link = re.compile(r'<(.+)>; rel="next"')
    retries = Retry(total=5, backoff_factor=0.25, status_forcelist=[500, 502, 503, 504])
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retries))
    
    def get_next_link(headers):
        if "Link" in headers:
            match = re_next_link.match(headers["Link"])
            if match:
                return match.group(1)
    
    def get_batch(batch_url):
        while batch_url:
            response = session.get(batch_url)
            response.raise_for_status()
            total = response.headers["x-total-results"]
            yield response, total
            batch_url = get_next_link(response.headers)
    
    def process_accessions(accessions):
        accession_batches = [accessions[i:i+500] for i in range(0, len(accessions), 500)]
        all_lines = []
    
        for accession_batch in accession_batches:
            accession_query = '%29%20OR%20%28accession%3A'.join(accession_batch)
            url = f"https://rest.uniprot.org/uniprotkb/search?compressed=true&fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Corganism_name%2Clength%2Cgo_p%2Cgo_c%2Cgo%2Cgo_f%2Cgo_id&format=tsv&query=%28%28accession%3A{accession_query}%29%29&size=500"
            
            progress = 0
            lines = []
            for batch, total in get_batch(url):
                # Decompress each batch as we want to extract the header
                decompressed = zlib.decompress(batch.content, 16 + zlib.MAX_WBITS)
                batch_lines = [line for line in decompressed.decode("utf-8").split("\n") if line]
                if not progress:
                    # First line so print TSV header
                    lines = [batch_lines[0]]
                lines += batch_lines[1:]
                progress = len(lines) - 1
                print(f"{progress} / {total}")
    
            all_lines.extend(lines)
    
        return all_lines
    
    def main(accession_file, output_dir):
        with open(accession_file, 'r') as f:
            accessions = f.read().splitlines()
    
        retrieved_data = process_accessions(accessions)
    
        # Write to a temporary gzip file
        temp_filename = "uniprot-retrieval-temp.tsv.gz"
        with gzip.open(temp_filename, "wt", encoding="utf-8") as f:
            f.write('\n'.join(retrieved_data))
    
        # Determine the full output path
        output_path = os.path.join(output_dir, "uniprot-retrieval.tsv.gz")
    
        # Merge the temporary file with the existing output file (if it exists)
        try:
            with gzip.open(output_path, "rb") as f_existing, open(temp_filename, "rb") as f_temp:
                with gzip.open("uniprot-retrieval-merged.tsv.gz", "wb") as f_merged:
                    shutil.copyfileobj(f_existing, f_merged)
                    shutil.copyfileobj(f_temp, f_merged)
            
            # Replace the original output file with the merged file
            shutil.move("uniprot-retrieval-merged.tsv.gz", output_path)
        except FileNotFoundError:
            # If the existing output file doesn't exist, rename the temporary file
            shutil.move(temp_filename, output_path)
    
    if __name__ == '__main__':
        if len(sys.argv) < 3:
            print("Usage: python uniprot-retrieval.py <input_file> <output_directory>")
            sys.exit(1)
    
        accession_file = sys.argv[1]
        output_dir = sys.argv[2]
    
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
        main(accession_file, output_dir)
    ```

3. Run the Python script:

    ```bash
    python3 uniprot-retrieval.py SPIDS.txt /path/to/desired/output/directory/
    ```
    - IMPORTANT: Requires Python >= 3!

    - If using R Markdown, run the above in a `bash` chunk:

 The resulting output file (`uniprot-retrieval.tsv.gz`) will be in the specified directory.

4. Gunzip the output file:

    ```bash
    gunzip uniprot-retrieval.tsv.gz
    ```

The resulting file (`uniprot-retrieval.tsv`) will be formatted with the following columns:

| Entry | Reviewed | Entry Name | Protein names | Gene Names | Organism | Length | Gene Ontology (biological process) | Gene Ontology (cellular component) | Gene Ontology (molecular function) | Gene Ontology (GO) | Gene Ontology IDs |
|-------|----------|------------|---------------|------------|----------|--------|------------------------------------|------------------------------------|------------------------------------|--------------------|-------------------|


NOTES:

- This requires Python >= 3 to run. Simplest way to access Python 3 is via a conda environment.

- On the first attempt, you'll likely need to install the packages that are being imported at the very beginning of the script.

- [Create an issue](https://github.com/RobertsLab/resources/issues) if you need help with any of the above.

### Map GO IDs to GOslims

Below are a series of R Markdown chunks to run.

The expected input file has at least two columns. One each with:

- gene ID
- Gene Ontology (GO) ID

NOTE: The GO IDs in the GO ID column should be separated with a semi-colon.

The basic output from this process will be:

- GOslim IDs (as rownames)
- GOslim terms
- Counts of GO IDs matching to corresponding GOslim
- Percentage of GO IDs matching to corresponding GOslim
- GOIDs mapped to corresponding GOslim, in a semi-colon delimited format

There are steps after this that perform different subsetting that you may/not be interested in. They've been left in to serve as examples.

Load libraries

````
```{r setup, include=TRUE}
library(GSEABase)
library(GO.db)
library(knitr)
library(tidyverse)
knitr::opts_chunk$set(
  echo = TRUE,         # Display code chunks
  eval = FALSE,        # Evaluate code chunks
  warning = FALSE,     # Hide warnings
  message = FALSE,     # Hide messages
  comment = ""         # Prevents appending '##' to beginning of lines in code output
)
```
````

Variables

IMPORTANT: The user needs to provide:

- names of the columns containing the GO IDs and the gene IDs!

- Path or URL to input file.

After that, there's almost no need to modify any of the chunks which follow.

````
```{r set-variables, eval=TRUE}
# Column names corresponding to gene name/ID and GO IDs
GO.ID.column <- "Gene.Ontology.IDs"
gene.ID.column <- "gene_id"

# Relative path or URL to input file
input.file <- "https://raw.githubusercontent.com/grace-ac/paper-pycno-sswd-2021-2022/d1cdf13c36085868df4ef4b75d2b7de03ef08d1c/analyses/25-compare-2021-2022/DEGlist_same_2021-2022_forGOslim.tab"


##### Official GO info - no need to change #####
goslims_obo <- "goslim_generic.obo"
goslims_url <- "http://current.geneontology.org/ontology/subsets/goslim_generic.obo"
```
````

Set GSEAbase location and download `goslim_generic.obo`
````
```{r download-generic-goslim-obo, eval=TRUE}
# Find GSEAbase installation location
gseabase_location <- find.package("GSEABase")

# Load path to GOslim OBO file
goslim_obo_destintation <- file.path(gseabase_location, "extdata", goslims_obo, fsep = "/")

# Download the GOslim OBO file
download.file(url = goslims_url, destfile = goslim_obo_destintation)

# Loads package files
gseabase_files <- system.file("extdata", goslims_obo, package="GSEABase")
```
````


Read in gene/GO file
````
```{r read-in-gene-file, eval=TRUE}
full.gene.df <- read.csv(file = input.file, header = TRUE, sep = "\t")

str(full.gene.df)
```
````

Remove rows with NA, remove whitespace in GO IDs column and keep just gene/GO IDs columns
````
```{r remove-NA-and-uniprotIDs, eval=TRUE}

# Clean whitespace, filter NA/empty rows, select columns, and split GO terms using column name variables
gene.GO.df <- full.gene.df %>%
  mutate(!!GO.ID.column := str_replace_all(.data[[GO.ID.column]], "\\s*;\\s*", ";")) %>% # Clean up spaces around ";"
  filter(!is.na(.data[[gene.ID.column]]) & !is.na(.data[[GO.ID.column]]) & .data[[GO.ID.column]] != "") %>% 
  select(all_of(c(gene.ID.column, GO.ID.column)))


str(gene.GO.df)
```
````


This flattens the file so all of the GO IDs per gene
are separated into one GO ID per gene per row.
````
```{r flatten-gene-and-GO-IDs, eval=TRUE}
flat.gene.GO.df <- gene.GO.df %>% separate_rows(!!sym(GO.ID.column), sep = ";")

str(flat.gene.GO.df)
```
````


Groups the genes by GO ID (i.e. lists all genes associated with each unique GO ID)
````
```{r group-by-GO, eval=TRUE}
grouped.gene.GO.df <- flat.gene.GO.df %>%
  group_by(!!sym(GO.ID.column)) %>%
  summarise(!!gene.ID.column := paste(.data[[gene.ID.column]], collapse = ","))

str(grouped.gene.GO.df)
```
````


Map GO IDs to GOslims

The mapping steps were derived from this [bioconductor forum response](https://support.bioconductor.org/p/128407/#128408)
````
```{r vectorize-GOIDs, eval=TRUE}
# Vector of GO IDs
go_ids <- grouped.gene.GO.df[[GO.ID.column]]

str(go_ids)
```
````


Creates new OBO Collection object of just GOslims, based on provided GO IDs.
````
```{r extract-GOslims-from-OBO, eval=TRUE}

# Create GSEAbase GOCollection using `go_ids`
myCollection <- GOCollection(go_ids)

# Retrieve GOslims from GO OBO file set
slim <- getOBOCollection(gseabase_files)

str(slim)
```
````

Get Biological Process (BP) GOslims associated with provided GO IDs.
````
```{r retrieve-BP-GOslims, eval=TRUE}
# Retrieve Biological Process (BP) GOslims
slimdf <- goSlim(myCollection, slim, "BP", verbose)
str(slimdf)
```
````




Performs mapping of of GOIDs to GOslims

Returns:

- GOslim IDs (as rownames)
- GOslim terms
- Counts of GO IDs matching to corresponding GOslim
- Percentage of GO IDs matching to corresponding GOslim
- GOIDs mapped to corresponding GOslim, in a semi-colon delimited format
````
```{r map-GO-to-GOslims, eval=TRUE}
# List of GOslims and all GO IDs from `go_ids`
gomap <- as.list(GOBPOFFSPRING[rownames(slimdf)])

# Maps `go_ids` to matching GOslims
mapped <- lapply(gomap, intersect, ids(myCollection))

# Append all mapped GO IDs to `slimdf`
# `sapply` needed to apply paste() to create semi-colon delimited values
slimdf$GO.IDs <- sapply(lapply(gomap, intersect, ids(myCollection)), paste, collapse=";")

# Remove "character(0) string from "GO.IDs" column
slimdf$GO.IDs[slimdf$GO.IDs == "character(0)"] <- ""

# Add self-matching GOIDs to "GO.IDs" column, if not present
for (go_id in go_ids) {
  # Check if the go_id is present in the row names
  if (go_id %in% rownames(slimdf)) {
    # Check if the go_id is not present in the GO.IDs column
    # Also removes white space "trimws()" and converts all to upper case to handle
    # any weird, "invisible" formatting issues.
    if (!go_id %in% trimws(toupper(strsplit(slimdf[go_id, "GO.IDs"], ";")[[1]]))) {
      # Append the go_id to the GO.IDs column with a semi-colon separator
      if (length(slimdf$GO.IDs) > 0 && nchar(slimdf$GO.IDs[nrow(slimdf)]) > 0) {
        slimdf[go_id, "GO.IDs"] <- paste0(slimdf[go_id, "GO.IDs"], "; ", go_id)
      } else {
        slimdf[go_id, "GO.IDs"] <- go_id
      }
    }
  }
}

str(slimdf)
```
````

"Flatten" file so each row is single GO ID with corresponding GOslim rownames_to_column needed to retain row name info
````
```{r flatten-GOslims-file, eval=TRUE}
# "Flatten" file so each row is single GO ID with corresponding GOslim
# rownames_to_column needed to retain row name info
slimdf_separated <- as.data.frame(slimdf %>%
  rownames_to_column('GOslim') %>%
  separate_rows(GO.IDs, sep = ";"))

# Group by unique GO ID
grouped_slimdf <- slimdf_separated %>%
  filter(!is.na(GO.IDs) & GO.IDs != "") %>%
  group_by(GO.IDs) %>%
  summarize(GOslim = paste(GOslim, collapse = ";"),
            Term = paste(Term, collapse = ";"))


str(grouped_slimdf)
```
````


Sorts GOslims by `Count`, in descending order and then
selects just the `Term` and `Count` columns.
````
```{r sort-and-select-slimdf-counts, eval=TRUE}

slimdf.sorted <- slimdf %>% arrange(desc(Count))

slim.count.df <- slimdf.sorted %>% 
  select(Term, Count)

str(slim.count.df)
```
````
---

## Enrichment Analysis Visualization and Interpretation

You've completed your enrichment analysis and have a list of significantly enriched GO terms, KEGG pathways, or other functional categories. Now what? Enrichment analysis often produces hundreds of significantly enriched terms, making it challenging to distill these results into a compelling narrative and impactful visualizations for your research story.

### Overview: From Results to Story

After completing enrichment analysis, you typically face these challenges:

1. **Identify the most important physiological processes** relevant to your biological question from hundreds of enriched terms
2. **Create visualizations** that clearly communicate key findings without overwhelming readers
3. **Write a coherent discussion** that tells a story rather than listing enriched terms

This section provides strategies, code examples, and best practices for transforming your enrichment results into publication-ready figures and narratives. **This guide assumes you already have enrichment results** (e.g., from clusterProfiler, GOseq, DAVID, or similar tools).

---

### Best Practices for Synthesizing Enrichment Results

#### 1. Prioritize and Filter Results

Not all significantly enriched terms are equally informative. Consider:

- **Biological relevance**: Focus on processes directly related to your experimental design or biological question
- **Term specificity**: Prefer specific terms (e.g., "lipid metabolic process") over very broad terms (e.g., "metabolic process")
- **Statistical significance**: Use adjusted p-values (FDR/q-value < 0.05) and consider effect size (fold enrichment)
- **Redundancy reduction**: Many GO terms are hierarchical and redundant; simplify by selecting representative terms

**Strategy**: Start by filtering to the top 10-20 most significant terms, then manually curate to remove redundancy and retain biological meaning.

#### 2. Group Related Processes

Organize enriched terms into higher-level biological themes:

- **Metabolism**: Energy production, biosynthesis, catabolism
- **Stress response**: Oxidative stress, heat shock, immune response
- **Development**: Cell differentiation, morphogenesis, growth
- **Signaling**: Cell communication, signal transduction
- **Structural**: Cytoskeleton, cell adhesion, extracellular matrix

This grouping helps create a coherent narrative and simplifies visualization.

#### 3. Compare Across Conditions

If you have multiple comparisons (e.g., multiple treatments or time points):

- Identify **shared** enriched processes (core response)
- Identify **unique** enriched processes (condition-specific responses)
- Look for **temporal patterns** (early vs. late response)
- Consider **opposing processes** (up-regulated vs. down-regulated genes)

---

### R Packages for Visualization

#### Essential Packages

```r
# Install Bioconductor packages (if needed)
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install(c("enrichplot", "GOSemSim", "DOSE"))

# Install CRAN packages
install.packages(c("ggplot2", "dplyr", "tidyr", "forcats", "stringr", "RColorBrewer"))
```

**Key packages**:
- **enrichplot**: Advanced visualization functions for enrichment results
- **GOSemSim**: Semantic similarity to reduce redundancy
- **ggplot2**: Customizable plotting
- **dplyr/tidyr**: Data manipulation

---

### Working with Your Enrichment Results

This section assumes you have enrichment results in one of these formats:

1. **clusterProfiler object** (e.g., from `enrichGO()`, `enrichKEGG()`)
2. **Data frame** with columns for: term ID, description, p-value, adjusted p-value, gene count, etc.
3. **Table from web tools** (DAVID, Enrichr, etc.) exported as CSV/TSV

#### Loading Your Results

```r
library(enrichplot)
library(ggplot2)
library(dplyr)

# If you have a clusterProfiler object already:
# ego_results <- readRDS("my_enrichment_results.rds")

# If you have a table from another tool, read it:
# enrichment_df <- read.csv("enrichment_results.csv")

# For this guide, we'll assume you have a clusterProfiler enrichResult object
# named 'ego_results' with your enrichment analysis results
```

#### Simplify Results (Remove Redundancy)

```r
library(GOSemSim)

# Assuming you have enrichment results in 'ego_results'
# Simplify GO terms based on semantic similarity
ego_simplified <- simplify(ego_results, 
                          cutoff = 0.7,      # Similarity threshold (0-1)
                          by = "p.adjust",   # Metric to select representative
                          select_fun = min)

# Further reduce to top N terms
top_n <- 20
ego_top <- ego_simplified[1:min(top_n, nrow(ego_simplified)), ]

# Convert to dataframe for further manipulation
ego_df <- as.data.frame(ego_simplified)
```

**Note**: If your enrichment results are from a non-clusterProfiler source (e.g., DAVID, Enrichr), you can manually filter redundant terms by:
- Selecting the most specific term from hierarchical groups
- Using [REVIGO](http://revigo.irb.hr/) to cluster semantically similar terms
- Prioritizing terms with the highest significance and gene counts

---

### Creating Impactful Figures

#### 1. Dot Plot (Most Common and Effective)

Dot plots show enriched terms with:
- **X-axis**: Gene ratio or fold enrichment
- **Y-axis**: GO terms
- **Dot size**: Number of genes
- **Dot color**: Significance (p-value or q-value)

```r
# Basic dotplot
dotplot(ego_top, 
        showCategory = 20,
        font.size = 10,
        title = "GO Biological Process Enrichment")

# Enhanced dotplot with custom colors
dotplot(ego_top, 
        showCategory = 20,
        font.size = 10) + 
  scale_color_gradient(low = "red", high = "blue") +
  theme_minimal() +
  theme(axis.text.y = element_text(size = 11)) +
  ggtitle("Top Enriched Biological Processes in DEGs")
```

**Best for**: Showing top 15-25 enriched terms with statistical significance and gene counts at a glance.

#### 2. Bar Plot (Clear and Simple)

```r
# Bar plot showing count or gene ratio
barplot(ego_top, 
        showCategory = 15,
        font.size = 10) + 
  ggtitle("GO Enrichment - Biological Process")

# Horizontal bar plot with custom aesthetics
ggplot(ego_df[1:15, ], aes(x = Count, y = reorder(Description, Count))) +
  geom_bar(stat = "identity", aes(fill = p.adjust)) +
  scale_fill_gradient(low = "red", high = "blue", name = "Adjusted\np-value") +
  labs(x = "Gene Count", y = "", title = "Top 15 Enriched GO Terms") +
  theme_minimal() +
  theme(axis.text.y = element_text(size = 11))
```

**Best for**: Simple, publication-ready figures showing the most enriched processes.

#### 3. Network/Enrichment Map (Shows Relationships)

Network plots display relationships between enriched terms based on shared genes:

```r
# Pairwise term similarity
ego_pairwise <- pairwise_termsim(ego_simplified)

# Enrichment map (network plot)
emapplot(ego_pairwise, 
         showCategory = 30,
         cex_label_category = 0.7,
         layout = "nicely") +
  ggtitle("Enrichment Map of GO Terms")

# Alternative: use ggraph for more control
library(ggraph)
emapplot(ego_pairwise, 
         showCategory = 30,
         cex_label_category = 0.7,
         layout = "fr")  # Fruchterman-Reingold layout
```

**Best for**: Showing how enriched processes relate to each other and identifying clusters of related functions.

#### 4. Upset Plot (For Multiple Gene Lists)

When comparing enrichment across multiple conditions:

```r
# Assuming you have multiple enrichment results
ego_list <- list(Condition1 = ego_cond1,
                Condition2 = ego_cond2,
                Condition3 = ego_cond3)

# Upset plot
upsetplot(ego_list)
```

**Best for**: Comparing enriched terms across multiple experimental conditions or time points.

#### 5. Heatmap of Enriched Terms

```r
# Heatplot showing gene-term relationships
heatplot(ego_top, 
         showCategory = 15,
         foldChange = gene_fc)  # Optional: include fold-change values

# Custom heatmap with ggplot2
library(pheatmap)

# Prepare matrix: rows = genes, columns = GO terms
# (Requires some data wrangling)
```

**Best for**: Detailed view of which genes contribute to which enriched terms.

#### 6. Gene-Concept Network

```r
# Show genes associated with top enriched terms
cnetplot(ego_top, 
         showCategory = 5,
         foldChange = gene_fc,  # Optional: show gene expression
         circular = FALSE,
         colorEdge = TRUE)

# Circular layout
cnetplot(ego_top, 
         showCategory = 5,
         circular = TRUE,
         colorEdge = TRUE)
```

**Best for**: Highlighting specific genes driving enrichment in key processes.

---

### Advanced Visualization Strategies

#### Combining Multiple Plots

```r
library(cowplot)
library(patchwork)

# Create multiple plots
p1 <- dotplot(ego_bp, showCategory = 15) + ggtitle("Biological Process")
p2 <- dotplot(ego_mf, showCategory = 15) + ggtitle("Molecular Function")
p3 <- dotplot(ego_cc, showCategory = 15) + ggtitle("Cellular Component")

# Combine into one figure
combined_plot <- p1 | p2 | p3
ggsave("combined_GO_enrichment.png", combined_plot, width = 18, height = 6, dpi = 300)
```

#### Custom Ordering and Grouping

```r
# Manually select and order terms by biological theme
selected_terms <- c(
  # Metabolism
  "lipid metabolic process",
  "carbohydrate metabolic process",
  
  # Stress response
  "response to oxidative stress",
  "response to heat",
  
  # Immune
  "innate immune response",
  "inflammatory response"
)

# Filter and plot in custom order
ego_custom <- ego_df %>%
  filter(Description %in% selected_terms) %>%
  mutate(Description = factor(Description, levels = selected_terms))

ggplot(ego_custom, aes(x = GeneRatio, y = Description)) +
  geom_point(aes(size = Count, color = p.adjust)) +
  scale_color_gradient(low = "red", high = "blue") +
  theme_minimal() +
  labs(title = "Key Physiological Processes in Response to Treatment")
```

#### Adding Annotations and Context

```r
# Add biological context to plot
dotplot(ego_top, showCategory = 15) +
  annotate("rect", xmin = 0.3, xmax = 0.5, ymin = 1, ymax = 5, 
           alpha = 0.2, fill = "yellow") +
  annotate("text", x = 0.4, y = 6, 
           label = "Metabolic\nreprogramming", 
           size = 4, fontface = "bold")
```

---

### Writing a Compelling Discussion

#### Structure Your Narrative

1. **Start with the big picture**: What is the overall biological theme?
   - *"Enrichment analysis revealed a coordinated metabolic shift toward lipid catabolism..."*

2. **Present major themes, not individual terms**: Group related processes
   - *"Three major physiological responses emerged: (1) stress defense, (2) metabolic remodeling, and (3) immune activation"*

3. **Connect to your hypothesis**: Link enrichment to your research question
   - *"Consistent with our hypothesis that heat stress triggers energy reallocation..."*

4. **Highlight specific processes**: Dive into 2-3 key enriched processes
   - *"The enrichment of 'oxidative stress response' (q-value = 0.001, 45 genes) suggests..."*

5. **Integrate with gene expression patterns**: Mention direction (up/down)
   - *"Up-regulated genes were enriched in immune pathways, while down-regulated genes showed enrichment in growth processes"*

6. **Compare to literature**: Reference similar findings or contrasts
   - *"This aligns with previous transcriptomic studies in oysters exposed to thermal stress (Smith et al., 2020)"*

7. **Acknowledge limitations and complexity**: Be transparent
   - *"While enrichment analysis provides functional insights, individual gene functions and pathway crosstalk require further investigation"*

#### Example Discussion Paragraph

```
Gene ontology enrichment analysis of the 1,247 up-regulated genes revealed significant 
overrepresentation of biological processes related to stress response and metabolic 
remodeling (Figure 3A). Specifically, genes involved in 'response to oxidative stress' 
(GO:0006979, q < 0.001, 68 genes), 'protein folding' (GO:0006457, q = 0.002, 45 genes), 
and 'lipid catabolic process' (GO:0016042, q = 0.003, 52 genes) were highly enriched. 
This pattern suggests a coordinated cellular response to thermal stress characterized by 
both protective mechanisms (heat shock proteins, antioxidant enzymes) and metabolic 
adaptation (shift from anabolic to catabolic processes). In contrast, down-regulated 
genes (n = 892) showed enrichment in 'cell division' (GO:0051301, q < 0.001) and 
'protein translation' (GO:0006412, q = 0.002), indicating suppression of energy-intensive 
growth processes during stress. These findings align with the concept of stress-induced 
growth-metabolism tradeoffs previously described in marine invertebrates (Jones et al., 2018).
```

---

### Complete Workflow Example

This example assumes you already have enrichment results from your analysis.

```r
# ===== Visualization Workflow Starting with Enrichment Results =====

library(enrichplot)
library(ggplot2)
library(dplyr)
library(GOSemSim)

# STARTING POINT: You already have enrichment results
# These could be from clusterProfiler, GOseq, or loaded from saved files
# For this example, we assume you have two enrichResult objects:
# - ego_up: enrichment results for up-regulated genes
# - ego_down: enrichment results for down-regulated genes

# If you saved your results previously, load them:
# ego_up <- readRDS("enrichment_results_up.rds")
# ego_down <- readRDS("enrichment_results_down.rds")

# 1. Simplify results to remove redundancy
ego_up_simp <- simplify(ego_up, cutoff = 0.7, by = "p.adjust", select_fun = min)
ego_down_simp <- simplify(ego_down, cutoff = 0.7, by = "p.adjust", select_fun = min)

# 2. Create publication-ready figure
p_up <- dotplot(ego_up_simp, showCategory = 15, title = "Up-regulated Genes") +
  scale_color_gradient(low = "red", high = "blue")

p_down <- dotplot(ego_down_simp, showCategory = 15, title = "Down-regulated Genes") +
  scale_color_gradient(low = "red", high = "blue")

# Combine plots
library(patchwork)
combined <- p_up / p_down
ggsave("Figure_GO_enrichment.png", combined, width = 10, height = 12, dpi = 300)

# 3. Export results table for supplementary materials
write.csv(as.data.frame(ego_up_simp), "Supplementary_Table_GO_up.csv", row.names = FALSE)
write.csv(as.data.frame(ego_down_simp), "Supplementary_Table_GO_down.csv", row.names = FALSE)

# 4. Create enrichment map for manuscript
ego_up_pairwise <- pairwise_termsim(ego_up_simp)
p_network <- emapplot(ego_up_pairwise, showCategory = 30) +
  ggtitle("Enrichment Network - Up-regulated Genes")
ggsave("Figure_enrichment_network.png", p_network, width = 10, height = 10, dpi = 300)
```

**Alternative: Working with enrichment results from other tools**

If you have enrichment results from DAVID, Enrichr, or similar web tools:

```r
# Load your enrichment results table
enrichment_df <- read.csv("enrichment_results.csv")

# Assuming columns: Term, P.value, Adjusted.P.value, Genes, Count
# Filter to significant terms
sig_terms <- enrichment_df %>%
  filter(Adjusted.P.value < 0.05) %>%
  arrange(Adjusted.P.value) %>%
  head(20)

# Create a custom bar plot
ggplot(sig_terms, aes(x = Count, y = reorder(Term, Count))) +
  geom_bar(stat = "identity", aes(fill = Adjusted.P.value)) +
  scale_fill_gradient(low = "red", high = "blue", name = "Adjusted\np-value") +
  labs(x = "Gene Count", y = "", title = "Top 20 Enriched Terms") +
  theme_minimal() +
  theme(axis.text.y = element_text(size = 10))

ggsave("enrichment_barplot.png", width = 8, height = 10, dpi = 300)
```

---

### Alternative Approaches and Tools

#### Using GOplot for Circular Visualization

```r
# Install GOplot
if (!requireNamespace("GOplot", quietly = TRUE))
    install.packages("GOplot")

library(GOplot)

# Prepare data (requires specific format)
# See: https://wencke.github.io/

# Circular visualization
GOCircle(GOplot_data, nsub = 10)
```

#### REVIGO for Semantic Clustering

For reducing GO term redundancy through semantic similarity:

1. Export GO terms with p-values
2. Upload to [REVIGO](http://revigo.irb.hr/)
3. Visualize clustered terms
4. Export representative terms

#### ShinyGO for Interactive Exploration

[ShinyGO](http://bioinformatics.sdstate.edu/go/) provides a web interface for:
- Enrichment analysis
- Interactive visualizations
- Pathway analysis
- No coding required

---

### Tips for Publication-Quality Figures

1. **Font sizes**: Ensure labels are readable (minimum 8-10 pt)
2. **Color palettes**: Use colorblind-friendly palettes (viridis, RColorBrewer)
3. **Resolution**: Export at 300 DPI for publication
4. **File format**: PDF for vector graphics, PNG for presentations
5. **Simplicity**: Don't show more than 20-25 terms per figure
6. **Consistency**: Use same color schemes across figures
7. **White space**: Don't overcrowd; consider multi-panel figures

```r
# Colorblind-friendly palette
library(viridis)

dotplot(ego_top, showCategory = 15) +
  scale_color_viridis(option = "plasma", direction = -1) +
  theme_minimal(base_size = 12)
```

---

### Common Pitfalls to Avoid

1. **Showing too many terms**: More is not better; focus on top processes
2. **Ignoring redundancy**: Simplify semantically similar terms
3. **Cherry-picking**: Report systematic filtering criteria
4. **Over-interpretation**: GO terms are predictions, not proof of function
5. **Ignoring background**: Always use appropriate universe/background
6. **P-value only**: Consider fold enrichment and gene counts too
7. **No biological context**: Connect enrichment to your research question

---

### Use Cases from Our Lab

- [Enrichment analysis examples](https://github.com/RobertsLab/paper-tanner-crab) - Tanner crab transcriptomics ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/paper-tanner-crab)

- [C. virginica GO enrichment](https://github.com/sr320/ceabigr) - Eastern oyster functional genomics ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/ceabigr)

---

### Additional Resources

**R Packages Documentation**:
- [clusterProfiler book](https://yulab-smu.top/biomedical-knowledge-mining-book/)
- [enrichplot documentation](https://github.com/YuLab-SMU/enrichplot)

**Tutorials**:
- [clusterProfiler tutorial](http://bioconductor.org/packages/release/bioc/vignettes/clusterProfiler/inst/doc/clusterProfiler.html)
- [GO enrichment analysis workflow](https://learn.gencore.bio.nyu.edu/rna-seq-analysis/gene-set-enrichment-analysis/)

**Theory**:
- [Gene Ontology Handbook](http://geneontology.org/)
- [Understanding enrichment analysis](https://www.pathwaycommons.org/guide/primers/statistics/fishers_exact_test/)

---

## Genome features
In addition to sequence database alignment, finding spatial relationship within a genome is also an import approach for annotation. Often this is done using software tools such as `bedtools`.

### `bedtools::intersectbed`
see also https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html

---

## Transcriptome (Trinity)

After [transcriptome assembly using Trinity](https://robertslab.github.io/resources/bio_Transcriptome-assembly/), run the numbered steps below, in order.

NOTE: The following info is long and requires the use of many programs. All of the code listed below are solely examples. Making the commands functional requires a fair amount of organization (i.e. listing paths to programs and input/output files, creating subdirectories for organizing outputs, etc.). See the Use Cases at the end of this section for a more complete picture of how to organize/run this pipeline.

1. Transdecoder

    - Identify longest open reading frames (ORFs).

    - Use transcriptome assembly and gene-trans map from [Trinity assembly](https://robertslab.github.io/resources/bio_Transcriptome-assembly/).

        ```
        TransDecoder.LongOrfs \
        --gene_trans_map Trinity.fasta.gene_trans_map \
        -t Trinity.fasta"
        ```

2. BLASTp

    - Run blastp on long ORFs from Step 1 above.

    - Output format 6 produces a standard BLAST tab-delimited file.

    - Settings are recommended in TransDecoder documentation.

    - Peptide database (`-db uniprot_sprot.pep`) is supplied with Trinotate (e.g. `Trinotate-v3.1.1/admin/uniprot_sprot.pep`), but can be changed to use your own version.

        ```
        blastp \
        -query longest_orfs.pep \
        -db uniprot_sprot.pep \
        -max_target_seqs 1 \
        -outfmt 6 \
        -evalue 1e-5 \
        -num_threads ${threads} \
        > Trinity.fasta.blastp.outfmt6
        ```

3. BLASTx ([`DIAMOND`](https://github.com/bbuchfink/diamond))

    - Run [`DIAMOND`](https://github.com/bbuchfink/diamond) blastx on long ORFs from Step 1 above.

    - Output format 6 produces a standard BLAST tab-delimited file.

    - Settings (`--evalue` and `--max-target-seqs`) are recommended in TransDecoder documentation.

    - `--block-size` and `--index-chunks` are specific to running [`DIAMOND`](https://github.com/bbuchfink/diamond) BLASTx.

    - `--db uniprot_sprot.dmnd` is a [`DIAMOND`](https://github.com/bbuchfink/diamond)-formatted BLAST database. User can generate their own.

            ```
            diamond blastx \
            --db uniprot_sprot.dmnd \
            --query Trinity.fasta \
            --out Trinity.fasta.blastx.outfmt6 \
            --outfmt 6 \
            --evalue 1e-4 \
            --max-target-seqs 1 \
            --block-size 15.0 \
            --index-chunks 4
            ```


4. pFam

    - Run pfam search on long ORFs from Step 1 above.

    - Protein hidden Markov model database (`Pfam-A.hmm`) is supplied with Trinotate (e.g. `Trinotate-v3.1.1/admin/Pfam-A.hmm`), but can be changed to use your own version.

        ```
        hmmscan \
        --cpu ${threads} \
        --domtblout Trinity.fasta.pfam.domtblout \
        Pfam-A.hmm \
        longest_orfs.pep
        ```



5. Transdecoder

    - Run Transdecoder using transcriptome assembly FastA, `blastp` and `Pfam` results.

    ```
    TransDecoder.Predict \
        -t Trinity.fasta \
        --retain_pfam_hits Trinity.fasta.pfam.domtblout \
        --retain_blastp_hits Trinity.fasta.blastp.outfmt6
    ```

6. Trinotate

    - Trinotate requires a large number of steps and programs!

        - Run `signalp`

            ```
            signalp \
            -f short \
            -n Trinity.fasta.trinotate.signalp.out \
            longest_orfs.pep
            ```

        - Run `tmHMM`

            ```
            tmhmm \
            --short \
            < longest_orfs.pep \
            > Trinity.fasta.trinotate.tmhmm.out
            ```

        - Run `RNAmmer`

            - Uses a special Trinotate implementation of `rnammer` (e.g. `Trinotate/util/rnammer_support/RnammerTranscriptome.pl`)

            ```
            RnammerTranscriptome.pl \
            --transcriptome Trinity.fasta \
            --path_to_rnammer rnammer
            ```
        
        - Load transcripts and coding regions into Trinotate SQLite database

            ```
            Trinotate \
            Trinotate.sqlite \
            init \
            --gene_trans_map Trinity.fasta.gene_trans_map \
            --transcript_fasta Tinity.fasta \
            --transdecoder_pep longest_orfs.pep
            ```

        - Load BLASTp/x homologies into SQLite database

            ```
            Trinotate \
            Trinotate.sqlite \
            LOAD_swissprot_blastp \
            Trinity.fasta.blastp.outfmt6
            ```

            ```   
            Trinotate \
            Trinotate.sqlite \
            LOAD_swissprot_blastx \
            Trinity.fasta.blastx.outfmt6
            ```

        - Load Pfam into SQLite database

            ```
            Trinotate \
            Trinotate.sqlite \
            LOAD_pfam \
            Trinity.fasta.pfam.domtblout
            ```

        - Load transmembrane domains

            ```
            Trinotate \
            Trinotate.sqlite \
            LOAD_tmhmm \
            Trinity.fasta.trinotate.tmhmm.out
            ```

        - Load signal peptides

            ```
            Trinotate \
            Trinotate.sqlite \
            LOAD_signalp \
            Trinity.fasta.trinotate.signalp.out
            ```

        - Load RNAmmer

            ```
            Trinotate \
            Trinotate.sqlite \
            LOAD_rnammer \
            Trinity.fasta.rnammer.gff
            ```

        - Create annotation report

            ```
            Trinotate \
            Trinotate.sqlite \
            report \
            > Trinity.fasta.annotation_report.txt
            ```

        - Extract gene ontology (GO) terms from annotation report

            ```
            extract_GO_assignments_from_Trinotate_xls.pl \
            --Trinotate_xls Trinity.fasta.annotation_report.txt \
            -G \
            --include_ancestral_terms \
            > Trinity.fasta.go_annotations.txt
            ```

            - The output file is formatted like this (`<trinity-id>``<tab>``<GO:NNNNNN,GO:NNNNN,...>`):

            ```
            TRINITY_DN0_c0_g1	GO:0003674,GO:0003824,GO:0003964,GO:0006139,GO:0006259,GO:0006310,GO:0006313,GO:0006725,GO:0006807,GO:0008150,GO:0008152,GO:0009987,GO:0016740,GO:0016772,GO:0016779,GO:0032196,GO:0034061,GO:0034641,GO:0043170,GO:0044237,GO:0044238,GO:0044260,GO:0044699,GO:0044710,GO:0044763,GO:0046483,GO:0071704,GO:0090304,GO:1901360
            TRINITY_DN0_c10_g1	GO:0003674,GO:0003824,GO:0004659,GO:0004660,GO:0005488,GO:0005575,GO:0005829,GO:0005875,GO:0005965,GO:0006464,GO:0006807,GO:0008150,GO:0008152,GO:0008270,GO:0008318,GO:0009987,GO:0016740,GO:0016765,GO:0018342,GO:0018343,GO:0019538,GO:0032991,GO:0036211,GO:0043167,GO:0043169,GO:0043170,GO:0043234,GO:0043412,GO:0044237,GO:0044238,GO:0044260,GO:0044267,GO:0044422,GO:0044424,GO:0044430,GO:0044444,GO:0044446,GO:0044464,GO:0046872,GO:0046914,GO:0071704,GO:0097354,GO:1901564,GO:1902494,GO:1990234
            TRINITY_DN0_c2_g4	GO:0000166,GO:0003674,GO:0005488,GO:0005524,GO:0005575,GO:0005737,GO:0005856,GO:0017076,GO:0030554,GO:0032553,GO:0032555,GO:0032559,GO:0035639,GO:0036094,GO:0043167,GO:0043168,GO:0043226,GO:0043228,GO:0043229,GO:0043232,GO:0044424,GO:0044464,GO:0097159,GO:0097367,GO:1901265,GO:1901363
            ```

    - Make transcript features annotation map

            ```
            Trinotate_get_feature_name_encoding_attributes.pl \
            Trinity.fasta.annotation_report.txt \
            > Trinity.fasta.annotation_feature_map.txt
            ```
