from email.mime.multipart import MIMEMultipart
# mime => multipurpose internet mail extensions => defines the format of emails

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()

message["from"] = "Aayush Jha"
message["to"] = "aayush@gmail.com"
message["subject"] = "This is a test email"

message.attach(MIMEText("this is the Body"))
message.attach(MIMEImage(Path("hey.png").read_bytes())) # requires data in binary

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()  # part of smtp protocol ie comm betn client and smtp server should start with a hello message
    smtp.starttls() # all the commands we send to the smtp server will be encrypted
    smtp.login("testuser@codewithmosh.com","password@123")
    smtp.send_message(message) 
    print("sent...")