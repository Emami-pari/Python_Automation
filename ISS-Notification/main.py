import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
my_email="******@ymail.com"
my_pass="******"
msg=EmailMessage()
msg["to"] =my_email
msg["Subject"]="Let's see the iss above your head!"
msg["From"]=my_email
my_lat=31.894480
my_lng=54.369541
my_pos=(my_lat,my_lng)
print(my_pos)

def iss_check():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    #print(response.status_code)     #just show the status code 200,300,400....
    response.raise_for_status()
    data=response.json()
    longitude=float(data["iss_position"]["longitude"])      #because ma lat,lng have decimal
    latitude=float(data["iss_position"]["latitude"])
    iss_pos=(longitude,latitude)
    print(iss_pos)
    if abs(my_pos[0]-iss_pos)<=5 and abs(my_pos[1]-iss_pos[1])<=5:
        return True

def night():
    parameters={
        "lat": my_lat,
        "lng":my_lng,                    #lng not long
        "formatted":0
    }
    response2=requests.get(url="https://api.sunrise-sunset.org/v2",params=parameters)
    response2.raise_for_status()
    data2=response2.json()
    print(data2.keys())
    sunrise=int(data2['sunrise'].split("T")[1].split(":")[0])
    sunset=int(data2["sunset"].split("T")[1].split(":")[0])
    print(sunrise,sunset)

    time_now=datetime.now()
    #print(time_now.hour)
    if time_now.hour<=sunrise or time_now.hour>=sunset:
        return True

if night() and iss_check():
    with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        msg.set_content("go outside and see the iss above in the sky")
        connection.send_message(msg)

