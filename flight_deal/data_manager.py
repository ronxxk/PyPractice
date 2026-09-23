
import requests




class DataManager:

    def __init__(self, departure, arrival, type_, username, email, time, logs, api):
        self.departure = departure 
        self.arrival = arrival 
        self.type_ = type_ 
        self.TOKEN = api 
        self.username = username
        self.email = email
        self.time = time
        self.logs = logs
        
    def something(self):
        

        ENDPOINT = f"https://api.sheety.co/{self.TOKEN}/flightFinderByRonxxk/data"
        
        params = {
            "username": self.username,
            "email": self.email,
            "departure": self.departure,
            "arrival": self.arrival,
            "type": self.type_,
            "time": self.time,
            "logs": self.logs,
        }

        # 3. Headers (Sheety needs authentication and JSON content type)
        headers = {
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }

        # 4. Sheety requires payload wrapped in the singular sheet tab name (e.g. "user")
        payload = {"datum": params}
        # 5. Send POST request
        response = requests.post(ENDPOINT, json=payload, headers=headers)

        return response.json()