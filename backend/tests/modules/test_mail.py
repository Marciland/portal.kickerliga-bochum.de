# pylint: skip-file
from email.parser import BytesParser
from email import policy
import socket
import ssl
from unittest.mock import patch, mock_open
from models import EmailCreds
from modules import MailClient, Mail

test_credentials = EmailCreds(email='test@test.test',
                              password='verystrongtestpassword')


def test_Smtp_init():
    smtp = MailClient(test_credentials)
    assert smtp.credentials == test_credentials
    assert smtp.sender == test_credentials.email
    assert isinstance(smtp.client.sock, socket.socket)
    assert isinstance(smtp.client.sock, ssl.SSLSocket)


def test_Smtp_create_email():
    smtp = MailClient(test_credentials)
    subject = 'Test Subject'
    content = 'Test Content'
    mail = smtp.create_email(content=content, subject=subject)
    parser = BytesParser(policy=policy.default)
    parsed_mail = parser.parsebytes(mail.as_bytes())
    html_part = next(
        (part.get_payload(decode=True).decode(part.get_content_charset())
         for part in parsed_mail.iter_parts()
         if part.get_content_type() == 'text/html'),
        None
    )
    assert html_part == content


def test_Mail_init():
    subject = 'Test Subject'
    content = 'Test Content'
    mail = Mail(content=content, subject=subject)
    parser = BytesParser(policy=policy.default)
    parsed_mail = parser.parsebytes(mail.as_bytes())
    html_part = next(
        (part.get_payload(decode=True).decode(part.get_content_charset())
         for part in parsed_mail.iter_parts()
         if part.get_content_type() == 'text/html'),
        None
    )
    assert html_part == content


def test_Mail_attach_file():
    subject = 'Test Subject'
    content = 'Test Content'
    file_name = 'Test file name'
    file_path = 'Test file path'
    file_data = b'Test data'
    mail = Mail(content=content, subject=subject)
    with patch('builtins.open', mock_open(read_data=file_data)):
        mail.attach_file(file_path=file_path,
                         file_name=file_name)
    attached_part = mail.get_payload()[1]
    assert attached_part.get_payload(decode=True) == file_data
    assert attached_part.get_filename() == file_name
