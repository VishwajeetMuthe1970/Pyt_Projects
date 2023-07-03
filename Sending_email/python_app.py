from email.message import EmailMessage
#from app2 import password
import ssl
import smtplib

email_sender = 'vsmuthe@gmail.com'
email_password = input("Please Enter your password")

email_receiver = 'rayori5577@chotunai.com'

subject = "Sending mail from python."
body = """
This is exciting to send an email using python!
"""

# Creating an instance of this email message.

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



