#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
import subprocess
import time
from datetime import timedelta
from functools import reduce

MAIL_HOST = "smtp.qq.com"
MAIL_SENDER = "somebody@qq.com"
MAIL_LICENCE = "123456"
MAIL_RECEIVERS = ["somebody@gmail.com", "Jack@qq.com"]

cmd_str = reduce(lambda x, y: x + " " + y, sys.argv[1:])
target_program = cmd_str.split()[0]
start_time = time.time()
ret = subprocess.run(cmd_str, shell=True)

# Setting subject.
if ret.returncode == 0:
    subject = "process [%s] " % target_program + "ends normally."
else:
    subject = "process [%s] " % target_program + "ends with an error, return code: %d" % ret.returncode

# Setting running time.
end_time = time.time()
running_time = end_time - start_time

html_msg = """<!DOCTYPE html>
<html>
<head>
<style>
* {
          font-family: "Lucida Console", "Courier New", monospace;
          }


.thick {
          font-weight: bold;
          }

</style>
</head>
<body>
<table>
<tr>
  <td><span class="thick">command:</span></td>""" +\
"  <td>\"%s\"\n</td>" % " ".join(sys.argv[1:]) +\
"""</tr>
<tr>
  <td><span class="thick">starts at:</span></td>""" +\
"  <td>%s\n</td>" % time.ctime(start_time) +\
"""</tr>
<tr>
  <td><span class="thick">ends at:</span></td>""" +\
"  <td>%s\n</td>" % time.ctime(end_time) +\
"""</tr>
<tr>
  <td><span class="thick">running time:</span></td>""" +\
"  <td>%f sec.\n</td>" % running_time  +\
"""</tr>
<tr>
  <td><span class="thick">timedelta:</span></td>""" +\
"  <td>%s</td>" % timedelta(seconds=running_time) +\
"""</tr>
</table>
</body>
</html>"""

message = MIMEText(html_msg, "html", "utf-8")
message['From'] = "mail-run notifier <jxy1996@qq.com>"
message['To'] = "jxy"
message['Subject'] = Header(subject, "utf-8")

try:
    smtp = smtplib.SMTP()
    smtp.connect(MAIL_HOST, 587)
    smtp.login(MAIL_SENDER, MAIL_LICENCE)
    smtp.sendmail(MAIL_SENDER, MAIL_RECEIVERS, message.as_string())
    print("mail successfully sent.")
except smtplib.SMTPException as e:
    print("unable to send mails.", e)
