import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
GMAIL_HOST = "smtp.gmail.com"

def send_csv(filename, name):

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = MY_EMAIL
    message['To'] = RECEIVER_EMAIL
    message['Subject'] = f"File with baby's name rating from {name}"

    # The body and the attachment for the mail
    attach_file_name = filename
    attach_file = open(attach_file_name, "rb") # Open file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment

    # Add payload header with filename
    payload.add_header("Content-Decomposition", "attachment", filename=attach_file_name)
    message.attach(payload)

    with smtplib.SMTP(GMAIL_HOST, port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        text = message.as_string()
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_EMAIL, msg=text)

    print("Email sent")
