### Hyak (klone) Storage Locations & Capacities
#### 1. User-specific storage
- Storage allocation: 10GB (or 256,000 files)
- Located on your login node (e.g. `/mmfs1/home/<UW_NetID>`)
- To see space and file utilization: `hyakstorage`
- For personal data, scripts, and other small files, or files you don't want potentially changed by others.
#### 2. Group-specific storage
- Storage allocation: 1.024TB (or 1,000,000 files)
- Located: `/gscratch/srlab/`
- Shared by all `srlab` members.
- To see space and file utilization: `hyakstorage`
#### 3. Temporary storage ("Scrubbed")
- Storage allocation: 200TB (or 200,000,000 files).
- Located: `/gscratch/scrubbed/<UW_NetID>`
- Shared by all Hyak (Klone) users.
- Files are _automatically deleted_ 30 days after creation.

---
### Suggested User Organization
You should be aware of storage limits above, but here is a suggestion of how to organize your files.

In our **group-specific storage** (`/gscratch/srlab/<UW_NetID>`) create clear subdirectories that any files that might be needed over the course of months or years and are not large in size.

Generally you will need to  use the **temporary storage**. Roughly >= 100GB of input or output would qualify for using this space. Of course this will always depend on our free space in **group-specific storage**. Just be aware of the 30 day limit in `/gscratch/scrubbed/`. 

An example of how Steven operates:

- For every job, he creates a directory (e.g. `/gscratch/scrubbed/sr320/020322-oly-snp`) and includes job shell script in this directory and write out to same directory. Once complete he transfers the directory via `rsync` to his personal directory on [Gannet](https://gannet.fish.washington.edu/seashell/).
