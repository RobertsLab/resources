Warning: There is no rote method for this. As Hyak users, we do not have administrator access, so anything that uses a `sudo` prefix, such as `pip`, will not work. Furthermore, Hyak is built on CentOS, as opposed to Debian, so the `apt` package manager does not exist. That means no `apt get` or anything nice like that. This tutorial can only offer the most cursory of guidance and lots of commiseration for your pain.

Guidance for installing programs.

1. Using either a Login or Build node, transfer your program files on to Hyak. Make note of any dependencies your program may need including Python (which can be loaded via a module) or another program.

2. If your program installation has dependency installation as part of the install script, you will need to use a build node for installation and compiling, otherwise an interactive node will be adequate.

3. Decide where you're going to have your program install, either `/gscratch/srlab/` or your Home directory.

4. Unzip the program files in to your chosen installation location.

5. Begin installation. There is a lot of trial and error in this step, and you'll get very good at reading and Googling error messages, StackExchange will be your friend. An example of the process involved can be found [here](https://genefish.wordpress.com/2017/04/07/hyak-and-you-pt-2-github-and-pitchfork/)

Some Tips:

For Python packages, `pip install --user` isn't the greatest answer when using the `module load anaconda*` option as it seems to view the user's location as the module's location as opposed to the actual user directory. Instead use `easy_install --install-dir /gscratch/srlab/install/dir packagename==version`. This seems to work much better.


### Installing R Packages

This is a guide to change the default R library install location to avoid running into space limits in the default home directory. After following the instructions below, all package installatios should be performed on a build node.

1. Make a designated directory for your R packages, e.g.:

  `mkdir --parents /gscratch/srlab/${USER}/R_libs`

2. Create an `.Renviron` file in your home directory, defining the `R_USER_LIB` location established in Step 1:

  `echo "# Set local library installation path
R_LIBS_USER=/gscratch/srlab/${USER}/R_libs" > ~/.Renviron`

3. Confirm success:

  ```shell
  # Start R
  /gscratch/srlab/programs/R-3.6.2/bin/R
  ```

  ```R
  # Check library paths
  .libPaths()
  ```

  - The output should look something like this:

    ```R
    [1] "/gscratch/srlab/sam/R_libs"          
    [2] "/gscratch/srlab/programs/R-3.6.2/library"
    ```
