These directions are taken from the Mox Hyak wiki found [here](https://wiki.cac.washington.edu/display/hyakusers/Mox_ipython_jupyter) Bolded parts need to be changed to fit user needs.

#### Use Jupyter Notebook

1. Login to Hyak (MOX).

2. Start an interactive node session via `srun -p srlab -A srlab --time=hh:mm:ss --pty /bin/bash`

  - Replace the `--time=hh:mm:ss` with desired runtime. E.g. `--time=02:00:00` will set a runtime of 2hrs, 0mins, and 0secs.

3. Activate Anaconda 3: `conda activate`

4. Navigate to your desired working directory (e.g. `cd /gscratch/srlab/` or `/gscratch/scrubbed/`).

5. Start Jupyter Lab `jupyter-lab --no-browser --port 9000 --ip 0.0.0.0`.

  - Make note of the NODE_NUMBER assigned to you (it will frequently be different each time you run this process) - highlighted in the screencap below:

  ![Screencap of example showing Jupyter Notebook startup on Mox, with NODE NUMBER, Mox hostname, and activated port number highlighted in white box](https://github.com/RobertsLab/resources/blob/master/img/mox-jupyter_lab-node_and_port.png?raw=true)

6. In another terminal window on your local desktop, type `ssh <UW_NetID>@mox.hyak.uw.edu -L 9000:<NODE_NUMBER>.hyak.local:9000`

  - Replace `<UW_NetID>` (including the `<>`) with your UW NetID.

  - Replace `<NODE_NUMBER>` (including the `<>`) with the node assigned to you in Step 3.

7. In your local web browser, paste the lengthy URL provided in Step 3.

