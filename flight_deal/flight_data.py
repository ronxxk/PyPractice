from flight_search import FlightSearch

class FlightData:
    def __init__(self, json_response: dict):
        self.raw_data = json_response 
    
    def return_data(self):
        if "error" in self.raw_data:
            return f"Please Enter Valid Input."

        # Filter for valid dictionaries containing price data
        raw_flights = self.raw_data.get("best_flights", []) + self.raw_data.get("other_flights", [])
        flights = [f for f in raw_flights if isinstance(f, dict) and "price" in f]

        if not flights:
            return "No valid flights found for the selected route."

        cheapest = min(flights, key=lambda f: f["price"])
        
        # Build up the output string line by line
        lines = [f"Cheapest Price: INR {cheapest['price']}"]

        # Extract flight segment details
        flight_legs = cheapest.get("flights", [])
        for leg in flight_legs:
            dep_airport = leg.get("departure_airport", {})
            arr_airport = leg.get("arrival_airport", {})
            airline     = leg.get("airline", "Unknown Airline")
            flight_num  = leg.get("flight_number", "")

            leg_info = (
                f"\n--- {airline} ({flight_num}) ---\n"
                f"Depart: {dep_airport.get('name', 'N/A')} ({dep_airport.get('id', '')}) at {dep_airport.get('time', 'N/A')}\n"
                f"Arrive: {arr_airport.get('name', 'N/A')} ({arr_airport.get('id', '')}) at {arr_airport.get('time', 'N/A')}"
            )
            lines.append(leg_info)

        return "\n".join(lines)