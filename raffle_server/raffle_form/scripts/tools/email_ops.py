import math
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# configuration
sender_email = "rafflebeezarebuzzing@gmail.com"  # Enter your address
password = r"B33zylil'beez"

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
email_length = 15
list_email = []

def generate_email(domain):
        email = ""
        for letter in range(0, email_length):
                email += chars[math.floor(random.random() * len(chars))]
        email += domain
        return email

def get_list(domain, count):
      for i in range(int(count)):
            email_id = generate_email(domain)
            list_email.append(email_id)
      return list_email
      
def send_email(receiver_email, subject,message_content):        

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        html = """\
        <html>
          <body style="background-color: #428bca; text-align: justify; color: white;
                  font-size: 20px;
                  font-family: Arial, Helvetica, sans-serif;
                  padding: 30px;">
            <p>Hi there,<br><br>
        
        {}
        
            <br>
            <br>
            Regards, <br>
            Raffle Beez
            </p>
          </body>
        </html>
        """.format(message_content)

        # Turn these into plain/html MIMEText objects
        part = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        message.attach(part)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
