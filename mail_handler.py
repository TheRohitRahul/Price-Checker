import smtplib
from config import TO_MAIL_ID, FROM_MAIL_ID, APP_PASSWORD

class GMail(object):
  def __init__(self):
    self.mail_client = smtplib.SMTP('smtp.gmail.com', 587)

  def send_mail(self, subject , body):
    self.mail_client.ehlo()
    self.mail_client.starttls()
    self.mail_client.ehlo()
    self.mail_client.login(FROM_MAIL_ID, APP_PASSWORD)

    mail = "Subject: {}\n\n{}".format(subject, body)
    
    self.mail_client.sendmail(FROM_MAIL_ID, TO_MAIL_ID, mail)
    
    return True
