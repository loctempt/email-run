# mail-run
A simple utility that proxies command line instructions, time it, and send an e-mail to myself when the instruction finishes.

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
When the execution is finished, the designated receivers will get an e-mail just like below.
```plain text
command: 	"./main.py run > run.log"
starts at: 	Mon Mar 7 10:34:27 2022
ends at: 	Mon Mar 7 10:34:54 2022
running time: 	27.525151 sec.
timedelta: 	0:00:27.525151
```
