import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 45.501690 # Your latitude
MY_LONG = -73.567253 # Your longitude



def position_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    if (40 < iss_latitude < 50.5) and (-78 < iss_longitude < -68):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset < time_now.hour < sunrise:
        return True


while True:
    time.sleep(60)
    username = ""
    password = ""
    if position_check() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=578) as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(from_addr=username, to_addrs="me@gmail.com", msg="Subject:Look up\n\n<Body>")

