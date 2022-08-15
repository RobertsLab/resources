### Hyak (mox) Storage Locations & Capacities
#### 1. User-specific storage
- Storage allocation: 10GB (or 250,000 files)
- Located on your login node (e.g. ```/usr/lusers/UWnetID```)
- To see space and file utilization: `mmlsquota gscratch:home --block-size G`
- For personal data, scripts, and other small files, or files you don't want potentially changed by others.
#### 2. Group-specific storage
- Storage allocation: 5500GB (or 2,475,000 files)
- Located: ```/gscratch/srlab/```
- Shared by all srlab members
- To see space and file utilization: `mmlsquota -j srlab gscratch --block-size G`
#### 3. Temporary storage
- Storage allocation: 200TB (or 200,000,000 files).
- Located: ```/gscratch/scrubbed/```
- Shared by all Hyak (mox) users.
- Files are automatically deleted 30 days after creation.
- To see space and file utilization: `mmlsquota -j scrubbed gscratch --block-size G`

---
### Suggested User Organization
You should be aware of storage limits above, but here is a suggestion of how to organize your files.

In our **group-specific storage** (`/gscratch/srlab/your_uw_id`) create clear subdirectories that any files that might be needed over the course of months or years and are not large in size.

Generally you will need to  use the **temporary storage**. Roughly 500GB of input or output would qualify for using this space. Of course this will always depend on our free space in **group-specific storage**. Just be aware of the 30 day limit. 

And example of how Steven operates is that for every job he creates a directory in slurm (eg 020322-oly-snp) and includes job shell script in this directory and write out to said directory. Once complete you would rsync to your personal directory on one of birds (eg gannet).
