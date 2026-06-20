# Offboarding

When you leave the [Roberts Lab](https://faculty.washington.edu/sr320) — graduating, finishing a postdoc or appointment, wrapping up an undergraduate position, or moving on for any reason — the goal is simple: **your work stays usable by the lab, and you leave with copies of everything that is yours to keep.**

Use this page as a checklist. Start **2–4 weeks before your last day** so nothing depends on access you no longer have. Work through it with Steven, and check items off as you go.

!!! tip "The one-line rule"
    Everything that matters lives in a **GitHub repository** under [RobertsLab](https://github.com/RobertsLab), on the lab servers, or in a shared lab account — **not** on your laptop, your personal cloud drive, or in your head. If it only exists in one of those places, move it before you go.

---

## 1. Data — make sure nothing is stranded

The lab must retain all research data, and you are welcome to keep copies of work you contributed to.

- [ ] **Raw data** (sequencing reads, images, instrument output, field/experimental measurements) is on the lab servers and/or in a permanent archive (e.g., [NCBI SRA/GEO](https://www.ncbi.nlm.nih.gov/sra), [OWL/Gannet](Computing-Hardware.md)). Note accession numbers in the relevant repo.
- [ ] **Processed/analyzed data** and intermediate files are stored or clearly reproducible from code. Large files belong on lab storage (Gannet/Owl), not in Git — link to them.
- [ ] **Metadata** is complete: sample sheets, README files, units, and collection details so someone else can interpret the data without you. See [Data Management](Data-Management.md).
- [ ] **Physical samples** (extractions, tissues, slides, plates) are labeled and logged in the [Lab Inventory](Lab-Inventory.md) / [Experiment Database](Experiment-Database.md), with freezer/box locations recorded.
- [ ] **Your personal copy:** export or download any data you are entitled to keep. Confirm with Steven what you may take and in what form.

## 2. GitHub — transfer ownership, don't take it with you

All lab project repositories should live in the [RobertsLab GitHub organization](https://github.com/RobertsLab), not in your personal account.

- [ ] **Move any project repos** currently under your personal account into the RobertsLab org (Repo → Settings → *Transfer ownership*). If a repo can't be transferred, push a complete copy to a RobertsLab repo.
- [ ] **Push your final commits.** No uncommitted or unpushed work on your local machine.
- [ ] **Update each repo's README** so a new person can pick it up: what the project is, where the data lives, how to run the analysis, and current status.
- [ ] **Open issues / loose ends** are written down as GitHub Issues so they aren't lost.
- [ ] **Your lab notebook** ([GitHub-based](Lab-Notebooks.md)) is complete and remains in the org.
- [ ] After your access is removed, you keep your **personal GitHub account** — you can keep forks/copies of public work, but the org's copy is the canonical one.

## 3. Notebooks and code — leave it reproducible

- [ ] **Lab notebook** is up to date through your last working day and stays accessible to the lab.
- [ ] **Analysis notebooks** (Jupyter `.ipynb`, R Markdown / Quarto `.qmd`/`.Rmd`, scripts) are committed to the relevant repo and **run top-to-bottom** from the data described in the README.
- [ ] **Environments are captured** — `environment.yml`, `renv.lock`, `requirements.txt`, or a container — so the analysis can be re-run later. See [Computing Best Practices](Computing-Best-Practices.md).
- [ ] **Your personal copies:** clone/download the repos and notebooks you want to keep before access is removed.

## 4. Keys, accounts, and access — hand off, then have it revoked

Make a quick list of everything you can log into for the lab, then work through it.

- [ ] **Server access** ([Klone/Hyak](klone_quick-start.md), Raven, Gannet, Owl, lab workstations): confirm your files are off your personal home directories and onto shared/permanent storage, then have your accounts deactivated.
- [ ] **Shared credentials / API keys / tokens** you used (cloud, database, instrument, sequencing-core, service accounts): identify them so they can be **rotated**. Never email keys in plain text or leave them in committed code — see [Data Management](Data-Management.md).
- [ ] **GitHub:** any personal access tokens or deploy keys tied to lab repos are revoked.
- [ ] **Communication & shared accounts:** lab [Slack](https://genefish.slack.com/), [Lab Calendar](https://calendar.google.com/calendar/embed?src=mrc305%40gmail.com&ctz=America/Los_Angeles), shared Google Drive folders, Zotero/citation groups, social or project accounts — transfer anything you alone control, then have your access removed.
- [ ] **Physical access:** return keys/fobs, and have building/room and freezer access updated per [Lab Safety](Lab-Safety.md).
- [ ] **UW accounts:** know that your NetID, UW email, and UW-licensed software access typically expire after you leave — move anything you need out of UW-only systems first.

## 5. Knowledge transfer — so the work continues

- [ ] **Hand off active projects** to a named lab member (or to Steven), with a short written summary: status, what's next, where everything lives.
- [ ] **Manuscripts in progress:** confirm authorship, share the latest drafts and source files (figures, code, data), and agree on who carries each paper forward. See [Writing Scientific Manuscripts](Writing.md) and [Pubathon](Pubathon.md).
- [ ] **Document the undocumented:** protocols, scripts, or "tricks" only you know go into the repo or [Protocols](Computing-Best-Practices.md) wiki.
- [ ] **Update [Project Management](Project-Management.md)** boards/issues to reflect reality.

## 6. Stay connected

- [ ] **Forwarding contact:** give Steven a personal (non-UW) email and, if you like, your new affiliation so we can reach you about papers, data questions, and references.
- [ ] **ORCID & affiliations:** make sure your [ORCID](https://orcid.org/) record reflects the lab and your publications.
- [ ] **Letters of recommendation / references:** let Steven know if you'll need them — easier to arrange before you go.
- [ ] **Keep in touch.** Alumni are part of the lab community; you're welcome to stay in the relevant channels and at lab events.

---

## Final checklist (the short version)

| Area | Done when… |
|------|------------|
| **Data** | Raw + processed data and metadata are on lab storage/archives; samples are logged; you have your personal copies |
| **GitHub** | All project repos are under [RobertsLab](https://github.com/RobertsLab) with current READMEs; nothing unpushed |
| **Notebooks/code** | Notebooks run end-to-end; environments captured; lab notebook complete |
| **Keys & access** | Shared keys flagged for rotation; server/UW/personal accounts handled; physical keys returned |
| **Knowledge transfer** | Active projects + manuscripts handed off in writing; authorship confirmed |
| **Stay connected** | Forwarding email shared; ORCID updated; references arranged |

---

*Questions about what you may keep, what must stay, or how to transfer something? Ask Steven before your last day.* See also [Onboarding](Onboarding.md), [Data Management](Data-Management.md), and [Environment and Expectations](Environment-and-Expectations.md).
