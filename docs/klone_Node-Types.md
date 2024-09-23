There are two types of Klone slices (i.e. nodes, computers, blades):

- Login

- Compute

Each has a different function and different levels of connectivity.

### Login Node

- Shell prompt looks like `[<UW_NetID>@klone-login03 ~]$`
- The first node you encounter upon logging in.
- Access to this node type is user-specific (i.e. only you have access to your login node).
- For file transfers and manipulation.
- This node has internet connectivity.     
- <em>Not</em> for running programs, program compiling, or other time/compute power intensive tasks.


### Compute Node
- [Runs computing jobs submitted via an `SLURM` script.](https://github.com/RobertsLab/hyak_mox/wiki/Running-a-Job) or in an [interactive session](https://github.com/RobertsLab/hyak_mox/wiki/Node-Types#interactive-node).
- For execution of large tasks. The "heavy lifting" node.
- This node has internet connectivity.
- Access to this node type is limited to the Roberts Lab group, but is limited to a single group member at one time.
- Cannot use interactively while node is in use.
- Creates `slurm-job#.out` files in working directory specified in `SLURM` execution script. This contains all standard out and error output from the program. This can be monitored via `cat` or `tail` from a Login node.
- `top` and other task manager functions can only be accessed after `ssh`ing in to the node.

#### Interactive Node

Starting an interactive node allows us to use the compute node directly from a terminal without the need to submit a job to the SLURM scheduler. Like the SLURM scheduler, you still need to specify the resources you want to use (i.e. RAM and CPU count), as well as the time you'd like to reserve those resources. _Unlike_ the SLURM scheduler, your session will hold the resources _until the end of the time requested_. The resources will _not_ be returned when your commands finish! Thus, please be sure to use the `exit` command once you have finished with your intended computing when using an interactive node. This will ensure that you don't accidentally hold the node's resources and prevent other lab members from accessing it.

Example command to start interactive node:

`srun -p compute -A srlab --time=02:00:00 --mem=50G --pty /bin/bash`

- `srun`: Command to start interactive node.

- `-p cpu-g2-mem2x`: Tells Hyak to use our partition, called `cpu-g2-mem2x`.

- `-A srlab`: Tells Hyak to use our account, called `srlab`.

- `--time=02:00:00`: Requests the resources reservation for 2hrs, 00mins, and 00secs.

- `--mem=50G`: Requests 50GB of RAM from our node.

- `--pty /bin/bash`: Tells Hyak to start a terminal session, using Bash.


#### Execute Node
