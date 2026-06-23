
There are a variety of hardware and software options and combinations available to you. While there are few concrete rules, here is an attempt to guide your success.


Resources for thinking about open and reproducible scientific computing.


!!! tip "New to Git &amp; GitHub? Start with the tutorial"
    The **[Git &amp; GitHub Tutorial](../github-tutorial.html)** is a self-paced, hands-on walkthrough of the everyday version-control loop — creating a repository, syncing with the **GitHub Desktop** app, making changes, and committing and pushing — with an advanced section covering the same workflow on the command line. Work through it first if version control is new to you.

## Practical Aspects

Foremost, code should be written so someone else could easily run. This means they have access and can understand.

1) Code should be in a Github repository 

2) [Organize](https://kbroman.org/steps2rr/pages/organize.html) your data and code. 

Here's an example of how repos should be organized. Note that each directory contains a `README.md`, which describes the contents of each directory (and, sometimes even describes each file in that directory).

Create a dedicated directory for GitHub repositories and then keep all subsequent repositories within it. On a personal computer, a common choice is `~/GitHub/`; on shared or lab systems, follow the local convention. Do not store GitHub repositories inside folders that automatically sync with iCloud Drive, Dropbox, Google Drive, or OneDrive. Sync services can interfere with Git and create conflicted or corrupted repository state.

Once a repository is cloned, do not casually move or rename it. Code, notebooks, relative paths, project settings, and Git configuration may depend on the repository location. If a repository needs to move, ask for help first.

```
gitrepos$ tree

.
├── <GitHub username>
│   └── Project-01
│       ├── code
│       │   ├── 01-FastQ-QC.Rmd
│       │   ├── 02-DESeq2
│       │   └── README.md
│       ├── data
│       │   ├── genome-features
│       │   │   └── README.md
│       │   ├── raw
│       │   │   └── README.md
│       │   └── README.md
│       ├── outputs
│       │   ├── 01-FastQ-QC
│       │   │   ├── figures
│       │   │   │   └── README.md
│       │   │   └── README.md
│       │   ├── 02-DESeq2
│       │   │   ├── figures
│       │   │   │   └── README.md
│       │   │   └── README.md
│       │   └── README.md
│       └── README.md
└── RobertsLab
    ├── lab-website
    │   └── README.md
    ├── README.md
    ├── resources
    │   └── README.md
    └── tusk
        └── README.md
```


### Working with Git and RStudio on Raven

<html>
<body>

<video width="640" height="480" controls>
  <source src="https://gannet.fish.washington.edu/seashell/snaps/rstudio-rav.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

</body>
</html>

related - getting a Personal Access token - https://d.pr/i/lS8UAr




## Papers

- [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)

- [Packaging data analytical work reproducibly using R (and friends)](https://peerj.com/preprints/3192/)


## Workshops

- [A crash-course in using a project-oriented workflow with Git + GitHub in scientific research](https://github.com/OARS-SAFS/projects-with-github)


## Courses

- [FISH546 - Bioinformatics for Environmental Sciences](https://github.com/sr320/course-fish546-2021/wiki)

- [FISH274 - Introduction to Data Analysis for Aquatic Sciences](https://sr320.github.io/course-fish274-2021/)

- [Data Carpentry for Biologists](https://datacarpentry.org/semester-biology/)
