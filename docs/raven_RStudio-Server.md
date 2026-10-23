# Using RStudio Server on Raven


There are two main ways to use RStudio on Raven:

1. Use a web browser to access RStudio Server, which is installed and running on Raven. This allows you to use RStudio's IDE through your web browser without needing to install anything on your local machine.

2. Use one of our Apptainer (Singularity) containers that have RStudio installed.


IMPORTANT: If you're off-campus, you'll need to activate the [Husky OnNet VPN](https://uwconnect.uw.edu/it?id=kb_article_view&sysparm_article=KB0034243) (UW guide) to access Raven!

## 1. Accessing RStudio Server on Raven


Point your web browser to the following URL to access RStudio Server on Raven:

[http://raven.fish.washington.edu:8787](http://raven.fish.washington.edu:8787)

NOTE: You may be prompted with a security warning, since the site uses `http` instead of `https`. You can safely ignore this warning and proceed to the site.


### Logging In

Log in with your _Raven_ account credentials.

## 2. Using RStudio via Apptainer Containers

Most people should just use the built-in RStudio Server above. Use a container when you need a specific R version or package set, or want the same environment you use on Klone.

### Available containers

Shared lab containers on Raven are in `/home/shared/containers`. To see what's there:

```bash
ls -lt /home/shared/containers
```

### Launching RStudio from a container

1. SSH into Raven.

2. Start a `screen` session so RStudio keeps running after you disconnect:

    ```bash
    screen -S rstudio
    ```

3. Download the launch script (first time only):

    ```bash
    curl -O https://raw.githubusercontent.com/RobertsLab/resources/master/scripts/raven-rstudio.sh
    ```

4. Run it:

    ```bash
    bash raven-rstudio.sh
    ```

    By default this uses the newest container in `/home/shared/containers`. To use a specific container, give its path:

    ```bash
    bash raven-rstudio.sh /home/shared/containers/<container_name>.sif
    ```

5. The script prints a URL (e.g. `http://raven.fish.washington.edu:41234`), your username, and a one-time password. Open the URL in your browser and log in with those.

    NOTE: You may be prompted with a security warning, since the site uses `http` instead of `https`. You can safely ignore this warning and proceed to the site.

6. Detach from `screen` with `Ctrl-a d`. Reattach later with `screen -r rstudio`.

### Stopping RStudio

Reattach (`screen -r rstudio`), press `Ctrl-C`, then type `exit` to close the screen session.

### What the script does

[`raven-rstudio.sh`](https://github.com/RobertsLab/resources/blob/master/scripts/raven-rstudio.sh) creates private temporary directories (so multiple users don't collide), picks an unused port, generates a password, and starts `rserver` inside the container with `singularity` (or `apptainer` if `singularity` isn't installed). See [Klone containers](klone_containers.md) for how lab containers are built.
