We have been using online lab notebooks since 2007 and the platforms and workflows have certainly changed over the years. Below is a compendium of best practices based on our experience and the particular research we do. This is intended for those in our lab group, however [comments and suggestions are welcome](https://github.com/RobertsLab/resources/issues).


An online lab notebook is required of all lab members. Entries need to be organized by date and in reverse chronological order.

## Notebooks

Person | Notebook  | Commitment
--- | --- | ----
Steven Roberts | [sr320.github.io](https://sr320.github.io/) |  ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/sr320.github.io)
Sam White | [robertslab.github.io](https://robertslab.github.io/sams-notebook/) |  ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/sams-notebook)
Matt George | [mattgeorgephd.github.io](https://mattgeorgephd.github.io/notebook/) | ![GitHub last commit](https://img.shields.io/github/last-commit/mattgeorgephd/mattgeorgephd.github.io)
Aidan Coyle | [afcoyle.github.io](https://afcoyle.github.io) |   ![GitHub last commit](https://img.shields.io/github/last-commit/afcoyle/afcoyle.github.io)
Olivia Cattau | [ocattau.github.io](https://ocattau.github.io)  | ![GitHub last commit](https://img.shields.io/github/last-commit/ocattau/ocattau.github.io)
Delaney Lawson| [drlawson.github.io](https://drlawson.github.io)  | ![GitHub last commit](https://img.shields.io/github/last-commit/drlawson/drlawson.github.io)
Ariana Huffmyer | [ahuffmyer.github.io/](https://ahuffmyer.github.io/ASH_Putnam_Lab_Notebook/) | ![GitHub last commit](https://img.shields.io/github/last-commit/AHuffmyer/ASH_Putnam_Lab_Notebook)
Laura Spencer | [laurahspencer.github.io](https://laurahspencer.github.io/LabNotebook/)  | [![GitHub followers](https://img.shields.io/github/followers/laurahspencer.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/laurahspencer)
Yaamini Venkataraman | [yaaminiv.github.io](https://yaaminiv.github.io/) | [![GitHub followers](https://img.shields.io/github/followers/yaaminiv.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/yaaminiv)
Grace Crandall | [grace-ac.github.io](https://grace-ac.github.io/) |  [![GitHub followers](https://img.shields.io/github/followers/grace-ac.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/grace-ac)
Shelly Trigg | [shellytrigg.github.io/notebook](https://shellytrigg.github.io/notebook/) |   [![GitHub followers](https://img.shields.io/github/followers/shellytrigg.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/shellytrigg)



## Platforms

The preferred platform is GitHub. See [Laura's Notebook](laurahspencer.github.io/LabNotebook/), [Steven's Notebook](sr320.github.io), or [Yaamini's Notebook](yaaminiv.github.io).

*Guide to creating a notebook on GitHub:*

One way to approach is simply to to follow the instructions at https://github.com/barryclark/jekyll-now. This is what our Notebooks are forks of.

To leverage the modifications Steven has made...

1) Fork his repository associated with his notebook: https://github.com/sr320/sr320.github.io.   
[Screencast](http://owl.fish.washington.edu/scaphapoda/grace/Github-noteboook.mov)

2) Change the user name associated the repository name in the Settings.

3) Revise the config.xml file to include your own personal information

4) Alter line 49 of `your_username.github.io/_layouts/default.html` so clicking on "admin" link takes you to your `_posts` directory.

5) Go to Disqus to set up comments for your website. Pick a page name, ignore instructions on adding code to your site. Complete registration.

6) Go back to config.xml file and add your Disqus shortname. This will magically alter code so comments will show up for each posts.

Note sometimes revisions take a few minutes to render on GitHub.


—-

Other options include:
- [genefish.wordpress.com](https://genefish.wordpress.com) (ask Steven for an account). See [Grace's Notebook](https://genefish.wordpress.com/author/graceac9/)

## Make sure it is reproducible
Document in a fashion where someone could replicate your work.

## Document daily
A record of your work should be published the day of activity. Yep, daily! Even if you feel like you did nothing, post <em>something</em> to describe what you did that day. Did you read some papers? Great! Make a post that lists the papers you read. Did you spend all day searching the web? Also great! Make a post about what you were searching for and how successful you were in finding what you wanted.

## Maintain backup
Have a copy of your notebook in another location. This could be done in several ways.
- composing in text editor and hosting on GitHub
- using IFTTT to post/save entries elsewhere
- run script (i.e. wget) to archive contents

Periodically, you will be asked to show where your backup is and demonstrate that it is functional.

---

## Archive

Aidan:

- github.io:
  - 2020: `https://github.com/afcoyle/afcoyle.github.io/archive/v2020.zip`

Grace:

- github.io:
  - 2020: `https://github.com/grace-ac/grace-ac.github.io/archive/v2020.zip`

Jay:

- ONS:
  - 2018: `https://eagle.fish.washington.edu/trilobite/notebooks/jay.zip`

Jake:

- Blogspot:
  - 2015: `https://eagle.fish.washington.edu/trilobite/notebooks/jake.zip`

Laura:

- github.io:
  - 2020: `https://github.com/laurahspencer/LabNotebook/archive/v2021.zip`
  - 2019: `https://github.com/laurahspencer/LabNotebook/archive/v2019.zip`

Matt:

- github.io:
  - 2020: `https://github.com/mattgeorgephd/mattgeorgephd.github.io/archive/v2020.zip`

Megan:

- github.io:
  - 2020: `https://github.com/meganewing/meganewing.github.io/archive/v2020.zip`

Sam:

- github.io:
  - 2020: `https://github.com/RobertsLab/sams-notebook/archive/v2020.zip`
  - 2019: `https://github.com/RobertsLab/sams-notebook/archive/v2019.zip`
- Jupyter notebooks and R Projects:
  - 2020: `https://github.com/RobertsLab/code/archive/v2020.zip`
  - 2019: `https://github.com/RobertsLab/code/archive/v2019.zip`

Shelly:

- github.io:
  - 2020: `https://github.com/shellytrigg/shellytrigg.github.io/archive/v2020.zip`


Steven:

- github.io:
  - 2020: `https://github.com/sr320/nb-2020/archive/v1.0.zip`
  - 2019: `https://github.com/RobertsLab/resources/blob/master/archive/sr320.github.io-2019.zip`
- ONS:
  - 2016: `https://eagle.fish.washington.edu/trilobite/notebooks/steven.zip`


Yaamini:

-  github.io:
  - 2020: `https://github.com/yaaminiv/yaaminiv.github.io/archive/v2020.zip`
  - 2019: `https://github.com/yaaminiv/yaaminiv.github.io/archive/v2019.zip`
