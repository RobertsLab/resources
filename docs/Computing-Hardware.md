# Roberts Lab Computing

Using computers is an integral part of Roberts Lab activities. The majority of our projects take on some form of bioinformatics analysis and manipulation of large data sets. Although we don't perform any high level programming, you will need to become familiar with basic command line syntax.

Below is a list of computing resources we have available, as well as some links to help you begin learning.

---

## Accounts

You will need accounts with the following services in order to minimally function in the Roberts Lab:

- [GitHub](https://github.com): Needed for posting/responding to [RobertsLab/resources Issues](https://github.com/RobertsLab/resources/issues)

- [Slack](https://slack.com): Needed for participation in the [Roberts Lab Slack channels](https://genefish.slack.com)

## Computers
You're free to use your own computer for any computing task that you wish. However, some of the computing work that you will perform will require lengthy run times. As such, we have computers available for you to use. Plus, Roberts Lab computers have better processors and much more RAM, which will allow you to keep your computer free for doing fun stuff, like reading Facebook (or scientific papers).

### Local Computers

Here is a table of computers we have in the lab that are available for use:

| Name        | Operating System                       | Location | CPU Cores                       | Memory          | Storage               | Primary Use                              | External Drives |
|-------------|----------------------------------------|----------|---------------------------------|-----------------|-----------------------|------------------------------------------|-----------------|
| genefish    | macOS Sierra (10.12), Windows 7        | 230      | 2.3 GHz Intel Core i7 Quad Core | 16GB            | 1TB                   |                                          |                 |
|             | Windows 7 Enterprise (64-bit)          | 228      |                                 |                 |                       | qPCR                                     |                 |
| woodpecker  | Windows 7 Enterprise (64-bit)          | 209      | 16                              | 64GB            | 2TB                   | Bioanalyzer;NanoDrop;NanoPore;proteomics |                 |
| swoose      | Ubuntu 16.04.1/Windows 10 Pro (64-bit) | 209      | 24                              | 72GB            | 1.5TB                 | Sam                                      | 8TB             |
| swan        | Windows 7 Enterprise (64-bit)          | Brinnon  | 24                              | 72GB            | 500GB                 | titrator                                 |                 |
| raven       | Ubuntu (18.04LTS)                      | 213      | 48                              | 256GB           | 1TB                   |                                          | 2 x 1TB         |


A more detailed spreadsheet, including IP addresses is below (Google Sheet). You'll need to request access from Steven or Sam.

- [Roberts Lab Computers](https://docs.google.com/spreadsheets/d/1mtIITcjqZVEQtynYZFdOdx51uXTiXP7Jvvzv_SnWCDY/edit?usp=sharing)

### Remote Services



## Mox (Hyak)

We have two nodes (a fancy name for a computer) in the University of Washington super-computing cluster, called Mox (formerly Hyak). They're well-suited for resource-intensive computing, like genome assemblies and shotgun proteomics analyses.

Computer specs:

| Model | CPU (dual) | Cores | RAM (GB) |
| ----- | ---------- |----- | -------- |
| Lenovo NextScale | E5-2680 v4 | 28 | 512 |
| Lenovo NextScale | E5-2680 v4 | 28 | 128 |

Due to the initial steep learning curve, we have a dedicated section on how to use Mox:

- [New Mox User](mox_Adding-a-User.md)

## Printers
You can send print jobs wirelessly to the Brother HL-L2395DW395DW printer in rm 209.

Windows computers:

1. Download the [printer driver software](https://support.brother.com/g/b/downloadtop.aspx?c=us&lang=en&prod=hll2395dw_us_as) to your computer.

2. Add the printer via: Settings-> Devices -> Printers and Scanners. You'll need to enter the IP address of the printer which is listed on the [Roberts Lab Computers spreadsheet](https://docs.google.com/spreadsheets/d/1mtIITcjqZVEQtynYZFdOdx51uXTiXP7Jvvzv_SnWCDY/edit#gid=0).

For Macs:

1. Add the printer via: System preferences-> Printers and scanners. You'll need to enter the IP address of the printer which is listed on the [Roberts Lab Computers spreadsheet](https://docs.google.com/spreadsheets/d/1mtIITcjqZVEQtynYZFdOdx51uXTiXP7Jvvzv_SnWCDY/edit#gid=0).

  - You may need to change the 'Use' drop down menu:

    - Choose 'select software'

    - Select 'Brother HL-L2395DW CUPS'.

  - You will need to change the *Protocol* to 'HP Jetdirect-Socket'.

## Software

To limit clutter on this page, we've assembled a list of software currently installed on each lab computer (including our Mox node):

- [Lab Software](Lab-Software.md)

If you need/want any particular software installed that isn't on the list, please submit a [GitHub Issue](https://github.com/RobertsLab/resources/issues). Please consider that we prefer to use free, open-source software.

## Reproducibility

Reproducibility is of the utmost importance to your, and the Roberts Lab, success! This means that someone (ironically, usually yourself) should be able to look at your notebook and get the same results you did by executing the same commands with the same files you used.

The easiest and most robust means that we've found to aid in this goal is through the use of a [Jupyter Notebook](http://jupyter.org/). A Jupyter Notebook serves as a substitute for your Terminal (i.e. the place where you normally run your commands) and documents all commands that you run in a given session.


- [Review our guide for using Jupyter Notebooks](Jupyter-Notebook-Guide.md)

## Learning & Other Resources

### Data Management, Reproducibility, and Collaboration

Please be sure to read the article linked below. It is a great starting point on understanding how to properly manage and manipulate data.

- [Good Enough Practices in Scientific Computing (Wilson et al, 2017)](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)

### Learning the Basics

If you are new to using the command line (and/or other languages like R and Python), don't worry! We all were (and still are), so we know how you feel! The links below are lessons that take you through the basics - no prior experience needed!

- [Software Carpentry Introduction to The Shell (command line)](http://swcarpentry.github.io/shell-novice)

- [Software Carpentry Introduction to Python](http://swcarpentry.github.io/python-novice-inflammation)

- [Software Carpentry Introduction to R](http://swcarpentry.github.io/r-novice-inflammation)
