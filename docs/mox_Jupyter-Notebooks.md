These directions are taken from the Mox Hyak wiki found [here](https://wiki.cac.washington.edu/display/hyakusers/Mox_ipython_jupyter) Bolded parts need to be changed to fit user needs.

#### Use Jupyter Notebook
1. Login to Hyak (MOX).

2. Start an interactive node session via `srun -p srlab --time=`**`hh:mm:ss`**` --pty /bin/bash`

2. Load Anaconda 2 module via `module load anaconda2_4.3.1`:

3. Start Jupyter notebook without a browser and specified port `jupyter notebook --no-browser --port=8899`. Note the Token supplied by Jupyter Notebook, that will be required in the last step.

4. In another terminal window on your local desktop, type `ssh -N -f -L 127.0.0.1:8899:127.0.0.1:8899 `**`UNetID`**`@mox.hyak.uw.edu`

5. Log in to Hyak on a third terminal window, and once logged in, ssh in to the interactive node you opened at the beginning via `ssh -N -f -L 127.0.0.1:8899:127.0.0.1:8899 `**`n1234`**

6. In your local browser, navigate to [http://127.0.0.1:8899](http://127.0.0.1:8899) and use the token from Step 3 to log in.
