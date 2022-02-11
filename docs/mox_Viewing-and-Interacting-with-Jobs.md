### Viewing Jobs:

There are two main commands to view job statuses. `squeue` and `scontrol`. `squeue` shows information about all jobs currently running on Hyak, while `scontrol` shows information on a specific job, and requires additional arguments

`squeue` - 

Typing `squeue` in any node type of Hyak shows the following output

```
[seanb80@mox1 CanuTest]$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             24074     build   my_job    dsale PD       0:00      1 (QOSMaxCpuPerUserLimit)
             24355     build   my_job    dsale PD       0:00      1 (Priority)
             32589      chem dft_dime  inguyen PD       0:00      2 (Resources)
             32590      chem dft_dime  inguyen PD       0:00      2 (Resources)
             32591      chem dft_dime  inguyen PD       0:00      2 (Resources)
             32592      chem dft_dime  inguyen PD       0:00      2 (Resources)
             32594      chem dft_dime  inguyen PD       0:00      2 (Resources)
             32595      chem dft_dime  inguyen PD       0:00      2 (Resources)
             32628      chem Modello_     gd24 PD       0:00      1 (Resources)
             32770    ilahie  R5local   vanouk PD       0:00     18 (Resources)
             32765       stf R5global   vanouk PD       0:00     11 (Resources)
             32776  ferrante     bash      af0  R      14:38      1 n2013
             32103      choe NPc_f2_5    ychoe  R 4-10:43:42      1 n2179
             32482      choe NPex_dn2    ychoe  R   22:14:20      1 n2012
             32481      choe  NPex_dn    ychoe  R   22:14:51      1 n2195
             32192      chem EXC-DMC-    lrm13  R 2-18:29:37      1 n2014
             32588      chem dft_dime  inguyen  R    3:34:51      2 n[2024-2025]
             32619      chem dft_snap   yliu92  R   17:08:07      1 n2201
             32618      chem dft_snap   yliu92  R   17:21:38      1 n2005
             32769    ilahie   R5orig   vanouk  R      57:21     18 n[2156-2173]
             32494      chem prova2_E     gd24  R   17:56:09      1 n2180
             32504      chem prova2_E     gd24  R   17:56:09      1 n2184
             ...
```

This shows the JobID (important for `scontrol`), the group who owns the JobID, the job name, time remaining, number of nodes used, and node IDs (important for `ssh`ing in to view process information). The output can be piped in to grep to identify individual groups via `squeue | grep "srlab"` for ease of finding relevant information.

```
[seanb80@n2149 CanuTest]$ squeue | grep "srlab"
             32779     srlab     bash  seanb80  R       0:09      1 n2149
```

`scontrol` - 

`scontrol` shows more in depth information regarding a specific job and node. 

Job information: `scontrol show job JobID` returns state, run time, time limit, and node architecture information. The output below shows that our job has been running for 00:14:55, (RunTime), has a total TimeLimit of 00:30:00 and is running on a 28 core node (NumCPUs) with 28gb of memory (mem). 

```
[seanb80@n2149 CanuTest]$ scontrol show job 32779
JobId=32779 JobName=bash
   UserId=seanb80(557445) GroupId=hyak-srlab(415510) MCS_label=N/A
   Priority=100 Nice=0 Account=srlab QOS=normal
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=1 Restarts=0 BatchFlag=0 Reboot=0 ExitCode=0:0
   RunTime=00:14:55 TimeLimit=00:30:00 TimeMin=N/A
   SubmitTime=2017-06-21T07:32:33 EligibleTime=2017-06-21T07:32:33
   StartTime=2017-06-21T07:32:33 EndTime=2017-06-21T08:02:33 Deadline=N/A
   PreemptTime=None SuspendTime=None SecsPreSuspend=0
   Partition=srlab AllocNode:Sid=mox1:15953
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=n2149
   BatchHost=n2149
   NumNodes=1 NumCPUs=28 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   TRES=cpu=28,mem=28G,node=1
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=1 MinMemoryCPU=1G MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   Gres=(null) Reservation=(null)
   OverSubscribe=NO Contiguous=0 Licenses=(null) Network=(null)
   Command=/bin/bash
   WorkDir=/gscratch/srlab/data/CanuTest
   Power=
```

---
### View CPU and Memory Loads on Node

There are two ways to see activity. Using `sstat` [the Slurm Workload Manager](https://slurm.schedmd.com/sstat.html) or `top`. 

For either I suggest starting to find details of your job:
```
[sr320@mox2 ~]$ squeue | grep srlab
            130588     srlab supernov    sr320  R 2-08:29:31      1 n2211
```

Then using the job ID 

```
[sr320@mox2 ~]$ sstat -j 130588.batch 
       JobID  MaxVMSize  MaxVMSizeNode  MaxVMSizeTask  AveVMSize     MaxRSS MaxRSSNode MaxRSSTask     AveRSS MaxPages MaxPagesNode   MaxPagesTask   AvePages     MinCPU MinCPUNode MinCPUTask     AveCPU   NTasks AveCPUFreq ReqCPUFreqMin ReqCPUFreqMax ReqCPUFreqGov ConsumedEnergy  MaxDiskRead MaxDiskReadNode MaxDiskReadTask  AveDiskRead MaxDiskWrite MaxDiskWriteNode MaxDiskWriteTask AveDiskWrite 
------------ ---------- -------------- -------------- ---------- ---------- ---------- ---------- ---------- -------- ------------ -------------- ---------- ---------- ---------- ---------- ---------- -------- ---------- ------------- ------------- ------------- -------------- ------------ --------------- --------------- ------------ ------------ ---------------- ---------------- ------------ 
130588.batch 378173576K          n2211              0 255186652K 297379616K      n2211          0 188699776K        0        n2211              0          0 6-21:36:24      n2211          0 1-12:27:15        1     27.00M       Unknown       Unknown       Unknown              0 75974159.15M           n2211               0 75974159.15M  3421658.12M            n2211                0  3421658.12M 
[sr320@mox2 ~]$ 
```
Yes it is ugly and for the most part not valuable.

You could trim down, 

```
[sr320@mox2 ~]$ sstat --format=AveCPU,AveCPUFreq,ReqCPUFreq,MaxVMSize,AveVMSize,MinCPU,NTasks,MaxRSSNode -j 130588.batch 
    AveCPU AveCPUFreq ReqCPUFreq  MaxVMSize  AveVMSize     MinCPU   NTasks MaxRSSNode 
---------- ---------- ---------- ---------- ---------- ---------- -------- ---------- 
1-13:07:49     14.99M    Unknown 378173576K 255188704K 6-21:36:24        1      n2211 
```

Now for what works! 

Using the node ID from above.

```
ssh -t n2211 top
```
<img src='https://d.pr/i/EtjyAv+'>


But you can simplify

```
ssh -t n2211 top -u sr320 | grep 8742
```

_Just remember to Control 'C' when you are done as this program is running on the node._ 



---
### Memory only

`free`
```
[sr320@mox1 jobs]$ ssh -t n2221 free -g
              total        used        free      shared  buff/cache   available
Mem:            251           6         241           2           3         241
Swap:            11           0          11
```


---

### Cancelling jobs:

Canceling jobs is done via the `scancel JobID` command. It cancels any job you have ownership of with a 12 second graceful shutdown period, so be sure you're canceling the right job when you execute it.

```
[seanb80@n2149 CanuTest]$ scancel 32779
srun: Force Terminated job 32779
[seanb80@n2149 CanuTest]$ srun: Job step aborted: Waiting up to 12 seconds for job step to finish.
srun: error: n2149: task 0: Killed
[seanb80@mox1 CanuTest]$ 
```

