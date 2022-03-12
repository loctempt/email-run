# mail-run
A simple utility that proxies command line instructions, time it, and intended to send an e-mail to yourself when the instruction finishes (**so you can have real-time notifications pushed to your mobile devices if you've got an e-mail client app**). 

This is useful when you are executing very heavy tasks on a remote server.

## Prerequisites
1. Python3 is installed on your computer;
1. You must have a valid public e-mail service account (e.g. Gmail, QQ mail etc.);
1. Make sure that SMTP is enabled (you can find SMTP switch on your mail-box's settings page).

## Usage 
1. Simply modify the CAPITALIZED variables at the topmost row of codes, so you can have your `mail-run` connects to your e-mail account;
1. cd to the repository, run `make install`;
1. Use `mail-run <any command>` to run anything you want, and you will receive an e-mail when it finishes.

If you are desperate to get rid of mail-run, `make uninstall` will do the dirty work for you, then you can delete the project folder, mail-run won't leave anything on your computer ;-).

## Sample
When the execution is finished, the designated receivers will get an e-mail just like below (in a "time -v" format).
```plain text
Command being timed: "ping baidu.com -c 4"
User time (seconds): 0.00
System time (seconds): 0.00
Percent of CPU this job got: 0%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:08.08
Average shared text size (kbytes): 0
Average unshared data size (kbytes): 0
Average stack size (kbytes): 0
Average total size (kbytes): 0
Maximum resident set size (kbytes): 2916
Average resident set size (kbytes): 0
Major (requiring I/O) page faults: 0
Minor (reclaiming a frame) page faults: 155
Voluntary context switches: 10
Involuntary context switches: 0
Swaps: 0
File system inputs: 0
File system outputs: 0
Socket messages sent: 0
Socket messages received: 0
Signals delivered: 0
Page size (bytes): 4096
Exit status: 0
```
