# VS Code on Klone via ProxyJump

## Overview

1. Provides a method to connect VS Code to a compute node on Klone, preserving the login nodes for the community. As a reminder, users running processes on the login node is prohibited.
2. Runs VS Code on your local computer, but runs background processes on Klone. A local copy of VS Code is required.
3. Requires: configuration files to be set up on your local computer, key-pair configuration, launching an interactive job, use of the Remote-SSH extension to connect to a compute node on klone.

## Initial set up

- Follow UW-IT guide here: [https://hyak.uw.edu/docs/tools/vsc-proxy-jump/](https://hyak.uw.edu/docs/tools/vsc-proxy-jump/)
- An alternative way to using VS code on Klone is through Hyak OnDemand: [https://hyak.uw.edu/docs/ood/vscode](https://hyak.uw.edu/docs/ood/vscode).
   - Pros: easier to get started
   - Cons: extensions like GitHub Co-pilot are not freely available or accessible 

## Running VS code after set up

1. Login to Klone through terminal
2. Start screen session
	- `screen -S vscode` 
3. Request compute node: 
	- partitions you can use include those you have access to when you run the command `hyakalloc` on Klone.
  - Examples
     - Using `srlab` partition: `salloc --partition=cpu-g2-mem2x --cpus-per-task=1 --mem=16G --job-name=vsc-proxy-jump	--time=24:00:00`
     - Using `coenv` partition: `salloc —-account coenv —-partition cpu-g2 -—cpus-per-task 1 --mem=50GB --time=24:00:00 --job-name=vsc-proxy-jump`
     - Using `ckpt` partition: `salloc --partition=ckpt --cpus-per-task=1 --mem=100G --job-name=vsc-proxy-jump`
4. Detach from screen:
  - `ctrl + A + D`
	- Before you do this, you may need to note or copy the node name (e.g. `n3441`) for the next step. If you'll use set-hyak-node.sh in the next step, you do not need to note it.
5. Set the node in your local `.ssh/klone-node-config file`
	- This is described in the UW-IT documentation: [https://hyak.uw.edu/docs/tools/vsc-proxy-jump/](https://hyak.uw.edu/docs/tools/vsc-proxy-jump/)
  - you can do this through your command line text editor (e.g. nano, vim). You’ll paste the node name after the `Hostname` field
	- Alternatively you can use the `Run set-hyak-node.sh` script 
	   - `bash set-hyak-node.sh`
6. Open VS Code and run Remove-SSH Connect to Server
  - type `fn + F1` then in the top bar type Remote-SSH: Connect to Server and select Klone-node.
     - If you don't see the function pop up in the bar, you may need to install the extention Remote-SSH.
     - If prompted about fingerprinting select continue.
     - If you are still having difficulty connecting, one hack is to log in to Klone through the terminal and delete the `.vscode-server` directory (`rm -r .vscode-server`). It is possible that it did not fully download when you initially tried to connect and this causes failure to connect. 

You should now be connected and the bottom left corner of the VS Code window should show `SSH: klone-node`. You should be able to navigate to the gscratch/scrubbed space and into your directory through the explorer. You can open a GitHub co-pilot chat and use the agent to help with some analysis. 

## Still struggling?

This is complicated and you don’t have to struggle alone. Create a [GitHub issue](https://github.com/RobertsLab/resources/issues), contact UW-IT (help@uw.edu), and/or go to [UW-IT office hours](https://calendar.washington.edu/sea_uwit-rc)
