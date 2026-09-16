import os
import platform
import time
from datetime import datetime, timezone
import requests
from dotenv import load_dotenv

# Build absolute path to .env file in parent directory
load_dotenv()

lat_ = float(os.getenv("lat"))
lng_ = float(os.getenv("lng"))

#file_path = "sample_media.mp4"

parameters = {
    "lat": lat_,
    "lng": lng_,
    "formatted": 0,
}

def isoverhead():
    api_iss = requests.get("http://api.open-notify.org/iss-now.json")
    api_iss.raise_for_status()
    data_iss = api_iss.json()
    iss_lng = float(data_iss["iss_position"] ["longitude"])
    iss_lat = float(data_iss["iss_position"] ["latitude"])
    
    return (iss_lat - 5 < lat_ < iss_lat + 5 and iss_lng - 5 < lng_ < iss_lng + 5)

def isvissible():
    api_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    api_sun.raise_for_status()
    data_sun = api_sun.json()
    sun_rise = datetime.fromisoformat(data_sun["results"]["sunrise"])
    sun_set = datetime.fromisoformat(data_sun["results"]["sunset"])
    time_ = datetime.now(timezone.utc)

    
    return(time_ < sun_rise or time_ > sun_set)

print("Monitoring ISS overhead passes during night time...")

while True:
    try:
        if isoverhead() and isvissible():
            print("Look up! The ISS is near and visible in the night sky!")
            '''if platform.system() == "Windows":
                os.startfile(file_path)
            elif platform.system() == "Darwin":  # macOS
                os.system(f'open "{file_path}"')
            else:  # Linux
                os.system(f'xdg-open "{file_path}"')'''
            break
        else:
            print("Iss not yet visible!")
    except requests.RequestException as e:
        print(f"API Request failed: {e}. Retrying in 60s...")

    time.sleep(60)
