# mail-run
A simple utility that proxies command line instructions, time it, and send an e-mail to myself when the instruction finishes.

## Prerequisites
1. You must have a valid public e-mail service account (e.g. Gmail, QQ mail etc.);
2. Make sure that SMTP is enabled (you can find SMTP switch on your mail-box's settings page)

## Usage 
1. Simply modify the CAPITALIZED variables at the topmost row of codes, so you can have your `mail-run` connects to your e-mail account;
2. Add execution permission to `mail-run.py` (`chmod u+x mail-run.py`);
3. Add `mail-run.py` to your PATH, or create a link to your environment's binary folder;
4. Use `mail-run <any command>` to run anything you want, and you will receive an e-mail when it finishes.

## Sample
When the execution is finished, the designated receivers will get an e-mail just like below.
```plain text
command: 	"./main.py run > run.log"
starts at: 	Mon Mar 7 10:34:27 2022
ends at: 	Mon Mar 7 10:34:54 2022
running time: 	27.525151 sec.
timedelta: 	0:00:27.525151
```
