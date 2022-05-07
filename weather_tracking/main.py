import requests

param = {
    "lat": -0.1,
    "lon": 0.51,
    "appid": "",
    "exclude": "current,minutely,daily"
}

hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=param)
response.raise_for_status()
data = (response.json())

will_rain = False
for x in hours:
    hourly_waether = data["hourly"][x]["weather"]
    weather_id = hourly_waether[0]["id"]
    print(weather_id)
    if weather_id < 700:
        will_rain = True
    else:
        print(hourly_waether[0]["description"])

if will_rain:
    print("Bring an umbrella")