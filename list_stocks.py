import requests
import json
from bs4 import BeautifulSoup

def request_html():
    url = "https://www.fundamentus.com.br/detalhes.php?papel=&h=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
    }
    response = requests.get(url=url, headers=headers)
    return response.text

def save(content):
    with open("content.html", "w") as file:
        file.write(content)

def load_file():
    with open("content.html", "r") as file:
        content = file.read()
        return content

def parse(content):
    soup = BeautifulSoup(content, "html.parser")
    body = soup.find("tbody")
    rows = body.find_all("tr")
    
    all_items = []

    for row in rows:
        items = row.find_all("td")
        obj = {"Papel": items[0].text, "Nome": items[1].text, "Razao": items[2].text}
        all_items.append(obj)

    return all_items

def save_json(content):
    with open("stocks.json", "w") as file:
        file.write(content)


#content = request_html()
#save(content)
content = load_file()
items = parse(content)
obj = { "data": items }
json_data = json.dumps(obj, ensure_ascii=False)
save_json(json_data)
