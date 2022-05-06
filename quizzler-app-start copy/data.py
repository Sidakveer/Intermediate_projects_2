import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.encoding = "utf-8"
data = (response.json())



question_data = data["results"]