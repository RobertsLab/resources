# Agentic Coding Tools and AI Assistants

AI-powered coding assistants are revolutionizing how we write and interact with code. This guide covers how to effectively use these tools in the Roberts Lab computing environment.

---

## GitHub Copilot

GitHub Copilot is an AI-powered coding assistant that helps you write code faster and with fewer errors by providing intelligent suggestions and completions.

### Getting Started with GitHub Copilot

#### Prerequisites

You'll need:
- A GitHub account with Copilot access (available through GitHub Education or paid subscription)
- VS Code or compatible IDE
- Active internet connection

#### Checking Copilot Access

1. Visit [GitHub Copilot](https://github.com/copilot) to check your subscription status
2. Students and educators can often get free access through [GitHub Education](https://education.github.com/)

---

## Setting Up GitHub Copilot with VS Code

### 1. Install the GitHub Copilot Extension

1. Open VS Code
2. Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`)
3. Search for "GitHub Copilot"
4. Install the official "GitHub Copilot" extension by GitHub
5. Optionally install "GitHub Copilot Chat" for conversational AI assistance

### 2. Sign In and Activate

1. After installation, you'll see a Copilot icon in the status bar
2. Click on it and select "Sign in to GitHub"
3. Follow the authentication flow in your browser
4. Return to VS Code - Copilot should now be active

### 3. Verify Installation

Create a new file (e.g., `test.py`) and start typing a function:
```python
def calculate_gc_content(
```
Copilot should suggest completions in gray text.

---

## Using GitHub Copilot on the Web

GitHub now offers Copilot directly in the web interface, making it accessible even when working remotely on repositories.

### 1. Accessing Web Copilot

1. Navigate to any GitHub repository
2. Press `.` (period) to open the web-based VS Code editor
3. Or go to `github.dev/owner/repository` directly
4. The Copilot extension should be available if you have access

### 2. Using Copilot in GitHub's Web Editor

- **Code completions**: Start typing and Copilot will suggest completions
- **Chat interface**: Use Copilot Chat for questions and explanations
- **Inline suggestions**: Accept suggestions with `Tab` or reject with `Esc`

### 3. GitHub.com Code View Features

When viewing code files on GitHub.com:
- Look for the Copilot icon in file views
- Click to get AI-powered explanations of code blocks
- Get suggestions for improvements and alternative approaches

---

## Best Practices for Using AI Coding Assistants

### 1. Code Quality and Review

- **Always review generated code** - AI suggestions may contain errors or security issues
- **Test thoroughly** - AI-generated code should be tested like any other code
- **Understand before using** - Don't include code you don't understand
- **Follow lab coding standards** - Ensure AI suggestions align with [Computing Best Practices](Computing-Best-Practices.md)

### 2. Effective Prompting Techniques

#### Write Clear Comments
```python
# Calculate GC content percentage for a DNA sequence
# Input: DNA sequence as string (A, T, G, C)
# Output: Float percentage (0-100)
def calculate_gc_content(sequence):
```

#### Use Descriptive Function Names
```python
def filter_high_quality_reads(fastq_file, min_quality=30):
    # Copilot will better understand the intent
```

#### Provide Context in Comments
```r
# Analyze differential gene expression using DESeq2
# Input: count matrix from RNA-seq experiment
# Compare treatment vs control groups
```

### 3. Documentation and Reproducibility

- Use Copilot to help generate clear docstrings and comments
- Ask for help explaining complex algorithms or data structures
- Generate README sections and documentation

Example prompt for documentation:
```python
def complex_analysis_function(data):
    """
    # Ask Copilot to help write comprehensive docstring
    """
```

### 4. Learning and Skill Development

- **Ask for explanations** - Use Copilot Chat to understand unfamiliar code patterns
- **Request alternatives** - Ask for different approaches to solve problems
- **Learn new libraries** - Get help with syntax and best practices for new packages

---

## Integration with Lab Computing Resources

### Using Copilot with UW Klone HPC

#### Remote Development Setup

1. **SSH with VS Code**
   ```bash
   # Install Remote-SSH extension in VS Code
   # Connect to Klone through VS Code's Remote SSH
   ssh your_netid@klone.hyak.uw.edu
   ```

2. **Port Forwarding for Development**
   ```bash
   # Forward ports for Jupyter or RStudio Server if needed
   ssh -L 8888:localhost:8888 your_netid@klone.hyak.uw.edu
   ```

#### Best Practices on Klone

- **Use Copilot for script development** before transferring to Klone
- **Generate SLURM job scripts** - Ask Copilot to help write submission scripts
- **Optimize resource usage** - Get suggestions for memory and CPU allocation

Example SLURM script generation:
```bash
# Ask Copilot to generate a SLURM script for RNA-seq analysis
#!/bin/bash
#SBATCH --job-name=rnaseq_analysis
#SBATCH --account=srlab
#SBATCH --partition=compute
```

#### Working with Large Datasets

```python
# Use Copilot to help with efficient data processing
# for large genomic datasets on Klone
import pandas as pd
import numpy as np

def process_large_genomic_data(filepath, chunk_size=10000):
    # Copilot can suggest memory-efficient approaches
```

### Using Copilot with Raven

#### RStudio Server Integration

1. **Access RStudio Server on Raven**
   - Connect via VPN as described in [Lab Software](Lab-Software.md)
   - Use the web interface at `http://172.25.149.12:8787`

2. **Development Workflow**
   - Develop scripts locally with Copilot assistance in VS Code
   - Transfer to Raven for execution on larger datasets
   - Use Copilot to generate R analysis scripts

#### R-Specific Tips

```r
# Use Copilot for bioinformatics workflows in R
library(DESeq2)
library(ggplot2)

# Copilot can help with complex ggplot2 visualizations
create_volcano_plot <- function(deseq_results) {
    # Ask for help with publication-quality plots
```

### Data Analysis Workflows

#### Genomics and Bioinformatics

```python
# Use Copilot for common bioinformatics tasks
import pandas as pd
from Bio import SeqIO
import subprocess

def run_blast_analysis(query_file, database):
    # Get help with command-line tool integration
```

#### Statistical Analysis

```r
# Copilot can assist with statistical modeling
library(lme4)
library(tidyverse)

# Mixed-effects models for experimental data
analyze_treatment_effects <- function(data, response_var) {
    # Get suggestions for appropriate statistical tests
```

---

## Security and Privacy Considerations

### 1. Sensitive Data

- **Never include sensitive data** in prompts or code shared with AI
- **Be cautious with proprietary algorithms** or unpublished methods
- **Review lab data policies** before using AI tools with research data

### 2. Code Review Requirements

- All AI-generated code should undergo the same review process as human-written code
- Include AI assistance in commit messages when significant portions are AI-generated
- Follow lab standards for code documentation and testing

### 3. Intellectual Property

- Understand your institution's policies on AI-generated code
- Be transparent about AI assistance in publications and documentation
- Ensure generated code doesn't inadvertently copy copyrighted material

---

## Troubleshooting Common Issues

### Copilot Not Working

1. **Check subscription status** - Verify your Copilot access is active
2. **Restart VS Code** - Sometimes the extension needs a restart
3. **Check internet connection** - Copilot requires active internet
4. **Update extensions** - Ensure you have the latest version

### Poor Suggestions

1. **Provide more context** - Add detailed comments about your intent
2. **Use better variable names** - Descriptive names help Copilot understand
3. **Break down complex problems** - Start with simpler functions and build up

### Performance Issues

1. **Close unnecessary files** - Too many open files can slow suggestions
2. **Check system resources** - Ensure adequate memory and CPU
3. **Adjust settings** - Reduce suggestion frequency if needed

---

## Alternative AI Coding Tools

While this guide focuses on GitHub Copilot, other tools are available:

- **Amazon CodeWhisperer** - AWS-integrated coding assistant
- **Tabnine** - AI code completion with local options
- **Claude** or **ChatGPT** - For explaining code and generating snippets
- **Cursor** - AI-powered code editor

Choose tools that align with lab policies and your specific needs.

---

## Learning Resources

### Documentation and Tutorials

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Guide](https://code.visualstudio.com/docs/editor/github-copilot)
- [Copilot Best Practices](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

### Lab-Specific Resources

- [Computing Best Practices](Computing-Best-Practices.md) - Apply these principles with AI assistance
- [Lab Software](Lab-Software.md) - See what tools are available for integration
- [Klone Guides](klone_quick-start.md) - Use AI to help with HPC workflows

---

## Getting Help

- **Lab Slack channels** - Ask for help with AI tool setup and usage
- **GitHub Issues** - [Report problems](https://github.com/RobertsLab/resources/issues) with this documentation
- **Office Hours** - Discuss AI tool integration during lab meetings

Remember: AI coding assistants are powerful tools that can enhance productivity, but they work best when combined with solid programming fundamentals and careful review practices.