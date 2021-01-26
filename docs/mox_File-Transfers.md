## `rsync`
### Transferring data to/from Mox (Hyak) with `rsync`

`rsync` is a file transfer program. It copies specified files/folders from one location to another. Additionally, it verifies data integrity after the files have been transferred. This feature is critical, due to the large file sizes we frequently work with.

#### Copy files to Mox:

- ```rsync --archive --progress --verbose /path/to/file username@mox_IP:/path/to/mox/directory```

#### Copy entire folder to Mox (it is important to make sure there is _no_ ```/``` at the end of the remote path):

Navigate to the directory immediately above the one which you are interested in copying and then run the following command):

- ```rsync --archive --progress --verbose --relative ./directory username@mox_IP:/path/to/mox/directory```


#### Copy files from Mox:

- ```rsync --archive --progress --verbose username@mox_IP:/path/to/mox/file /path/to/local/directory```


---

## `sftp`

- `sftp -oPort=#### user42@my.server.edu`  once in commands include `ls`, `cd`, `get -r *` etc. Note port only needs be set not default (21).

