import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import logging

def errorMail(err, envConfig):
   logging.basicConfig(filename=envConfig['LOGFILEPATH'], level=logging.INFO)

   errorRecipient = []

   errorRecipient.append(envConfig['RECIPIENT'])
   errorRecipientSTR = envConfig['RECIPIENT']
   envSender = envConfig['SENDER']
   envSMTP = envConfig['SMTP']

   sender = envSender
   recipients = errorRecipient

   message = MIMEText( f"Hiba - ellenőrizd a logot: \n {err}")

   message['From'] = envSender
   message['To'] = errorRecipientSTR
   message['Subject'] = 'Wolt - FB hiba'

   try:
      smtpObj = smtplib.SMTP(envSMTP)
      smtpObj.sendmail(sender, recipients, message.as_string())
   except smtplib.SMTPException as e:
      logging.info(" " + datetime.now().strftime('%Y.%m.%d %H:%M:%S') + " cannot send email: " + f"{e}")
