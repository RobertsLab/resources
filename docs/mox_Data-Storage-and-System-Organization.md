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

In our **group-specific storage** (`/gscratch/srlab/your_uw_id`) create subdirectories:
- `jobs` where job scripts live. These could be named based on date. For example Steven uses `MMDD-HHMM.sh` format.
- `data` data you are acting on.
- `analyses` where output goes. Steven uses MMDD subdirectory naming structure. This is where he points to a working directory in job script header.
- `blastdb` where blast databases live.

If you have _a lot_ of data to analyze or your output will be _big_ (or thousands of files) you will need to use the **temporary storage**. Roughly 500GB of input or output would qualify for using this space. Of course this will always depend on our free space in **group-specific storage**. Just be aware of the 30 day limit. For this you could have two subdirectories in (`/gscratch/scrubbed/your_uw_id`)...
- `analyses` where output goes.
- `data` data you are acting on.

For both, Steven uses MMDD subdirectory structure.
