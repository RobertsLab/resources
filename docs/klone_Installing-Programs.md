# Containers

Computing on Klone requires the use of containers. Specifically, the Univ. of Washington utilizes [Apptainer](https://apptainer.org/docs/user/main/introduction.html) (formerly Singularity) on Klone for building/executing/running containers. See the [section about containers](./klone_containers.md) for more background info.

The container the Roberts Lab uses hosts virtually all of the software we use. Its location on Klone:

`/gscratch/srlab/containers/srlab-bioinformatics-container-<git_commit_hash>.sif`

- `<git_commit_hash>` is the corresponding git commit for the [container definition file](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-container.def) from which the container was built. This allows users to re-build previous versions of containers, if desired. It also allows users to keep track of which version of the container is being used.

# Alternative: Conda Environments

For users who prefer or need to use conda/miniforge for package management outside of containers, see the [Klone Conda Guide](./klone_Conda.md). This guide covers proper installation locations and configuration to avoid storage limitations.

# Definition file(s)

The definition files are used to build the containers. They also contain all the instructions for software installation. _Software cannot be installed in a container after it is built._ To install new software, the [container definition file](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-container.def) needs to be updated with instructions for downloading and installing the software. Then, a new version of the container needs to be built, in order to incorporate the new software.

The definition file is in a git repo on Klone:

`/gscratch/srlab/gitrepos/RobertsLab/code/apptainer_definition_files/srlab-bioinformatics-container.def`

- To minimize conflicts, please _do not_ modify the git repo on Klone (other than using `git pull` to update the repo). Any changes should be made on your own computer or on GitHub, and then pulled to Klone.

# Building containers

Containers are built using a definition file. Once built, they exist as a single file. Since we're using [Apptainer](https://apptainer.org/docs/user/main/introduction.html) (formerly Singularity), the container files will have the `.sif` suffix. Currently, we use the script [`srlab-bioinformatics-build.sh`](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-build.sh) (GitHub) to build the container directly on Klone. However, the container could be built on any computer running [Apptainer](https://apptainer.org/docs/user/main/introduction.html) (formerly Singularity), and the resulting file could be transferred to Klone. 

The build process must be initiated _manually_. If the definition file(s) is updated, then the user must remember to re-build the container, in order to incorporate the new changes!

# More Resources

- [Klone Conda Guide](./klone_Conda.md) - For installing and configuring conda/miniforge on Klone
- [UW Hyak Documentation](https://hyak.uw.edu/docs) is a great way to start using Hyak (Klone) by providing (relatively) easy to follow walkthrough of how to access Klone, what the different nodes are, examples of how to build containers, and more.