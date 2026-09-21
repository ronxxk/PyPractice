import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

        
class FlightSearch:
    def __init__(self, departure, arrival, API_KEY, type:int):
        self.departure = departure
        self.arrival = arrival
        self.api = API_KEY
        self.trip_type = int(type)
        
    def touch(self):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_later = datetime.now() + timedelta(days=6 * 30)
        ENDPOINT = "https://serpapi.com/search?engine=google_flights"
        params = {
            "engine":        "google_flights",
            "departure_id":  self.departure, 
            "arrival_id":    self.arrival,
            "outbound_date": tomorrow.strftime("%Y-%m-%d"),
            "type":          self.trip_type,  # "1" for round-trip, "2" for one-way
            "adults":        "1",
            "currency":      "INR",
            "stops":         "2",
            "api_key":       self.api, 
        }

        # Only include return_date if it's a round-trip search
        if self.trip_type == 1:
            params["return_date"] = six_month_later.strftime("%Y-%m-%d")
        try:
            response = requests.get(ENDPOINT, params=params)
            response.raise_for_status()  # Throws an error for bad HTTP codes (4xx, 5xx)
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {e}"}