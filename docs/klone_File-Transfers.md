## `rsync`
### Transferring data to/from Klone (Hyak) with `rsync`

`rsync` is a file transfer program and is the recommended file transfer program for Roberts Lab member. It copies specified files/folders from one location to another. Importantly, it verifies data integrity after the files have been transferred. This feature is critical, due to the large file sizes we frequently work with.

#### Copy files to Klone:

```bash
rsync --archive --progress --verbose /path/to/file/on/your/computer/file.txt <UW_NetID>@klone.hyak.uw.edu:/gscratch/scrubbed/<UW_NetID>/directory
```

#### Copy entire folder to Klone (it is important to make sure there is _no_ `/` at the end of the remote path):

Navigate to the directory immediately above the one which you are interested in copying and then run the following command):

```bash
rsync --archive --progress --verbose --relative ./directory <UW_NetID>@klone.hyak.uw.edu:/gscratch/scrubbed/<UW_NetID>/directory
```


#### Copy files from Klone:

```bash
rsync --archive --progress --verbose <UW_NetID>@klone.hyak.uw.edu:/gscratch/scrubbed/<UW_NetID>/file.txt /path/to/local/directory
```

