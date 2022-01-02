import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings

import random
#https://github.com/WISEPLAT/python-code/blob/master/python-email/main.py

def send_mail(recipients,code):
    print(recipients)
    print(code)

    sender = 'gfake6388@gmail.com'
    subject = 'Код для аунтификации'
    text = 'Ваш код: '+code
    html = '<html><head></head><body><p>' + text + '</p></body></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Рейтинг бот'
    msg['To'] = recipients
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/'

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)
    
    mail = smtplib.SMTP_SSL('imap.gmail.com')
    mail.login('@gmail.com', '')
    #https://www.google.com/settings/security/lesssecureapps
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
