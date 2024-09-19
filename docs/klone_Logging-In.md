1. Open your favorite terminal
2. Type `ssh <YourUWNetID>@klone.hyak.uw.edu` (replace `<YourUWNetID>` with your own UW Net ID)
3. Input your UWNetID _password_
4. Approve the two-factor authentication.
5. You're logged in to a Login node for Hyak!

Example:

```
D-69-91-141-150:~ Sean$ ssh seanb80@mox.hyak.uw.edu
Password:
Enter passcode or select one of the following options:

 1. Duo Push to iOS (XXX-XXX-1239)
 2. Phone call to iOS (XXX-XXX-1239)

Duo passcode or option [1-2]: 1
Passcode or option (1-2): 1
Success. Logging you in...
     _    _                    _                 _
    | | _| | ___  _ __   ___  | |__  _   _  __ _| | __
    | |/ / |/ _ \| '_ \ / _ \ | '_ \| | | |/ _` | |/ /
    |   <| | (_) | | | |  __/ | | | | |_| | (_| |   <
    |_|\_\_|\___/|_| |_|\___| |_| |_|\__, |\__,_|_|\_\
                                     |___/

This login node is meant for interacting with the job scheduler and 
transferring data to and from KLONE. Please work by requesting an 
interactive session on (or submitting batch jobs to) compute nodes.

Visit the HYAK website for more documentation:
https://hyak.uw.edu/docs/

Questions? E-mail help@uw.edu with "hyak" in the subject.

Run "scontrol show res" to see any reservations in place that will 
prevent your jobs from running with the reason "ReqNodeNotAvail".


[seanb80@mox2 ~]$
```
