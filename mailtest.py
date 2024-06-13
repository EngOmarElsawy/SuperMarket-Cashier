
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication





# Email credentials and settings
def sendEmail(to_email):
        # from bettersuper import customermail
        # to_email = 'omar.future.123@gmail.com'
        from_email = 'omarelsawy160@gmail.com'
        subject = 'PDF Attachment Test'
        smtp_server = 'smtp.example.com'
        smtp_port = 587

        from pdf import convert_to_pdf


        # Create a new email message with the PDF file as an attachment
        message = MIMEMultipart()
        message['To'] = to_email
        message['From'] = from_email
        message['Subject'] = subject
        convert_to_pdf("Fatora.txt","fatora.pdf")
        with open('fatora.pdf', 'rb') as pdf_file:
                attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
                attachment.add_header('Content-Disposition', 'attachment', filename='Supermarket Recipet.pdf')
        message.attach(attachment)
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login('omarelsawy160@@gmail.com', 'qxnsyaxbqeatgtxs')
        smtp_obj.sendmail(from_email, to_email, message.as_string())
        smtp_obj.quit()
# sendEmail('omar.future.123@gmail.com')