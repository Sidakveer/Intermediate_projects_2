import datetime
import requests


APP_ID = "71ade528"
API_KEY = "84f26a437c068d01fb04e5a5b034eee4"
GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "174"
AGE = "22"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("Enter what exercise you did? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

json_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=json_params, headers=headers)
result = response.json()
x = (result["exercises"][0])
dateToday = datetime.datetime.now().strftime(f"%d/%m/%Y")
time_now = datetime.datetime.now().strftime("%X")

sheety_params = {
    "workout": {

        "date": dateToday,
        "time": time_now,
        "exercise": x["name"],
        "duration": x["duration_min"],
        "calories": x["nf_calories"],

    }
}

sheety_response = requests.post(url="https://api.sheety.co/63fb69ef04fd0000558b3b99957a8d83/workouts/workouts", json=sheety_params)
print(sheety_response.json())