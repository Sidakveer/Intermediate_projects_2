import datetime
import requests


USERNAME = "sidak" #your username
TOKEN = "dfsfdsfds" #your token

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph12",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

response1 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response1.text)

pixel_end = f"{pixela_endpoint}/{USERNAME}/graphs/graph12"

today = datetime.datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3"
}


response3 = requests.post(url=pixel_end, json=pixel_params, headers=headers)
print(response3.text)