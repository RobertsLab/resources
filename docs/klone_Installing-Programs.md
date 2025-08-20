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

# Adding Python Packages

Python packages can be added to the Roberts Lab Apptainer container through the [container definition file](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-container.def). Since _software cannot be installed in a container after it is built_, Python packages must be installed during the container build process.

## Methods for Installing Python Packages

There are several approaches to add Python packages to the container:

### Method 1: System Python packages (via apt)

For basic Python packages available in Ubuntu repositories, add them to the `%post` section in the definition file:

```bash
%post
    # ... existing apt install commands ...
    python3-numpy \
    python3-pandas \
    python3-matplotlib \
    # ... continue with other packages ...
```

### Method 2: pip packages

For packages available via pip, install them in the `%post` section:

```bash
%post
    # ... after other installations ...
    
    # Install pip packages
    pip3 install --no-cache-dir numpy pandas matplotlib seaborn biopython scikit-learn
    
    # Or install from requirements file (if using a requirements.txt)
    # pip3 install --no-cache-dir -r /path/to/requirements.txt
```

### Method 3: Conda/Mamba environments

The container already includes Miniforge. You can create a dedicated environment for Python packages:

```bash
%post
    # ... after miniforge installation ...
    
    # Create a Python environment with specific packages
    mamba create -n python_analysis_env python=3.9 numpy pandas matplotlib biopython scikit-learn -y
    
    # Or install additional packages to the base environment
    mamba install numpy pandas matplotlib biopython scikit-learn -y
```

### Method 4: Installing from GitHub or custom sources

For packages not available in standard repositories:

```bash
%post
    # ... other installations ...
    
    # Install from GitHub
    pip3 install git+https://github.com/username/repository.git
    
    # Install from specific version/branch
    pip3 install git+https://github.com/username/repository.git@v1.0.0
```

## Best Practices

1. **Pin package versions** when possible to ensure reproducibility:
   ```bash
   pip3 install numpy==1.21.0 pandas==1.3.0
   ```

2. **Use `--no-cache-dir`** with pip to reduce container size:
   ```bash
   pip3 install --no-cache-dir package_name
   ```

3. **Group related packages** together in the same command to optimize build layers:
   ```bash
   pip3 install --no-cache-dir numpy pandas matplotlib seaborn
   ```

4. **Consider conda/mamba** for complex scientific packages with compiled dependencies:
   ```bash
   mamba install -c conda-forge -c bioconda package_name
   ```

## Example: Adding Common Data Science Packages

To add a comprehensive set of Python data science packages, add this to the `%post` section:

```bash
%post
    # ... existing installations ...
    
    # Install essential Python data science packages
    pip3 install --no-cache-dir \
        numpy==1.24.3 \
        pandas==2.0.3 \
        matplotlib==3.7.2 \
        seaborn==0.12.2 \
        scikit-learn==1.3.0 \
        biopython==1.81 \
        jupyter==1.0.0 \
        jupyterlab==4.0.5
        
    # Or use mamba for packages with complex dependencies
    mamba install -c conda-forge -c bioconda \
        plotly \
        bokeh \
        dask \
        xarray -y
```

# Building containers

Containers are built using a definition file. Once built, they exist as a single file. Since we're using [Apptainer](https://apptainer.org/docs/user/main/introduction.html) (formerly Singularity), the container files will have the `.sif` suffix. Currently, we use the script [`srlab-bioinformatics-build.sh`](https://github.com/RobertsLab/code/blob/master/apptainer_definition_files/srlab-bioinformatics-build.sh) (GitHub) to build the container directly on Klone. However, the container could be built on any computer running [Apptainer](https://apptainer.org/docs/user/main/introduction.html) (formerly Singularity), and the resulting file could be transferred to Klone. 

The build process must be initiated _manually_. If the definition file(s) is updated, then the user must remember to re-build the container, in order to incorporate the new changes!

# More Resources

- [Klone Conda Guide](./klone_Conda.md) - For installing and configuring conda/miniforge on Klone
- [UW Hyak Documentation](https://hyak.uw.edu/docs) is a great way to start using Hyak (Klone) by providing (relatively) easy to follow walkthrough of how to access Klone, what the different nodes are, examples of how to build containers, and more.