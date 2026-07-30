import datetime as dt
import random
import smtplib
import pandas as pd
from email.message import EmailMessage
my_email="***@ymail.com"
my_pass="*****"
msg=EmailMessage()
msg["Subject"]="Happy Birthday!"
msg["From"]=my_email

today_tuple=(dt.datetime.now().month,dt.datetime.now().day)
file=pd.read_csv("birthdays.csv")
birthdays_dic = {
    (row.month,row.day):row for (index,row) in file.iterrows()
    }
print(birthdays_dic)


if today_tuple in birthdays_dic:
    person_detail=birthdays_dic[today_tuple]             # as a row of table has coloumns
    if person_detail["name"]=="Hengame"or "Leila" or "Masume" or "Zohre":    
        number=22                              #use specific letter for specific friends
    else:
        number=random.randint(1,3)
    letter_path=f"letter_templates/letter_{number}.txt"
    with open(letter_path) as letter:
        content=letter.read()
        content=content.replace("[NAME]",person_detail["name"])     #because of replace it should be saved

    with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        recipient_email = person_detail["email"]
        msg["to"] = recipient_email
        msg.set_content(content)
        connection.send_message(msg)
        print("sent")


