# Quick start guide to running a job on Klone

1. SSH into Klone:

- `ssh <username>@klone.hyak.uw.edu`

2. Create a SLURM script (e.g. `20240917-cgig-ncbi-blastx.sh`) with the following commands (these come after the SLURM header):

```bash
module load apptainer


apptainer exec \
--home $PWD \
--bind /mmfs1/home/ \
--bind /mmfs1/gscratch/ \
/gscratch/srlab/containers/srlab-bioinformatics-container-<git_commit_hash>.sif \
<program_name> <programs_arguments>
```

- You'll need to replace anything in `<>` (including the `<` and `>`) with your specific requirements.

3. Submit job to SLURM scheduler (i.e. start your job):

- `sbatch <slurm_script_name.sh>`

- You'll need to replace anything in `<>` (including the `<` and `>`) with your specific requirements.