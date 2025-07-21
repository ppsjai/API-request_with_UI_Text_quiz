import requests
# https://opentdb.com/api.php?amount=10&category=15&difficulty=medium&type=boolean
# see the parameters variable--> amount was 10 given link was same and its type was boolean same in link.

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
