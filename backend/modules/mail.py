from __future__ import annotations

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from models import EmailCreds as Credentials


class Smtp:
    def __init__(self, credentials: Credentials):
        self.credentials = credentials
        self.sender = credentials.email
        self.client = smtplib.SMTP(host='smtp.gmail.com', port=587)
        self.client.starttls()

    def login(self) -> None:  # pragma: no cover
        self.client.login(self.credentials.email,
                          self.credentials.password)

    def create_email(self, content: str, subject: str) -> Mail:
        mail = Mail(content, subject)
        mail['From'] = self.sender
        return mail

    def send_email(self, mail: Mail, to_address: str) -> None:  # pragma: no cover
        mail['To'] = to_address
        self.client.sendmail(from_addr=self.sender, to_addrs=to_address,
                             msg=mail.as_string())


class Mail(MIMEMultipart):
    def __init__(self, content: str, subject: str) -> None:
        super().__init__()
        self.attach(MIMEText(content, 'html'))
        self['Subject'] = subject

    def attach_file(self, file_path: str, file_name: str) -> None:
        with open(file_path, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            f'attachment; filename="{file_name}"')
            self.attach(part)
