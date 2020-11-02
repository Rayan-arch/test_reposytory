import smtplib


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class GmailAdapter:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.username = username
        self.password = password
        self.server = smtplib.SMTP_SSL(host, port)

    def login(self):
        self.server.ehlo()
        self.server.login(self.username, self.password)

    def send_mail(self, recipient_email: str, subject: str, content: str):
        message = self._compose_message(content, recipient_email, subject)
        self.server.sendmail(self.username, recipient_email, message.as_string())

    def _compose_message(self, content, recipient_email, subject):
        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = self.username
        message['To'] = recipient_email
        message.attach(
            MIMEText(content, 'html')
        )
        return message

    def __del__(self):
        self.server.close()
