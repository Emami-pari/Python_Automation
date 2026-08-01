import requests
from WMO_code import WEATHER_CODES
from collections import Counter
import json
with open("config.jason") as file:
    config=json.load(file)
city=config["city"]

def get_location():
    parameters = {
        "name": city
    }
    response=requests.get(url="https://geocoding-api.open-meteo.com/v1/search",params=parameters)
    #print(response.status_code)
    response.raise_for_status()
    data=response.json()
    longitude=data["results"][0]["longitude"]
    latitude=data["results"][0]["latitude"]
    return latitude,longitude

def get_weather(lat,lon):
    hourly_vars=["temperature_2m","precipitation_probability","precipitation","weather_code"]
    parameters={
        "latitude": lat,
        "longitude":lon,
        "timezone":"auto",
        "hourly":",".join(hourly_vars),      #should be lon string, not a list here api doesnt recognize
        "forecast_day":1                    # dont work with this type of data
    }
    response2=requests.get(url="https://api.open-meteo.com/v1/forecast",params=parameters)
    response2.raise_for_status()
    data2=response2.json()
    print(data2["hourly"].keys())

    return data2

def data_analysis(data):   # to filter the T, PP , P form 7-4
    tem=data["hourly"]["temperature_2m"][7:16]
    precip=data["hourly"]["precipitation"][7:16]
    prob_precip=data["hourly"]["precipitation_probability"][7:16]
    wmo_code=data["hourly"]["weather_code"][7:16]
    tem_ave=sum(x for x in tem)/len(tem)
    precip_ave=sum(x for x in precip)/len(precip)
    prob_ave=sum(x for x in prob_precip)/len(prob_precip)
    counter=Counter(wmo_code)
    most_common=counter.most_common(1)[0][0]   # to find most common weather code
    if most_common in WEATHER_CODES:
        w_c=WEATHER_CODES[most_common]
    return {
        "T": tem_ave,
        "P": precip_ave,
        "Prob_p": prob_ave,
        "W_C": w_c
    }
latitude,longitude= get_location()
data=get_weather(latitude,longitude)
weather=data_analysis(data)
