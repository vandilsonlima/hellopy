import requests
import json

def save(content):
    with open("chart_year.json", "w") as file:
        file.write(content)

def chart():
    response = requests.get(
    "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart",
     params= {'interval': '1d', 'symbol': 'HGLG11.SA', 'range': '1y', 'region': 'BR'},
        headers={
            'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com',
            'x-rapidapi-key': '031368cb8cmshd04277d5b4ddb37p138d8djsn7201a96c3ca6'
        }
    )
    return response

r = chart()
data = json.dumps(r.json(), indent=4, sort_keys=True)
save(data)
