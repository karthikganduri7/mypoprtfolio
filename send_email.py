import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "karthikganduri.gcp@gmail.com"
password = "rwdyejvhpsbangus"

receiver = "karthikganduri.gcp@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: Test mail
Hi
This is to test mail
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

