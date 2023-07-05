import smtplib
import logging
import os
import sys
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from utils.errormail import errorMail

def sendMail(filePath, fileName, datum, envConfig):

   # list for recipients
   emailRecipients = []
   errorRecipient = []

   # enviroment variables setup
   envRecipients = envConfig['EMAILRECIPIENTS']
   errorRecipient.append(envConfig['ERRORRECIPIENT'])
   envSender = envConfig['SENDER']
   envSMTP = envConfig['SMTP']

   # env list
   for email in envRecipients.split(","):
      emailRecipients.append(email)

   logging.basicConfig(filename=envConfig['LOGFILEPATH'], level=logging.INFO)

   sender = envSender
   recipients = emailRecipients

   message = MIMEMultipart()
 
   message['From'] = envSender
   message['To'] = ", ".join(recipients)
   message['Subject'] = f'Wolt törzs hiányzó tételek {datum}'
   xls = MIMEApplication(open(filePath, 'rb').read())
   xls.add_header('Content-Disposition', 'attachment', filename= fileName)
   message.attach(xls)

   try:
      smtpObj = smtplib.SMTP(envSMTP)
      smtpObj.sendmail(sender, recipients, message.as_string())
   except smtplib.SMTPException as err:
      errorMail(err, envConfig)
      logging.info(" " + datetime.now().strftime('%Y.%m.%d %H:%M:%S') + " Nem sikerült elküldeni a levelet hiba: " + f"{err}")

