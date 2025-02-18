# Quick start guide to running a job on Klone

See the ["Running a job" instructions](./klone_Running-a-Job.md) for a more detailed description of how set up and run a job on Klone.

1. SSH into Klone:

- `ssh <UW_NetID>@klone.hyak.uw.edu`

    - You'll need to replace `<UW_NetID>` (including the `<` and `>`) with your UW NetID.

2. Create a SLURM script (e.g. `20240917-cgig-ncbi-blastx.sh`) with the following commands (these come after the [SLURM header](./klone_Running-a-Job.md)):

    ```bash
    module load apptainer


    apptainer exec \
    --home $PWD \
    --bind /mmfs1/home/ \
    --bind /mmfs1/gscratch/ \
    --bind /gscratch/ \
    /gscratch/srlab/containers/srlab-bioinformatics-container-<git_commit_hash>.sif \
    <commands-script.sh>
    ```

    - You'll need to replace anything in `<>` (including the `<` and `>`) with your specific requirements.
    - `<commands-script.sh>` is a Bash script containing all of the commands/programs you wan to run.

IMPORTANT: `<commands-script.sh>` needs to be executable!! Make sure to run `chmod +x <commands-script.sh>` to make it executable.

3. Submit job to SLURM scheduler (i.e. start your job):

    - `sbatch <slurm_script_name.sh>`

        - You'll need to replace anything in `<>` (including the `<` and `>`) with your specific requirements.

---

For more information, check out the following:

- Roberts Lab Klone guides:

    - [Using containers](./klone_containers.md)
    - [Storage on Klone](./klone_Data-Storage-and-System-Organization.md)
    - [Running a job on Klone](./klone_Running-a-Job.md)

- [UW Hyak Documentation](https://hyak.uw.edu/docs)
