from smtplib import SMTP, SMTP_SSL
from email.message import EmailMessage


class MailhogSMTP(SMTP):
    def __init__(self, username, password):
        super().__init__('localhost', port=1025)
        self.login(username, password)

    """A wrapper for handling SMTP connections to FastMail."""
    def send_email(self, from_address, to_address, subject, content, mail_options=(), rcpt_options=()):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = to_address
        msg.set_content(content)
        self.send_message(msg)


class FastMailSMTP(SMTP_SSL):
    """A wrapper for handling SMTP connections to FastMail."""
    def __init__(self, username, password):
        super().__init__('mail.messagingengine.com', port=465)
        self.login(username, password)

    """A wrapper for handling SMTP connections to FastMail."""
    def send_email(self, from_address, to_address, subject, content, mail_options=(), rcpt_options=()):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = to_address
        msg.set_content(content)

        self.send_message(msg)
