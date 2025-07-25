# Usage of Conda on Raven

## Best Practices

- **Use Environments**: Always create a new Conda environment for each project or analysis to avoid dependency conflicts.
- **Environment Naming**: Use descriptive names for environments, such as `project_name_env`.

## Activating Conda

To activate the base (default) environment, run:

```bash
eval "$(/opt/anaconda/anaconda3/bin/conda shell.bash hook)"
```

This should change your shell prompt to look like this (it'll have your username instead of `sam`):

`(base) sam@raven:`

## Creating a New Environment
To create a new Conda environment, use the following command:

```bash
conda create -n myenv_name conda_package_name1 conda_package_name2
```