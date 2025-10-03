# Managing Home Directory Space on Klone

## Overview

The home directory on Klone has a strict 10GB storage limit. This space can quickly fill up with cache directories from various applications like VS Code, Cursor, Apptainer, and system caches. This guide shows you how to relocate these directories to group storage to free up home directory space.

## Common Space Consumers

The following directories commonly consume significant home directory space:

- `.cache` - General application cache (can grow to 3-4GB)
- `.local` - User-installed Python packages and application data (2-3GB)
- `.apptainer` - Apptainer/Singularity cache (1-2GB)
- `.vscode-server` - VS Code Remote Server files (1-2GB)
- `.cursor-server` - Cursor editor server files (1-2GB)

## Checking Home Directory Usage

Before making changes, check your current space usage:

```bash
# Check overall storage usage
hyakstorage

# Check what's using space in home directory
du -sh ~/*
du -sh ~/.*

# Detailed breakdown of hidden directories
du -h --max-depth=1 ~ | sort -hr | head -20
```

## Relocating Cache Directories

### 1. Moving General Cache (.cache)

The `.cache` directory stores temporary files for various applications. You can safely move this to group storage:

```bash
# Create cache directory in group storage
mkdir -p /gscratch/srlab/${USER}/.cache

# Move existing cache (if it exists)
if [ -d ~/.cache ]; then
    rsync -av ~/.cache/ /gscratch/srlab/${USER}/.cache/
    rm -rf ~/.cache
fi

# Create symbolic link
ln -s /gscratch/srlab/${USER}/.cache ~/.cache

# Verify the setup
ls -la ~/.cache
```

### 2. Moving VS Code Server (.vscode-server)

If you use VS Code Remote SSH to connect to Klone, it creates a `.vscode-server` directory:

```bash
# Create directory in group storage
mkdir -p /gscratch/srlab/${USER}/.vscode-server

# Move existing VS Code server files (if they exist)
if [ -d ~/.vscode-server ]; then
    rsync -av ~/.vscode-server/ /gscratch/srlab/${USER}/.vscode-server/
    rm -rf ~/.vscode-server
fi

# Create symbolic link
ln -s /gscratch/srlab/${USER}/.vscode-server ~/.vscode-server

# Verify the setup
ls -la ~/.vscode-server
```

### 3. Moving Cursor Server (.cursor-server)

If you use Cursor editor to connect to Klone:

```bash
# Create directory in group storage
mkdir -p /gscratch/srlab/${USER}/.cursor-server

# Move existing Cursor server files (if they exist)
if [ -d ~/.cursor-server ]; then
    rsync -av ~/.cursor-server/ /gscratch/srlab/${USER}/.cursor-server/
    rm -rf ~/.cursor-server
fi

# Create symbolic link
ln -s /gscratch/srlab/${USER}/.cursor-server ~/.cursor-server

# Verify the setup
ls -la ~/.cursor-server
```

### 4. Relocating Apptainer Cache (.apptainer)

Apptainer creates cache directories for container images. You can relocate these using environment variables:

```bash
# Create Apptainer cache directories in group storage
mkdir -p /gscratch/srlab/${USER}/apptainer/cache
mkdir -p /gscratch/srlab/${USER}/apptainer/tmp

# Add to ~/.bashrc
cat >> ~/.bashrc << 'EOF'

# Apptainer cache configuration
export APPTAINER_CACHEDIR=/gscratch/srlab/${USER}/apptainer/cache
export APPTAINER_TMPDIR=/gscratch/srlab/${USER}/apptainer/tmp
EOF

# Reload shell configuration
source ~/.bashrc

# Move existing cache (if it exists)
if [ -d ~/.apptainer ]; then
    rsync -av ~/.apptainer/ /gscratch/srlab/${USER}/apptainer/cache/
    rm -rf ~/.apptainer
fi

# Verify configuration
echo $APPTAINER_CACHEDIR
echo $APPTAINER_TMPDIR
```

### 5. Managing .local Directory

The `.local` directory contains user-installed packages and application data. Be careful when moving this:

```bash
# Create directory in group storage
mkdir -p /gscratch/srlab/${USER}/.local

# Move specific subdirectories that tend to be large
# Only move if they exist and are not critical system files

# Move pip cache
if [ -d ~/.local/share/pip ]; then
    mkdir -p /gscratch/srlab/${USER}/.local/share
    rsync -av ~/.local/share/pip/ /gscratch/srlab/${USER}/.local/share/pip/
    rm -rf ~/.local/share/pip
    ln -s /gscratch/srlab/${USER}/.local/share/pip ~/.local/share/pip
fi

# Move conda packages if stored here
if [ -d ~/.local/share/conda ]; then
    mkdir -p /gscratch/srlab/${USER}/.local/share
    rsync -av ~/.local/share/conda/ /gscratch/srlab/${USER}/.local/share/conda/
    rm -rf ~/.local/share/conda
    ln -s /gscratch/srlab/${USER}/.local/share/conda ~/.local/share/conda
fi
```

!!! warning
    Be careful with the `.local` directory. Some applications expect specific files to be in the home directory. Always test after moving to ensure applications still work correctly.

## Complete Setup Script

Here's a comprehensive script that relocates all common cache directories:

```bash
#!/bin/bash
# Script to relocate cache directories to group storage
# Save this as ~/setup_cache_relocation.sh and run: bash ~/setup_cache_relocation.sh

USER_GSCRATCH="/gscratch/srlab/${USER}"

echo "Setting up cache relocation to ${USER_GSCRATCH}"

# Function to safely relocate a directory
relocate_dir() {
    local source_dir=$1
    local target_dir=$2
    local link_name=$3
    
    echo "Processing ${link_name}..."
    
    # Create target directory
    mkdir -p "${target_dir}"
    
    # Move existing content if source exists
    if [ -d "${source_dir}" ] && [ ! -L "${source_dir}" ]; then
        echo "  Moving existing content..."
        rsync -av "${source_dir}/" "${target_dir}/"
        rm -rf "${source_dir}"
    elif [ -L "${source_dir}" ]; then
        echo "  Already a symlink, skipping..."
        return
    fi
    
    # Create symlink
    ln -s "${target_dir}" "${source_dir}"
    echo "  Created symlink: ${source_dir} -> ${target_dir}"
}

# Relocate cache directories
relocate_dir ~/.cache "${USER_GSCRATCH}/.cache" "General cache"
relocate_dir ~/.vscode-server "${USER_GSCRATCH}/.vscode-server" "VS Code Server"
relocate_dir ~/.cursor-server "${USER_GSCRATCH}/.cursor-server" "Cursor Server"

# Setup Apptainer environment variables
if ! grep -q "APPTAINER_CACHEDIR" ~/.bashrc; then
    echo "" >> ~/.bashrc
    echo "# Apptainer cache configuration" >> ~/.bashrc
    echo "export APPTAINER_CACHEDIR=/gscratch/srlab/\${USER}/apptainer/cache" >> ~/.bashrc
    echo "export APPTAINER_TMPDIR=/gscratch/srlab/\${USER}/apptainer/tmp" >> ~/.bashrc
    echo "Added Apptainer environment variables to ~/.bashrc"
fi

# Create Apptainer directories
mkdir -p "${USER_GSCRATCH}/apptainer/cache"
mkdir -p "${USER_GSCRATCH}/apptainer/tmp"

# Move existing Apptainer cache
if [ -d ~/.apptainer ]; then
    echo "Moving Apptainer cache..."
    rsync -av ~/.apptainer/ "${USER_GSCRATCH}/apptainer/cache/"
    rm -rf ~/.apptainer
fi

echo ""
echo "Setup complete! Please run: source ~/.bashrc"
echo "Then verify with: hyakstorage"
```

## Verification

After relocating directories, verify the setup:

```bash
# Check that symlinks are correct
ls -la ~ | grep -E '\->'

# Check storage usage
hyakstorage

# Verify environment variables
echo $APPTAINER_CACHEDIR
echo $APPTAINER_TMPDIR

# Test that applications still work
# - Try connecting with VS Code/Cursor
# - Run an Apptainer container
```

## Maintenance

### Regular Cleanup

Even with relocated caches, perform regular cleanup:

```bash
# Clean old cache files
find /gscratch/srlab/${USER}/.cache -type f -mtime +30 -delete

# Clean Apptainer cache
apptainer cache clean

# Remove unused VS Code server versions
# (Be careful - only remove old versions)
ls -lt /gscratch/srlab/${USER}/.vscode-server/bin/
```

### Monitoring

Regularly check your storage usage:

```bash
# Weekly or monthly checks
hyakstorage

# Detailed breakdown
du -sh /gscratch/srlab/${USER}/.* | sort -hr
```

## Troubleshooting

### Symlink Issues

If applications don't recognize symlinks:

```bash
# Check symlink
ls -la ~/.cache
readlink ~/.cache

# Recreate if broken
rm ~/.cache
ln -s /gscratch/srlab/${USER}/.cache ~/.cache
```

### Permission Errors

If you encounter permission issues:

```bash
# Fix permissions
chmod -R u+rwX /gscratch/srlab/${USER}/.cache
chmod -R u+rwX /gscratch/srlab/${USER}/.vscode-server
chmod -R u+rwX /gscratch/srlab/${USER}/.cursor-server
chmod -R u+rwX /gscratch/srlab/${USER}/apptainer
```

### Application Not Finding Files

If an application can't find files after relocation:

1. Check the symlink is correct: `ls -la ~/.<directory>`
2. Check the target directory exists and has content
3. Try restarting the application or reconnecting
4. Check application-specific configuration files

## See Also

- [Klone Data Storage and System Organization](klone_Data-Storage-and-System-Organization.md)
- [Klone Conda](klone_Conda.md) - Managing conda installations
- [Klone Installing Programs](klone_Installing-Programs.md)
