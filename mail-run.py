#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
import subprocess
import time
import os
from uuid import uuid4
from datetime import timedelta
from functools import reduce


MAIL_HOST = "smtp.qq.com"
SMTP_PORT = 587
MAIL_SENDER = "somebody@qq.com"
MAIL_FROM = "mail-run notifier <%s>" % MAIL_SENDER
MAIL_LICENCE = "123456"
MAIL_RECEIVERS = ["somebody@gmail.com", "Jack@qq.com"]


def stripped_time_record_list(time_record_file_path) -> list:
    stripped = []
    with open(time_record_file_path) as trf:
        for line in trf:
            stripped.append(line.strip())
    return stripped


def make_mail_body(time_record_file_path):
    return "\n".join(stripped_time_record_list(time_record_file_path))


def main():
    target_cmd = reduce(lambda x, y: x + " " + y, sys.argv[1:])
    time_record_file_path = "/tmp/time-out-" + str(uuid4()) + ".tmp"
    execution_cmd = " ".join(["time -v -o ", time_record_file_path, target_cmd])
    completed = subprocess.run(execution_cmd, shell=True)

    exit_status = completed.returncode
    subject = "\"%s\"" % target_cmd + " ends with status %s." % exit_status

    message = MIMEText(make_mail_body(time_record_file_path), "plain", "utf-8")
    message['From'] = MAIL_FROM
    message['Subject'] = Header(subject, "utf-8")

    try:
        smtp = smtplib.SMTP()
        smtp.connect(MAIL_HOST, SMTP_PORT)
        smtp.login(MAIL_SENDER, MAIL_LICENCE)
        smtp.sendmail(MAIL_SENDER, MAIL_RECEIVERS, message.as_string())
        print("mail successfully sent.")
    except smtplib.SMTPException as e:
        print("unable to send mails.", e)
    finally:
        os.remove(time_record_file_path)


if __name__ == "__main__":
    main()
