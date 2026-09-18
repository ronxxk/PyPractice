import requests
import os
from dotenv import load_dotenv
import pywhatkit

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("api")
no = os.getenv("no")

weather_params = {
"lat": float(os.getenv("lat")),
"lon": float(os.getenv("lon")),
"appid": api_key,
"cnt":5
}

data = requests.get(OWM_Endpoint, params=weather_params)

data.raise_for_status()

data = data.json()


for i in range(0, 5):
    forcast = data["list"][i]["weather"][0]
    if forcast["id"] < 700:
        print("Bring an umbrella today!")
        pywhatkit.sendwhatmsg(
            phone_no=no, 
            message="Bring an umbrella today!", 
            time_hour=6, 
            time_min=0,
            wait_time=15,
            tab_close=True,
            close_time=5
        )
        break
    else:
        print("No need for an umbrella today!")
        pywhatkit.sendwhatmsg(
            phone_no=no, 
            message="No need for an umbrella today!", 
            time_hour=22, 
            time_min=14,
            wait_time=15,
            tab_close=True,
            close_time=5
        )
        break
