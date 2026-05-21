# Agentic Coding Tools and AI Assistants

AI-powered coding assistants can speed up writing, debugging, and refactoring code. They can also introduce subtle errors, leak context to third-party servers, or push changes in the wrong direction if you are not careful.

This guide covers tools the lab commonly uses—**GitHub Copilot**, **ChatGPT / Codex**, and **local models (Ollama)**—plus practices that keep agents useful and your work reproducible.

**Related:** [Computing Best Practices](Computing-Best-Practices.md) · [VS Code on Klone](klone_VS-Code.md)

---

## Quick comparison

| Tool | Where it runs | Best for | Needs internet |
|------|---------------|----------|----------------|
| [GitHub Copilot](#github-copilot) | VS Code, github.dev, GitHub.com | Tab completion, in-editor chat, issue → PR agent | Yes |
| [ChatGPT / Codex](#chatgpt-and-openai-codex) | Browser, desktop app, terminal CLI | Explaining concepts, one-off scripts, repo-wide tasks via CLI | Yes |
| [Ollama + Continue](#ollama-local-models) | Your machine only | Quick questions, regex help, privacy-sensitive drafts | No (after model download) |
| [Image tools](#image-generation) | Various | Figures, diagrams, mockups (verify licensing & accuracy) | Usually yes |

---

## Principles for using AI assistants in research code

### Protect your main branch and your data

1. **Work on a branch.** Agents can edit many files at once. A feature branch limits damage and makes review easy.
2. **Never commit secrets.** Do not paste API keys, passwords, or `.env` contents into chat. Add those paths to `.gitignore` before sharing a repo with an agent.
3. **Treat unpublished data carefully.** Sequences, field notes, and embargoed results may be sent to vendor servers when you use cloud tools. Prefer [local models](#ollama-local-models) or offline workflows when sensitivity matters.
4. **Review every change.** Read diffs like a colleague’s PR. Run tests and spot-check outputs—especially statistics, file paths, and HPC job scripts.

### Give agents enough context

Agents work better when the repository explains itself:

| File | Purpose |
|------|---------|
| `instructions.md` (or `AGENTS.md`) | Project goals, conventions, how to run code, what *not* to touch |
| `tasks.md` | Current sprint: what is done, in progress, and blocked |
| `README.md` in each folder | What data and scripts live where ([Computing Best Practices](Computing-Best-Practices.md)) |

Keep these files short and current. Stale instructions are worse than none.

### Match the mode to the job

| You want to… | Use |
|--------------|-----|
| Understand code or an error message | **Ask** / chat (read-only Q&A) |
| Change a specific function or block | **Edit** / inline edit on a selection |
| Multi-step work (tests, refactors, debugging) | **Agent** / coding agent |
| An entire GitHub issue implemented as a PR | **Copilot coding agent** on GitHub |

### Watch usage limits

Copilot and ChatGPT plans have monthly or rate limits. Usage often depends on whether you use lightweight **Ask** vs heavier **Agent** modes and which model you select. Check your account dashboard when sessions stop unexpectedly.

---

## GitHub Copilot

[GitHub Copilot](https://github.com/copilot) suggests code as you type and can run conversational or agentic workflows in the editor and on GitHub.com.

### Prerequisites

- GitHub account with Copilot access ([GitHub Education](https://education.github.com/) provides free access for many students and educators)
- VS Code or another [supported IDE](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-for-your-enterprise/about-github-copilot-for-business)
- Active internet connection (cloud models)

**Check access:** [github.com/copilot](https://github.com/copilot)

### Setup in VS Code

#### 1. Install extensions

1. Open VS Code → Extensions (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Install **GitHub Copilot** (by GitHub)
3. Install **GitHub Copilot Chat** for Ask / Agent / Edit panels

#### 2. Sign in

1. Click the Copilot icon in the status bar → **Sign in to GitHub**
2. Complete browser authentication
3. Confirm the status bar shows Copilot as enabled

#### 3. Verify inline completion

Create a test file and start a function:

```python
def calculate_gc_content(
```

Gray ghost text should appear; accept with `Tab`, dismiss with `Esc`.

### Ask, Edit, and Agent in VS Code

Copilot Chat exposes three interaction styles:

**Ask** — Chat panel for questions without automatic edits.

- Examples: “What does this function do?”, “Write a regex for valid FASTA headers”
- Copilot explains or suggests snippets; you apply changes manually
- Best for learning and planning

**Edit** — Change selected code from a prompt.

- Select code → open Edit → e.g. “Convert this loop to vectorized pandas”
- Shows a diff; accept or reject
- Best for localized refactors

**Agent** — Multi-step, goal-oriented sessions.

- Can read files, propose edits, run terminal commands (depending on settings), and iterate on errors
- Best for debugging, test runs, and larger refactors
- Use on a branch; review all file changes before commit

**Rule of thumb:** Ask to understand → Edit to change a region → Agent for bigger workflows.

### Practical use cases in the lab

- **Tab completion** while writing R, Python, shell, or Quarto/Rmd
- **Explaining** unfamiliar API calls or error stacks
- **Refactoring** repetitive plotting or file I/O
- **Drafting** tests or README sections (then verify)
- **Scaffolding** Slurm scripts—always validate partition, account, and resource flags against [Klone guides](klone_quick-start.md)

### Copilot on the web

#### github.dev editor

1. Open any repository on GitHub
2. Press `.` (period) to open the web VS Code editor, or visit `https://github.dev/owner/repo`
3. Use completions and Copilot Chat like desktop VS Code (when your plan includes it)

#### Code view on GitHub.com

- Look for the Copilot control in file views for explanations and improvement ideas
- Treat suggestions as starting points, not ground truth

#### Assign issues to the Copilot coding agent

One of the strongest workflows for repo maintenance:

1. Open an issue with clear **background**, **acceptance criteria**, and **files or areas** to touch
2. Assign the issue to **Copilot** (same as assigning a teammate)
3. Copilot plans work, pushes to a branch, and opens a **pull request**
4. You review the PR; request changes or merge when satisfied

Write issues the way you would for a human contributor: what “done” looks like, constraints, and test commands if any.

![Ways to interact with Copilot on GitHub](http://gannet.fish.washington.edu/seashell/snaps/Screen20Shot202025-09-0120at2019.04.11.png)

Official docs: [Assign Copilot to an issue](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/assign-copilot-to-an-issue)

### Copilot on UW Klone (HPC)

Copilot runs in VS Code on **your laptop**, talking to cloud models; compute still runs on Klone when you execute code remotely.

**Recommended:** [VS Code on Klone via ProxyJump](klone_VS-Code.md) — connect to a compute node with Remote-SSH so login nodes stay free.

**Note:** Hyak OnDemand VS Code is easier to start but may not support Copilot extensions the same way; see pros/cons in the Klone VS Code guide.

Basic Remote-SSH flow:

```bash
# On your laptop: install Remote-SSH in VS Code, configure ProxyJump per UW-IT
ssh your_netid@klone.hyak.uw.edu
# Then salloc a compute node and connect VS Code to klone-node (see klone_VS-Code.md)
```

### Copilot documentation

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot guide](https://code.visualstudio.com/docs/copilot/overview)
- [Prompting best practices (GitHub Blog)](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

---

## ChatGPT and OpenAI Codex

### ChatGPT (chat)

[ChatGPT](https://chat.openai.com/) is useful for:

- Explaining algorithms, statistics, or file formats
- Drafting small standalone scripts before moving them into a repo
- Brainstorming analysis plans (then implementing and validating in version-controlled code)

**Limitations:** Chat sessions are not tied to your repo unless you upload files or use connectors. It will not run your Klone jobs or know your directory layout unless you provide that context. Always copy final code into GitHub with normal review.

### OpenAI Codex (CLI agent)

[Codex](https://github.com/openai/codex) is a **terminal-based** coding agent (distinct from the older “Codex” API name). It can read and edit files in a project directory, run commands, and work across a repository.

**Install (examples):**

```bash
npm install -g @openai/codex
# or
brew install --cask codex
```

**Typical workflow:**

1. `cd` into your git repository (on a feature branch)
2. Start Codex: `codex`
3. Describe the task in natural language; approve file and command changes when prompted
4. Review `git diff`, run tests, then commit

Access is included with many ChatGPT paid plans; see [Codex CLI documentation](https://developers.openai.com/codex/cli) for authentication options.

**When to prefer Codex vs Copilot:** Codex is strong when you want a **terminal-first**, repo-wide session without VS Code. Copilot is stronger for **inline completion** and **GitHub-native** issue → PR flows.

---

## Ollama (local models)

Running models locally keeps prompts on your machine—useful for quick help (regex, bash one-liners, explaining error messages) without sending text to a cloud API.

### Install Ollama

1. Download from [ollama.com](https://ollama.com/)
2. Pull a coding-oriented model, for example:

```bash
ollama pull qwen2.5-coder:7b
```

Smaller models are faster; larger models are better for multi-file reasoning but need more RAM.

### Use with VS Code (Continue extension)

[Continue](https://continue.dev/) connects VS Code to Ollama for chat and optional tab completion.

1. Install the **Continue** extension in VS Code
2. Ensure Ollama is running (`ollama serve` if needed)
3. Configure Continue to use `http://localhost:11434` as the Ollama API base
4. Select your pulled model in Continue’s model picker

Example minimal config concept (paths vary by OS; see [Continue docs](https://docs.continue.dev/)):

```json
{
  "models": [
    {
      "title": "Qwen2.5 Coder",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:11434"
    }
  ]
}
```

### When local models are enough

- Syntax checks and small transformations
- Drafting commit messages or docstrings
- Learning a new library API at your desk

### When to use cloud tools instead

- Large refactors across many files
- Agents that run tests and iterate on CI failures
- Tight integration with GitHub Issues and PRs

---

## Image generation

AI image tools can help with **conceptual diagrams**, **presentation figures**, and **mockups**. They are poor sources of scientific truth—do not use them for data plots, specimen IDs, or quantitative results.

| Tool | Notes |
|------|--------|
| ChatGPT / DALL·E | Good for rough schematics; check [OpenAI usage policies](https://openai.com/policies) |
| Copilot / VS Code | Some plans support image generation in chat; treat output as draft art |
| Dedicated tools (Midjourney, Ideogram, etc.) | Useful for outreach graphics; document that AI assisted if required by venue |

**Lab practice:** Prefer real data visualizations (ggplot2, matplotlib, etc.) for publication. Use generated images only where accuracy is not implied, and label them as illustrative.

---

## Choosing a workflow (examples)

| Task | Suggested approach |
|------|-------------------|
| Fix a failing R script on your laptop | Copilot **Ask** or **Agent** in VS Code on a branch |
| Implement a filed GitHub issue end-to-end | Assign issue to **Copilot coding agent**, review PR |
| Explain a Slurm error without leaving the terminal | **Codex** or **ChatGPT** with the job log pasted in |
| Quick regex for filenames, no cloud | **Ollama** + Continue |
| Heavy analysis on Klone | VS Code Remote-SSH + Copilot on laptop; run jobs on compute node |
| Figure for a seminar slide (not data) | Image tool + manual cleanup in Illustrator/PowerPoint |

---

## Getting help

- **Lab:** [open a GitHub issue](https://github.com/RobertsLab/resources/issues) on this handbook repo
- **UW Hyak / Klone:** [Hyak documentation](https://hyak.uw.edu/docs/) and [UW-IT office hours](https://calendar.washington.edu/sea_uwit-rc)
- **Copilot access / education:** [GitHub Education](https://education.github.com/)

If something in this page is outdated (models and UIs change quickly), edit the doc via the pencil icon in the handbook or submit a PR.
