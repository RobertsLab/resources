There are 4 main types of Hyak nodes:

- Login

- Build

- Interactive

- Execute

Each has a different function and different levels of connectivity.

We're guaranteed one node allocation at any given time, some nodes count towards this allocation, some do not.

### Login Node

- Shell prompt looks like `[UWNetID@mox2 ~]$`
- The first node you encounter upon logging in.
- Access to this node type is user-specific (i.e. only you have access to your login node).
- For file transfers and manipulation.
- This node has internet connectivity.     
- <em>Not</em> for running programs, program compiling, or other time/compute power intensive tasks.  

### Build Node
- Enter Build node from Login node (specify time needed):

    - `srun -p build --time=h:mm:ss --mem=100G --pty /bin/bash`

- Shell prompt looks like `[UWNetID@nXXXX ~]$`. (```XXXX``` will actually be a number)
- For downloading and compiling software from external sources
- This node has internet connectivity
- <em>Not</em> for compute power intensive tasks.
- Access to this node type is granted to all users of the Hyak (mox) system across the entire university.
- A limited number of build nodes are available across all Hyak (mox) users, so there may be a wait to access a build node at times.
- When finished, exit a build node by typing ```exit``` and then press the ```Enter``` key.

### Interactive Node
- Shell prompt looks like `[UNetID@nXXXX ~]$`. (```XXXX``` will actually be a number)
- Enter Interactive node from Login node (specify time needed):
    - `srun -p srlab -A srlab --time=h:mm:ss --mem=100G --pty /bin/bash`

- For testing, short run/low power tasks, and experimentation
- Access to this node type is limited to the Roberts Lab group, but is limited to a single group member at one time.
- <em>Cannot use Execute node while Interactive node is in use.</em>
- <em>This node does not have internet connectivity.</em>
- <em>Not</em> for compute power or time intensive tasks. Has file size/number limits.
- When finished, exit an interactive node by typing ```exit``` and then press the ```Enter``` key.

### Execute Node
- [Runs computing jobs submitted via an ```sbatch``` script.](https://github.com/RobertsLab/hyak_mox/wiki/Running-a-Job)
- For execution of large tasks. The "heavy lifting" node.
- No shell prompt
- <em>This node does not have internet connectivity</em>
- Access to this node type is limited to the Roberts Lab group, but is limited to a single group member at one time.
- <em>Cannot use Interactive node while Execute node is in use.</em>
- Creates `slurm-job#.out` files in working directory specified in `sbatch` execution script. This contains all standard out output from the program. This can be monitored via `cat` or `tail` from a Login node.
- `top` and other task manager functions can only be accessed after `ssh`ing in to the node.
