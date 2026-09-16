# Roberts Lab Resources

This repository serves as the central hub for [Roberts Lab](http://faculty.washington.edu/sr320/) members, containing comprehensive documentation, protocols, and guidance for all aspects of lab operations. Whether you're a new member getting started or an experienced researcher looking for specific protocols, this repository provides the resources you need.

## 📖 Quick Start

- **New to the lab?** Start with the [Roberts Lab Handbook](https://robertslab.github.io/resources/) and its [Onboarding](https://robertslab.github.io/resources/Onboarding/) checklist
- **Looking for protocols?** Browse our [Lab Protocols](https://github.com/RobertsLab/resources/tree/master/protocols) collection
- **Need computing resources?** See [Computing Hardware](https://robertslab.github.io/resources/Computing-Hardware/), which shows live up/down status for raven, gannet, and klone
- **Looking for data?** Try the [Histology Databank Explorer](https://robertslab.github.io/resources/histology-explorer/) or [Genomic Resources](https://robertslab.github.io/resources/Genomic-Resources/)
- **Need help or have questions?** Submit an [issue](https://github.com/RobertsLab/resources/issues) or join the discussion on [Slack](https://genefish.slack.com)
- **Major research projects** can be found [here](https://github.com/RobertsLab?utf8=%E2%9C%93&q=project&type=&language=)

## 🤝 How to Interact with This Repository

### For All Lab Members:
- **Browse resources**: Navigate through folders and files to find what you need
- **Search**: Use GitHub's search function to quickly locate specific information
- **Stay updated**: Watch this repository for notifications about important updates

### Contributing and Getting Help:
- **Report issues**: Found something outdated or incorrect? [Submit an issue](https://github.com/RobertsLab/resources/issues/new/choose) — templates are available for general lab support, access requests, and coding problems
- **Suggest improvements**: Use [GitHub Discussions](https://github.com/RobertsLab/resources/discussions) for ideas and feedback  
- **Make edits**: Click the pencil icon (✏️) on any page to edit directly, or submit a pull request
- **Join conversations**: Connect with lab members on [Slack](https://genefish.slack.com)

### Communication Channels:
- **GitHub Issues**: For troubleshooting, requests, and lab meeting topics
- **GitHub Discussions**: For broader conversations and feedback
- **Slack**: For day-to-day lab communication ([genefish.slack.com](https://genefish.slack.com))

[![issues](https://img.shields.io/github/issues/RobertsLab/resources.svg)](https://github.com/RobertsLab/resources/issues)
![GitHub Discussions](https://img.shields.io/github/discussions/RobertsLab/resources)
![GitHub contributors](https://img.shields.io/github/contributors/RobertsLab/resources)

---

## 📁 Repository Structure

### Core Documentation:
- **`docs/`**: Source files for the [Roberts Lab Handbook](https://robertslab.github.io/resources/) including:
  - Lab culture: onboarding and offboarding, code of conduct, expectations, safety
  - How we work: communication, project management, lab notebooks, data management
  - Guides: scientific writing, oral presentations, outreach slides
  - Computing and code: best practices, agentic coding tools, hardware, Klone and Raven guides
  - Bioinformatic workflows: annotation, DNA methylation, gene expression, transcriptome assembly
  - Self-directed tutorials (standalone HTML): `bash-tutorial.html`, `github-tutorial.html`, `agentic-ai-bootcamp.html`, `bivalve-histology-tutorial/`

### Data Catalogs and Web Tools:
- **`docs/histology-explorer/`**: [Histology Databank Explorer](https://robertslab.github.io/resources/histology-explorer/) — static site for searching the histology databank by species, project, year, tissue, and researcher, with links to slide images on owl. Includes the build scripts that regenerate its data (`build/build_index.py`, `build/make_derivatives.py`) — see its [README](docs/histology-explorer/README.md)
- **`data-portal/`**: Self-contained portal for browsing the lab's sequencing libraries (Nightingales) and reference genomes. `build.py` regenerates `nightingales.json` from the Nightingales sheet export and `genomes.json` from `docs/Genomic-Resources.md`
- **`igv_server/`**: IGV genome registry and annotation files for the lab's IGV server

### Lab Resources:
- **`protocols/`**: Comprehensive collection of lab protocols, including both custom procedures and commercial kit protocols. Note that protocols surfaced in the handbook navigation live in `docs/protocols/`
- **`equipment_manuals/`**: Equipment documentation and user manuals
- **`lab_safety_docs/`**: Safety training materials and documentation

### Automation:
- **`.github/workflows/`**: Deploys the handbook to GitHub Pages on push to `master`, probes server status every 15 minutes, and checks for broken links in Markdown files
- **`.github/ISSUE_TEMPLATE/`**: Issue templates for lab support requests, access requests, and coding issues
- **`scripts/`**: Server status probers (`check_servers.py`, `publish_status.sh`) that power the status lights on the Computing Hardware page. Results are published to the orphan `server-status` branch by both a GitHub Action and an in-network cron job, since raven is not reachable from outside the UW network — see [scripts/README.md](scripts/README.md)

### Administrative:
- **`mkdocs.yml`**: Configuration and navigation for the [MkDocs](https://www.mkdocs.org/) handbook site
- **`.readthedocs.yml`**: Read the Docs build configuration (the live handbook is deployed to GitHub Pages by the workflow above)
- **`histology_request_form_2019.pdf`**: Histology sample submission form for consultation services

### Additional Resources:
- **`archive/`**: Historical documents and archived materials
- **`img/`**: Images and media files used throughout the documentation
