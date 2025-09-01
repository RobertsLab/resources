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
2. Students and educators get free access through [GitHub Education](https://education.github.com/)

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

- **Review generated code** - AI suggestions may contain errors or security issues
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


### 4. Learning and Skill Development

- **Ask for explanations** - Use Copilot Chat to understand unfamiliar code patterns
- **Request alternatives** - Ask for different approaches to solve problems
- **Learn new libraries** - Get help with syntax and best practices for new packages

---



### Using Copilot with UW Klone HPC

#### Remote Development Setup

1. **SSH with VS Code**
   ```bash
   # Install Remote-SSH extension in VS Code
   # Connect to Klone through VS Code's Remote SSH
   ssh your_netid@klone.hyak.uw.edu
   ```

2. OPTION 2 - more coming soon



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
