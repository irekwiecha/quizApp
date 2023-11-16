import requests
from icecream import ic

parameters = {
    "amount": 10,
    "type": "boolean"
}

resp = requests.get("https://opentdb.com/api.php?", params=parameters)
resp.raise_for_status()
data = resp.json()
question_data = data["results"]
