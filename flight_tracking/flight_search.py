import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "WOHB9UC1vPwzasp2J2txwn7pxSblWL1X"

class FlightSearch:

    def get_destination_code(self, cityName):

        headers = {
            "apikey": TEQUILA_API_KEY
        }

        paramas = {
            "term": cityName,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=paramas, headers=headers)
        result = response.json()
        code = result["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code,
                      des_city_code, from_time, to_time):
        headers = {
            "apikey": TEQUILA_API_KEY
        }

        params = {
            "fly_from": origin_city_code,
            "fly_to": des_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=params, headers=headers)

        try:
            data = response.json()["data"][0]
        except:
            print(f"No flights found for {des_city_code}")
            return None

        flight = FlightData(data["price"],data["route"][0]["cityFrom"],
                            data["route"][0]["flyFrom"],
                            data["route"][0]["cityTo"],
                            data["route"][0]["flyTo"],
                            # data["route"][0]["local_departure"].split("T")[0],
                            # data["route"][1]["local_departure"].split("T")[0]
                            )
        print(f"{flight.des_city}: {flight.price}")
        return flight