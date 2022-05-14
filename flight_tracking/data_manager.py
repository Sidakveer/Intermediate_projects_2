import requests


SHEETY_ENDPOINT = "https://api.sheety.co/63fb69ef04fd0000558b3b99957a8d83/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for x in self.destination_data:
            params = {
                "price": {
                "iataCode": x["iataCode"]
            }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{x['id']}", json=params)

            # print(response.text)
