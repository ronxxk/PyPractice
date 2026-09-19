import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("username")
token = os.getenv("token")
pixela = "https://pixe.la/v1/users"
now = datetime.now()
now_date = (now.strftime("%Y")+now.strftime("%m")+now.strftime("%d"))

params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela}/{username}/graphs"
graph_config = {
    "id": "graph2",
    "name": "pages",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
    }

headers = {
    "X-USER-TOKEN": token
}    

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela}/{username}/graphs/graph2"

data = {
    "date": now_date,
    "quantity": (input("How many pages did u read today?\n")),
}

#response = requests.post(url=pixel_creation_endpoint, json=data, headers=headers)

