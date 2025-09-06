---
editor_options: 
  markdown: 
    wrap: 72
---

# Agentic Coding Tools and AI Assistants

AI-powered coding assistants can influence how we write and interact
with code. This guide covers how we might use these tools.    
**General tips for Using AI Coding Assistants**    
1. Use branches. This will protect main branch if you go off the rails.   
2. Provide an instructions.md and tasks.md. This will help keep agent on track

Below we cover GitHub Copilot (w/VScode), ChatGPT, local models 

------------------------------------------------------------------------

# GitHub Copilot

GitHub Copilot is an AI-powered coding assistant that helps you write
code by providing intelligent suggestions and completions.

### Getting Started with GitHub Copilot

#### Prerequisites

You'll need: - A GitHub account with Copilot access (available through
GitHub Education) - VS Code or compatible IDE - Active internet
connection

#### Checking Copilot Access

1.  Visit [GitHub Copilot](https://github.com/copilot) to check your
    subscription status
2.  Students and educators get free access through [GitHub
    Education](https://education.github.com/)

------------------------------------------------------------------------

## Setting Up GitHub Copilot with VS Code

### 1. Install the GitHub Copilot Extension

1.  Open VS Code
2.  Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`)
3.  Search for "GitHub Copilot"
4.  Install the official "GitHub Copilot" extension by GitHub
5.  Optionally install "GitHub Copilot Chat" for conversational AI
    assistance

### 2. Sign In and Activate

1.  After installation, you'll see a Copilot icon in the status bar
2.  Click on it and select "Sign in to GitHub"
3.  Follow the authentication flow in your browser
4.  Return to VS Code - Copilot should now be active

### 3. Verify Installation

Create a new file (e.g., `test.py`) and start typing a function:

``` python
def calculate_gc_content(
```

Copilot should suggest completions in gray text.

------------------------------------------------------------------------

### Practical use cases and notes

-   Tab completion.

-   Have it develop, refactor, buid code based on natural language
    instructions to "Agent".

-   There is a limit to use, so will need to keep an eye on this. Can
    see on Github website.

    -   Aspects that influence this if you "Ask" versus "Agent" and what
        model you select.

### VS Code Copilot Commands

In VS Code with GitHub Copilot, there are three main ways to interact with the AI assistant:

**1. Ask**
- Opens a chat-like panel (Copilot Chat)
- Type natural language questions ("What does this function do?", "How do I write a regex for emails?")
- Copilot responds with explanations, code snippets, or suggestions, but doesn't automatically change your code
- Best for Q&A, explanations, or guidance

**2. Agent**
- Runs a Copilot "task agent" that can perform multi-step or tool-like actions
- Examples: debugging, running tests, explaining diagnostics, or walking through refactors
- Agents are more goal-oriented and can combine different steps (like reading docs, analyzing code, generating edits)
- Best for complex workflows where Copilot needs context beyond a single answer

**3. Edit**
- Lets you select code in the editor, then ask Copilot to modify it
- Example: highlight a function → Edit with Copilot → "Convert this to async/await"
- Copilot rewrites the selection directly in your file, showing a diff you can accept or reject
- Best for direct code changes/refactoring

**✅ Rule of thumb:**
- Use **Ask** when you want to understand
- Use **Edit** when you want to change
- Use **Agent** when you want Copilot to do something bigger/more involved (like debugging, running tests, or analyzing errors)

------------------------------------------------------------------------

## Using GitHub Copilot on the Web

GitHub offers Copilot directly in the web interface, making it
accessible even when working remotely on repositories.

### 1. Accessing Web Copilot

1.  Navigate to any GitHub repository
2.  Press `.` (period) to open the web-based VS Code editor
3.  Or go to `github.dev/owner/repository` directly
4.  The Copilot extension should be available if you have access

### 2. Using Copilot in GitHub's Web Editor

-   **Code completions**: Start typing and Copilot will suggest
    completions
-   **Chat interface**: Use Copilot Chat for questions and explanations
-   **Inline suggestions**: Accept suggestions with `Tab` or reject with
    `Esc`

### 3. GitHub.com Code View Features

When viewing code files on GitHub.com:

\- Look for the Copilot icon in file views

\- Click to get AI-powered explanations of code blocks

\- Get suggestions for improvements and alternative approaches

### 4. Assigning Copilot Issues

Arguably one of the most powerful features is the ability to assign issues to Copilot.  
Copilot will create a plan, implement on a new branch, then you (or someone else can review).
If you like it, you can merge it in using a pull request.


**Copilot in action on the web**

![Ways to interact with Copilot on
GitHub](http://gannet.fish.washington.edu/seashell/snaps/Screen20Shot202025-09-0120at2019.04.11.png){width=50%}

------------------------------------------------------------------------

### Using Copilot with UW Klone HPC

#### Remote Development Setup

1.  **SSH with VS Code**

    ``` bash
    # Install Remote-SSH extension in VS Code
    # Connect to Klone through VS Code's Remote SSH
    ssh your_netid@klone.hyak.uw.edu
    ```

2.  OPTION 2 - more coming soon

------------------------------------------------------------------------



### Documentation and Tutorials

-   [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
-   [VS Code Copilot
    Guide](https://code.visualstudio.com/docs/editor/github-copilot)
-   [Copilot Best
    Practices](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

---

# ChatGPT

Most are familar with ChatGPT chat features (online or standalone).
There is also ChatGPT codex that allows you to interact directly with a
GitHub repository online or in the terminal

---

# Ollama (local models)

There are certain use cases where having everything on your machine
makes sense such as asking simple regex questions. For this installing
Ollama is an option.

---

# Image Generation 

more coming soon

---
.
