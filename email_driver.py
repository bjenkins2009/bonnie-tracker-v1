import smtplib
import os

import settings

SENT_FROM = "bonnie.bear2021@gmail.com"

def email_message(to="", msg=""):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(os.getenv('gmail_user'), os.getenv('gmail_password'))
    server.sendmail(SENT_FROM, to, msg)
    server.close()
