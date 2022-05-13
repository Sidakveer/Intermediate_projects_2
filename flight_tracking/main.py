from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager1 = DataManager()
sheet_data = data_manager1.get_destination_data()
print(sheet_data)
print(data_manager1.update_destination_codes())