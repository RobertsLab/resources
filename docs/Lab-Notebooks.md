We have been using online lab notebooks since 2007 and the platforms and workflows have certainly changed over the years. Below is a compendium of best practices based on our experience and the particular research we do. This is intended for those in our lab group, however [comments and suggestions are welcome](https://github.com/RobertsLab/resources/issues).


An online lab notebook is required of all lab members. Entries need to be organized by date and in reverse chronological order, and **Updated daily**.

## Notebooks

Person | Notebook  | Commitment
--- | --- | ----
Steven Roberts | [sr320.github.io](https://sr320.github.io/) |  ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/sr320.github.io)
Sam White | [robertslab.github.io](https://robertslab.github.io/sams-notebook/) |  ![GitHub last commit](https://img.shields.io/github/last-commit/RobertsLab/sams-notebook)
Matt George | [mattgeorgephd.github.io](https://mattgeorgephd.github.io/notebook/) | ![GitHub last commit](https://img.shields.io/github/last-commit/mattgeorgephd/mattgeorgephd.github.io)
Aspen Coyle | [afcoyle.github.io](https://afcoyle.github.io) |   ![GitHub last commit](https://img.shields.io/github/last-commit/afcoyle/afcoyle.github.io)
Olivia Cattau | [ocattau.github.io](https://ocattau.github.io/notebook-2/)  | ![GitHub last commit](https://img.shields.io/github/last-commit/ocattau/notebook-2)
Delaney Lawson| [drlawson.github.io](https://drlawson.github.io)  | ![GitHub last commit](https://img.shields.io/github/last-commit/drlawson/drlawson.github.io)
Ariana Huffmyer | [ahuffmyer.github.io](https://ahuffmyer.github.io/ASH_Putnam_Lab_Notebook/) | ![GitHub last commit](https://img.shields.io/github/last-commit/AHuffmyer/ASH_Putnam_Lab_Notebook)
Chris Mantegna | [chrismantegna.github.io](https://chrismantegna.github.io/) | ![Github last commit](https://img.shields.io/github/last-commit/ChrisMantegna/ChrisMantegna.github.io)
Zach Bengtsson | [zbengt.github.io](https://zbengt.github.io/notebook/) | ![Github last commit](https://img.shields.io/github/last-commit/zbengt/zbengt.github.io)
Larken Root | [larkenr.github.io](https://larkenr.github.io) | ![Github last commit](https://img.shields.io/github/last-commit/larkenr/larkenr.github.io)
Laura Spencer | [laurahspencer.github.io](https://laurahspencer.github.io/LabNotebook/)  | [![GitHub followers](https://img.shields.io/github/followers/laurahspencer.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/laurahspencer)
Yaamini Venkataraman | [yaaminiv.github.io](https://yaaminiv.github.io/) | [![GitHub followers](https://img.shields.io/github/followers/yaaminiv.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/yaaminiv)
Grace Crandall | [grace-ac.github.io](https://grace-ac.github.io/) |  [![GitHub followers](https://img.shields.io/github/followers/grace-ac.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/grace-ac)
Shelly Trigg | [shellytrigg.github.io/notebook](https://shellytrigg.github.io/notebook/) |   [![GitHub followers](https://img.shields.io/github/followers/shellytrigg.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/shellytrigg)

## Platforms

# Quarto

One of the great features of Quarto is using it to create websites. What is really cool is the ability to used code chunks you might be already be familiar with. Unique features include callouts and tabs. These websites can be quite simple with only a single page, a blog, or more complex with multiple pages and options, such as the website for this course. Websites created with **Quarto** can be viewed/hosted directly on **GitHub**, or copied over to a server such as <http://students.washington.edu>.

------------------------------------------------------------------------

# Setup

For this exercise, we'll create a simple personal blog and host it on **GitHub**. See also <https://quarto.org/docs/websites/website-blog.html>

## Create RStudio project

Create a new project in **RStudio**. However, rather than base this new project on an existing repo, as we've done in the past, we'll instead choose **New Directory**.

```{r rs_new_proj, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/rs_new_project.png")
```

<br>

Scroll down the options for **Project Type** and select Quarto Blog.

```{r rs_blog, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/rs_blog.png")
```

<br>

In the next window, enter your a name for `Directory name:`

Choose the location where you'd like this new project to live.

When you are finished, check the box next to `Open in new session` and click the **Create Project** button.

```{r rs_dir, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/rs_blogdir.png")
```

<br>

# Prepare for GitHub Publishing

## Render to `docs`

```{r rs_docs, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/rs_docs.png")
```

You could also change the theme, blog title, links, etc here.

## add a `.nojekyll` file

```{r rs_no, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/rs_noj.png")
```

## Render

```{r rs_render, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/rs_render.png")
```

## Commit and Push

First time needs to be done via command line or GitHub Desktop, then could be done all within RStudio.

```{r gh_desktop, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/gh_desktop.gif")
```

<br>

------------------------------------------------------------------------

# Publish with GitHub Pages

Now we can go to the repo in GitHub and set source for deployment.

```{r pages, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/gh_pages.gif")
```

```{r live, echo = FALSE, out.width = "70%", fig.align = "center"}
knitr::include_graphics("img/gh_live.gif")
```

Everthing should be live.

<br>

------------------------------------------------------------------------

# Creating a new post

Add a new post to your blog by creating a sub-directory within `posts`, and adding an `index.qmd`file to the directory. That `qmd` file is the new blog post and when you render that, the blog home page will automatically update to include the newest post at the top of the listing. For more options see <https://quarto.org/docs/websites/website-blog.html#posts-directory>




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

All GitHub-based notebooks are also backed up to Gannet: https://gannet.fish.washington.edu/github_backups/notebooks/

---

## Archive

Aspen:

- github.io:
    - 2020: `https://github.com/afcoyle/afcoyle.github.io/archive/v2020.zip`

Chris:

- gitbhu.io:

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

Olivia:

- github.io:

Sam:

- github.io:
    - 2021: `https://github.com/RobertsLab/sams-notebook/archive/refs/tags/v2021.zip`
    - 2020: `https://github.com/RobertsLab/sams-notebook/archive/v2020.zip`
    - 2019: `https://github.com/RobertsLab/sams-notebook/archive/v2019.zip`
- Jupyter notebooks and R Projects:
    - 2021: `https://github.com/RobertsLab/code/archive/refs/tags/v2021.zip`
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

- github.io:
    - 2020: `https://github.com/yaaminiv/yaaminiv.github.io/archive/v2020.zip`
    - 2019: `https://github.com/yaaminiv/yaaminiv.github.io/archive/v2019.zip`

Zach:

- github.io:
