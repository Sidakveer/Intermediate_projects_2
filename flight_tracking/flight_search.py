import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
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
        response = requests.get(url=TEQUILA_ENDPOINT, params=paramas, headers=headers)
        result = response.json()
        code = result["locations"][0]["code"]
        return code

