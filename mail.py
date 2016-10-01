#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib  import SMTP_SSL


login, password = 'mail@gmail.com', getpass('Gmail Password:')
recipients = ['mail@gmail.com']

# create message
msg = MIMEText('message body…', 'plain', 'utf-8')
msg['Subject'] = Header('subject…', 'utf-8')
msg['From'] = login
msg['To'] = ", ".join(recipients)

# send it via gmail
s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
s.set_debuglevel(1)
try:
    s.login(login, password)
    s.sendmail(msg['From'], recipients, msg.as_string())
finally:
    s.quit()