#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from dotenv import load_dotenv
import os

load_dotenv()

API  = str(os.getenv("x-app-key"))

try:
    depart = input("Enter Your Departure Airport IATA Code: ").upper().strip()
    arrival = input("Enter Your Arrival Airport IATA Code: ").upper().strip() 
    type_ = int(input("Type '1' for Round Trip\nType '2' for One-Way Trip\n"))
    
    searcher = FlightSearch(departure=depart, arrival=arrival, API_KEY=API, type=type_)
except:
    print("Please Input Valid IATA Code Or Type")


raw_json = searcher.touch()

flight_info = FlightData(raw_json)

text = flight_info.return_data()

print(text)

