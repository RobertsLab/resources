# Containers

Computing on Klone requires the use of containers. See the [section about containers](./klone_containers.md) for more background info.

The container the Roberts Lab uses hosts virtually all of the software we use. Its location on Klone:

`/gscratch/srlab/containers/srlab-bioinformatics-container-<git_commit_hash>.sif`

- `<git_commit_hash>` is the corresponding git commit for the [container definition file](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-container.def) from which the container was built. This allows users to re-build previous versions of containers, if desired. It also allows use to keep track of which version of the container is being used.

# Definition file(s)

The definition files are used to build the containers. They also contain all the instructions for software installation. _Software cannot be installed in a container after it is built._ To install new software, the [container definition file](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-container.def) needs to be updated with instructions for downloading and installing the software. Then, a new version of the container needs to be built, in order to incorporate the new software.

The definition file is in a git repo on Klone:

`/gscratch/srlab/gitrepos/RobertsLab/code/apptainer_definition_files/srlab-bioinformatics-container.def`

- To minimize conflicts, please _do not_ modify the git repo on Klone (other than using `git pull` to update the repo). Any changes should be made on your own computer or on GitHub, and then pulled to Klone.

# Building containers

