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
