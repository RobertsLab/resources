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

Using RStudio via Apptainer containers allows you to run RStudio in an isolated environment and can be useful to switch between different computers (e.g. run stuff on Klone and then switch to Raven later).

### Launching RStudio from an Apptainer Container

1. SSH into Raven.
2. Start a `screen` session (optional, but recommended):

   ```bash
   screen -S rstudio_session
   ```

   This will allow you to close your SSH session without terminating RStudio.

3. Launch the RStudio Apptainer container with port forwarding:

   ```bash
   singularity exec \
  --bind /tmp:/tmp \
  --bind /home:/home \
  --bind ~/rstudio-server/var-lib:/var/lib/rstudio-server \
  --bind ~/rstudio-server/var-run:/var/run/rstudio-server \
  --bind ~/rstudio-server/tmp:/tmp/rstudio-server \
  </path/to/your/container>/srlab-R4.4-bioinformatics-container-4743580.sif \
  rserver --www-port 8788 --www-address 0.0.0.0 --server-user=$(whoami)
   ```
   Replace `</path/to/your/container>/` with the path to your RStudio Apptainer container file.

4. Open a web browser on your local machine and navigate to:
   [`http://raven.fish.washington.edu:8788`](http://raven.fish.washington.edu:8788)

   NOTE: You may be prompted with a security warning, since the site uses `http` instead of `https`. You can safely ignore this warning and proceed to the site.
   
5. Log in with your _Raven_ account credentials.