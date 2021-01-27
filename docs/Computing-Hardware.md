# Roberts Lab Computing

Using computers is an integral part of Roberts Lab activities. The majority of our projects take on some form of bioinformatics analysis and manipulation of large data sets. Although we don't perform any high level programming, you will need to become familiar with basic command line syntax.

Below is a list of computing resources we have available, as well as some links to help you begin learning.

---

## Accounts

You will need accounts with the following services in order to minimally function in the Roberts Lab:

- [GitHub](github.com): Needed for posting/responding to [RobertsLab/resources Issues](https://github.com/RobertsLab/resources/issues)

- [Slack](slack.com): Needed for participation in the [Roberts Lab Slack channels](genefish.slack.com)

## Computers
You're free to use your own computer for any computing task that you wish. However, some of the computing work that you will perform will require lengthy run times. As such, we have computers available for you to use. Plus, Roberts Lab computers have better processors and much more RAM, which will allow you to keep your computer free for doing fun stuff, like reading Facebook (or scientific papers).

### Local Computers

Here is a link to a list of computers we have in the lab that are available for use (Google Sheet): [Roberts Lab Computers](https://docs.google.com/spreadsheets/d/1mtIITcjqZVEQtynYZFdOdx51uXTiXP7Jvvzv_SnWCDY/edit?usp=sharing)

The Xserve computers are suitable for most tasks.

  - Two Xserve computers run on Mac OS(X).

  - Two Xserve computers run on Ubuntu (Linux).

The Dell T5500 is dedicated for Windows-only programs.

### Remote Services



## Mox (Hyak)

We have two nodes (a fancy name for a computer) in the University of Washington super-computing cluster, called Mox (formerly Hyak). They're well-suited for resource-intensive computing, like genome assemblies and shotgun proteomics analyses.

Computer specs:

| Model | CPU (dual) | Cores | RAM (GB) |
| ----- | ---------- |----- | -------- |
| Lenovo NextScale | E5-2680 v4 | 28 | 512 |
| Lenovo NextScale | E5-2680 v4 | 28 | 128 |

Due to the initial steep learning curve, we have a dedicated wiki to document how to use Mox:
- [Mox Wiki](https://robertslab.github.io/resources/mox_Adding-a-User/)

## Printers
You can send print jobs wirelessly to the Brother MFC7460DN printer in rm 209.

First, download the [printer driver software](https://support.brother.com/g/b/downloadtop.aspx?c=us&lang=en&prod=mfc7460dn_all) to your computer.

Next, add the printer via system preferences-> printers and scanners for Mac or settings-> devices -> printers and scanners for Windows. You'll need to enter the IP address of the printer which is listed on the [Roberts Lab Computers spreadsheet](https://docs.google.com/spreadsheets/d/1mtIITcjqZVEQtynYZFdOdx51uXTiXP7Jvvzv_SnWCDY/edit#gid=0).

For Macs, you may need to change the 'Use' drop down menu:

- choose 'select software'

- select 'Brother MFC-7460DN CUPS'.

## Software

To limit clutter on this page, we've assembled a list of software currently installed on each lab computer (including our Mox node):

- [Lab Software](https://robertslab.github.io/resources/Lab-Software/)

If you need/want any particular software installed that isn't on the list, please submit a [GitHub Issue](https://github.com/RobertsLab/resources/issues). Please consider that we prefer to use free, open-source software.

## Reproducibility

Reproducibility is of the utmost importance to your, and the Roberts Lab, success! This means that someone (ironically, usually yourself) should be able to look at your notebook and get the same results you did by executing the same commands with the same files you used.

The easiest and most robust means that we've found to aid in this goal is through the use of a [Jupyter Notebook](http://jupyter.org/). A Jupyter Notebook serves as a substitute for your Terminal (i.e. the place where you normally run your commands) and documents all commands that you run in a given session.


- [Review our guide for using Jupyter Notebooks](https://github.com/RobertsLab/code/wiki/Jupyter-Notebook-Guide)

## Learning & Other Resources

### Data Management, Reproducibility, and Collaboration

Please be sure to read the article linked below. It is a great starting point on understanding how to properly manage and manipulate data.

- [Good Enough Practices in Scientific Computing (Wilson et al, 2017)](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)

### Learning the Basics

If you are new to using the command line (and/or other languages like R and Python), don't worry! We all were (and still are), so we know how you feel! The links below are lessons that take you through the basics - no prior experience needed!

- [Software Carpentry Introduction to The Shell (command line)](http://swcarpentry.github.io/shell-novice)

- [Software Carpentry Introduction to Python](http://swcarpentry.github.io/python-novice-inflammation)

- [Software Carpentry Introduction to Python](http://swcarpentry.github.io/r-novice-inflammation)

### Roberts Lab Resources

We have also compiled our own sets of useful bits of code (mostly "one-liners") for common tasks in our dedicated [code repo](https://github.com/RobertsLab/code).

This is a particularly handy resource if you're getting stuck trying to manipulate a file and/or extract some basic info from the file (decompressing, compressing, and counting words/lines/sequences).

Additionally, the [code Wiki](https://github.com/RobertsLab/code/wiki) has in-depth guides on more complex, but commonly used, computing topics.
