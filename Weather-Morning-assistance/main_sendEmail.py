import smtplib
import os
from email.message import EmailMessage
from create_recom import message
my_email="parisa2emami@ymail.com"
my_pass=os.environ.get(Email_PASS)
msg=EmailMessage()
msg["to"] ="emo.golpari2010@gmail.com"
msg["Subject"]="Let's check weather and clothes!"
msg["From"]=my_email

def send_email():
    with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        msg.set_content(message)
        connection.send_message(msg)

send_email()
