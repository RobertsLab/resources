Warning: There is no rote method for this. As Hyak users, we do not have administrator access, so anything that uses a `sudo` prefix will not work. Furthermore, standard package mangers (e.g. `apt` or `yum`) are not available and cannot be installed. That means no `apt get` or anything nice like that. This tutorial can only offer the most cursory of guidance and lots of commiseration for your pain.

## Guidance for installing programs.

_All program installations should be performed with a Build node._

1. Transfer your program files on to Hyak. Make note of any dependencies your program may need including Python (which can be loaded via a module) or another program.

2. If your program installation has dependency installation as part of the install script, you will need to use a build node for installation and compiling, otherwise an interactive node will be adequate.

3. Due to space limitations, and our desire to share with the rest of the lab, all programs should be installed here:

  `/gscratch/srlab/programs`.

4. Unzip the program files.

5. Begin installation. Most software packages include a `README` text file that explains the installation procedure. There is a lot of trial and error in this step, and you'll get very good at reading and Googling error messages, StackExchange will be your friend. An example of the process involved can be found [here](https://genefish.wordpress.com/2017/04/07/hyak-and-you-pt-2-github-and-pitchfork/)

## General Tips

- Add `cmake` to your system `$PATH` by adding the following to your `~/.bashrc` file:

  ```bash
  # Append cmake to beginning of PATH (primarily for Trinity 2.8 install)
  export PATH="/gscratch/srlab/programs/cmake-3.12.1/bin:$PATH"
  ```

## (Ana) conda packages:

1. Activate the default (base) conda environment:

  ```shell
  /gscratch/srlab/programs/anaconda3/condabin/conda activate
  ```

2. Install your desired package (replace `<package>` with your package name):

- `conda install <package>`

3. Deactivate the conda environment:

- `conda deactivate`

4. The program should now be available in this directory:

- `/gscratch/srlab/programs/anaconda3/bin/<program_name>`


## Installing R Packages

This is a guide to change the default R library install location to avoid running into space limits in the default home directory. After following the instructions below, all package installations should be performed on a build node.

1. Make a designated directory for your R packages, e.g.:

  `mkdir --parents /gscratch/srlab/${USER}/R_libs`

2. Create an `.Renviron` file in your home directory, defining the `R_USER_LIB` location established in Step 1:

  ```shell
  echo "# Set local library installation path
  R_LIBS_USER=/gscratch/srlab/${USER}/R_libs" > ~/.Renviron
  ```

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
