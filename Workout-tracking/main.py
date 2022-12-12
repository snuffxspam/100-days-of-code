import requests
import datetime
### track api
API_ID, API_KEY = "your api_id", "your api_key"

ex = input()

head = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

params = {
    "query": ex,
    "gender": "your gender",
    "weight_kg": "your weight",
    "height_cm": "your height",
    "age": "your age"
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=head)
res = response.json()



###sheety
API = "your sheety api"
bearer_headers = {
    "Authorization": f"Bearer {'your token'}"
}

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")
for i in res["exercises"]:
    data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }

sheet = requests.post(API, json=data, headers=bearer_headers)
print(sheet.text)