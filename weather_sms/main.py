import requests
import os
from dotenv import load_dotenv
import pywhatkit

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("api")
no = os.getenv("no")
timehr = int(os.getenv("time_hour"))
timemin = int(os.getenv("time_min"))

weather_params = {
"lat": float(os.getenv("lat")),
"lon": float(os.getenv("lon")),
"appid": api_key,
"cnt":5
}

data = requests.get(OWM_Endpoint, params=weather_params)

data.raise_for_status()

data = data.json()


will_rain = False

for i in range(0, 5):
    forecast = data["list"][i]["weather"][0]
    if forecast["id"] < 700:
        will_rain = True
        break  


if will_rain:
    print("Bring an umbrella today!")
    pywhatkit.sendwhatmsg(
        phone_no=no, 
        message="Bring an umbrella today!", 
        time_hour=timehr, 
        time_min=timemin,
        wait_time=30,
        tab_close=True,
        close_time=5
    )
else:
    print("No need for an umbrella today!")
    pywhatkit.sendwhatmsg(
        phone_no=no, 
        message="No need for an umbrella today!", 
        time_hour=timehr, 
        time_min=timemin,
        wait_time=30,
        tab_close=True,
        close_time=5
    )