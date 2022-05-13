import requests

from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager


data_manager1 = DataManager()
sheet_data = data_manager1.get_destination_data()
print(sheet_data[0])

for x in range(len(sheet_data)):
    if sheet_data[x]["iataCode"] == "":
        flight_search1 = FlightSearch()
        sheet_data[x]["iataCode"] = flight_search1.get_destination_code()

    data_manager1.destination_data = sheet_data
    data_manager1.update_destination_codes()
    print(sheet_data)
