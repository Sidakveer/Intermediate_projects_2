import datetime

import requests

from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager


data_manager1 = DataManager()
sheet_data = data_manager1.get_destination_data()
flight_search1 = FlightSearch()

ORIGIN_CITY_IATA = "JFK"

for x in range(len(sheet_data)):
    if sheet_data[x]["iataCode"] == "":
        city_name = sheet_data[x]["city"]
        sheet_data[x]["iataCode"] = flight_search1.get_destination_code(city_name)

    data_manager1.destination_data = sheet_data
    data_manager1.update_destination_codes()

    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    sixmonths_from_now = datetime.datetime.now() + datetime.timedelta(days=(6 * 30))

    flight = flight_search1.check_flights(ORIGIN_CITY_IATA,
                                          sheet_data[x]["iataCode"],
                                          tomorrow, sixmonths_from_now)
