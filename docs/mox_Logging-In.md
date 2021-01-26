1. Open your favorite terminal
2. Type `ssh YourUWNetID@mox.hyak.uw.edu`
3. Input your UWNetID password
4. If you're signed up for 2-factor authentication via Duo, open your smart phone and approve the connection, if you're using an Entrust fob, activate it and type the number in.
5. You're logged in to a Login node for Hyak!

Example:

```
D-69-91-141-150:~ Sean$ ssh seanb80@mox.hyak.uw.edu
Password: 
Enter passcode or select one of the following options:

 1. Duo Push to iOS (XXX-XXX-1239)
 2. Phone call to iOS (XXX-XXX-1239)

Duo passcode or option [1-2]: 1
Last login: Thu Jun  8 14:59:10 2017 from d-173-250-161-130.dhcp4.washington.edu

     ** NOTICE **
     Users need to do all their interactive work, including compiling and 
     building software, on the compute nodes (n####) and NOT on the
     head/login node (hyak.washington.edu). The login nodes are for
     interacting with the scheduler and transferring data to and from the
     system.

     Please visit the Hyak User Wiki for more details
     http://wiki.hyak.uw.edu


[seanb80@mox2 ~]$ 
```