# What is a container?

A container is a self-contained, virtual computer. It exists as a file on your computer, but when run, can be interacted with as though the user is using a different computer.

## Why use containers?

For our use case(s), reproducibility is the biggest advantage. Since containers function as virtual computers, if everyone uses the same container, then we know the exact conditions and programs that were used to run analyses. There are no concerns about different people using different versions of software and/or operating systems. Another benefit to using containers, is that containers are portable. Because a container is just a file, it can easily be shared with someone else and that person will be able to run analyses exactly as you've run them, without the need to install the programs needed for the analyses.

Additionally, using containers allows us to install software without modifying the underlying operating system. Some software installations are more complex than others and containers reduce the risk that we accidentally modify the underlying operating system in a way which screws things up.

# Creating containers

Containers are created from a definition file. A definition file provides all the instructions on what the resulting container should contain - things like which operating system, which programs, which files, directory stucture, etc). Once a definition file is set up, then the user can instruct the container program (Apptainer in our case) to build the container from the definition file. The resulting container functions as an independent computing system, but is actually just a file. This means a user can easily move this file (container) to other computers and run the container exactly the same way on any system.

The Roberts Lab currently uses a single definition file: [`srlab-bioinformatics-container.def`](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-container.def). Our goal is to keep things as simple as possible. Everyone will use the same container and same versions of programs. The downside to this is that the resulting container file is large (> 2GB) and is time consuming to build, however, portability is not our primary concern, nor do we ancticipate having to update/rebuild the container regularly. Other labs may have completely separate containers for:

- individual software/program

- dedicated pipeline (e.g. HISAT2, StringTie, DESeq2)

For lab-specific guides on building/using containers in the Roberts Lab, specifically written for use on our HPC system, Klone:

- [Klone Quick Start Guide](./klone_quick-start.md)

- [Klone Installing Programs](./klone_Installing-Programs.md)

- [Klone Running a Job](./klone_Running-a-Job.md)

- [Klone RStudio Server](./klone_RStudio-Server.md)