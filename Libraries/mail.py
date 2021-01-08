from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "joaquintor2014@hotmail.com"
message["to"] = "jtornello2019@hotmail.com"
message["subject"] = "Testing"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.live.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # Transport Layer Security mode -> Encryption
    smtp.login("joaquintor2014@hotmail.com", "Qwerty2013")
    smtp.send_message(message)
    print("Sent...")
