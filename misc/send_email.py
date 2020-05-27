import logging
import smtplib
import time

from email.message import EmailMessage

LOGGER = logging.getLogger(__name__)


def email_ims(user, password, sender, to, smtp_server):
    msg = EmailMessage()
    msg.set_content('This is Test Email')

    msg['Subject'] = 'Request to stand up a new cluster'
    msg['From'] = sender
    msg['To'] = to

    while True:
        try:
            server = smtplib.SMTP(smtp_server)
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
            server.quit()
        except smtplib.SMTPException:
            LOGGER.exception("Exception sending email")
            time.sleep(10)
        else:
            LOGGER.info("Email sent to IMS")
            break

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    email_ims('admin@isiloncloud.com', 'DellEMC123!!', 'admin@isiloncloud.com', 'Robert.Li2@emc.com', 'smtp.office365.com:587')
       # time.sleep(1)
