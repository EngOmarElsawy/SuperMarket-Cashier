import smtplib
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def sendEmail(to_email):
    config = configparser.ConfigParser()
    config.read('config.ini')
    from_email  = config['email']['from_email']
    password    = config['email']['password']
    smtp_server = config['email']['smtp_server']
    smtp_port   = int(config['email']['smtp_port'])

    from pdf import convert_to_pdf
    convert_to_pdf("Fatora.txt", "fatora.pdf")

    message = MIMEMultipart()
    message['To']      = to_email
    message['From']    = from_email
    message['Subject'] = 'Supermarket Receipt'

    with open('fatora.pdf', 'rb') as pdf_file:
        attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
        attachment.add_header('Content-Disposition', 'attachment', filename='Receipt.pdf')
        message.attach(attachment)

    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(from_email, password)
    smtp_obj.sendmail(from_email, to_email, message.as_string())
    smtp_obj.quit()
