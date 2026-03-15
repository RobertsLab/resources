# Using Conda on Klone


## Overview

!!! warning
    As a best practice, please use our [bioinformatics container(s)](klone_Container-Documentation.md) for your Conda workflows instead of installing conda packages directly on Klone. Containers provide a consistent and reproducible environment, reducing dependency issues and simplifying software management.

Conda (including Miniforge, Miniconda, and Anaconda) is a popular package manager for Python and other languages. However, conda installations and environments can quickly consume significant disk space. This guide explains how to properly install and configure conda on Klone to avoid storage limitations.

## Storage Considerations

Klone has different storage locations with varying capacities:

- **Home directory** (`/mmfs1/home/<UW_NetID>`): Only 10GB - **NOT recommended for conda**
- **Group storage** (`/mmfs1/gscratch/srlab/<UW_NetID>`): 1.024TB shared - **Recommended for conda**
- **Temporary storage** (`/gscratch/scrubbed/<UW_NetID>`): 200TB but files deleted after 30 days

**Important**: Always install conda in group storage (`/mmfs1/gscratch/srlab/<UW_NetID>`) to avoid hitting the 10GB home directory limit.

## Fresh Conda Installation

### Step 1: Download Miniforge (Recommended)

```bash
# Navigate to your group storage directory
cd /mmfs1/gscratch/srlab/${USER}

# Download Miniforge (recommended over Anaconda for smaller size)
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
```

### Step 2: Install to Group Storage

```bash
# Run the installer
bash Miniforge3-Linux-x86_64.sh

# When prompted for installation location, specify:
# /mmfs1/gscratch/srlab/${USER}/miniforge3

# Answer "yes" when asked to initialize conda
```

### Step 3: Configure Your Shell

Add the following to your `~/.bashrc` file:

```bash
# Initialize conda from group storage location
eval "$(/mmfs1/gscratch/srlab/${USER}/miniforge3/bin/conda shell.bash hook)"
```

Then reload your shell:

```bash
source ~/.bashrc
```

## Moving Existing Conda Installation

If you already have conda installed in your home directory and are running out of space:

### Step 1: Check Current Installation

```bash
# Check where conda is currently installed
which conda
conda info --base

# Check current storage usage
hyakstorage
```

### Step 2: Create New Installation Location

```bash
# Create directory in group storage
mkdir -p /mmfs1/gscratch/srlab/${USER}
```

### Step 3: Move the Installation

```bash
# Stop any running conda processes
conda deactivate

# Move the entire conda installation
mv /mmfs1/home/${USER}/miniforge3 /mmfs1/gscratch/srlab/${USER}/

# Or if you have anaconda3:
# mv /mmfs1/home/${USER}/anaconda3 /mmfs1/gscratch/srlab/${USER}/
```

### Step 4: Update Shell Configuration

Edit your `~/.bashrc` file to remove the old conda initialization and add the new one:

```bash
# Remove or comment out old lines like:
# eval "$(/mmfs1/home/${USER}/miniforge3/bin/conda shell.bash hook)"

# Add new initialization:
eval "$(/mmfs1/gscratch/srlab/${USER}/miniforge3/bin/conda shell.bash hook)"
```

Reload your shell:

```bash
source ~/.bashrc
```

### Step 5: Verify the Move

```bash
# Check new location
which conda
conda info --base

# Check that environments are accessible
conda env list

# Verify storage usage improvement
hyakstorage
```

## Configuring Conda Environment Location

To ensure all conda environments are created in group storage:

### Method 1: Set Default Environment Directory

```bash
# Create conda configuration directory
mkdir -p ~/.conda

# Create/edit conda configuration file
cat > ~/.conda/condarc << EOF
envs_dirs:
  - /mmfs1/gscratch/srlab/${USER}/miniforge3/envs
  - /mmfs1/gscratch/srlab/${USER}/conda_envs
pkgs_dirs:
  - /mmfs1/gscratch/srlab/${USER}/miniforge3/pkgs
  - /mmfs1/gscratch/srlab/${USER}/conda_pkgs
EOF
```

### Method 2: Always Specify Environment Location

When creating environments, explicitly specify the location:

```bash
# Create environment in group storage
conda create --prefix /mmfs1/gscratch/srlab/${USER}/conda_envs/myenv_name package_name

# Activate environment
conda activate /mmfs1/gscratch/srlab/${USER}/conda_envs/myenv_name
```

## Best Practices

### Environment Management

- **Use descriptive names**: Name environments after projects or specific purposes
- **Create project-specific environments**: Avoid conflicts by keeping environments separate
- **Regular cleanup**: Remove unused environments to save space
- **Document dependencies**: Keep track of package requirements for reproducibility

### Space Management

```bash
# Check conda disk usage
du -sh /mmfs1/gscratch/srlab/${USER}/miniforge3

# Clean conda cache periodically
conda clean --all

# List environments and their sizes
conda env list
du -sh /mmfs1/gscratch/srlab/${USER}/miniforge3/envs/*
```

### Backup and Sharing

```bash
# Export environment for sharing/backup
conda env export --name myenv > environment.yml

# Recreate environment from file
conda env create --file environment.yml --prefix /mmfs1/gscratch/srlab/${USER}/conda_envs/myenv_restored
```

## Integration with SLURM Jobs

When using conda environments in SLURM jobs, ensure you activate the environment correctly:

```bash
#!/bin/bash
#SBATCH --job-name=my_conda_job
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --time=1:00:00

# Initialize conda
eval "$(/mmfs1/gscratch/srlab/${USER}/miniforge3/bin/conda shell.bash hook)"

# Activate your environment
conda activate /mmfs1/gscratch/srlab/${USER}/conda_envs/myenv_name

# Run your analysis
python my_script.py
```

## Troubleshooting

### Environment Not Found

If conda can't find your environments after moving:

```bash
# Check conda configuration
conda config --show envs_dirs

# List all environments with full paths
conda env list

# Manually specify environment path
conda activate /full/path/to/environment
```

### Permission Issues

If you encounter permission errors:

```bash
# Check directory permissions
ls -la /mmfs1/gscratch/srlab/${USER}/

# Fix permissions if needed
chmod -R u+rwX /mmfs1/gscratch/srlab/${USER}/miniforge3
```

### Storage Still Full

If home directory is still full after moving conda:

```bash
# Check what's using space
du -sh /mmfs1/home/${USER}/*
du -sh /mmfs1/home/${USER}/.*

# Common culprits to move to group storage:
# - .cache directory (see Managing Home Directory guide)
# - .vscode-server, .cursor-server (see Managing Home Directory guide)
# - .apptainer cache (see Managing Home Directory guide)
# - .nextflow directory
# - .sra cache
# - Large data files
# - Git repositories
```

For detailed instructions on relocating cache directories, see [Managing Home Directory Space](klone_Managing-Home-Directory.md).

## See Also

- [Klone Data Storage and System Organization](klone_Data-Storage-and-System-Organization.md)
- [Klone Installing Programs](klone_Installing-Programs.md)
- [Raven Conda Usage](raven_Conda.md) (for comparison)