import requests
import json
from bs4 import BeautifulSoup

def request_html():
    url = "https://www.debit.com.br/tabelas/tabela-completa.php?indice=cdi"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
    }
    response = requests.get(url=url, headers=headers)
    return response.text

def parse(content):
    soup = BeautifulSoup(content, "html.parser")
    body = soup.find("main")
    tables = body.find_all("table")

    items = []

    for i, table in enumerate(tables):
        if i % 2 == 0:
            continue
        data = table.find_all("td")
        length = len(data)
        for j, td in enumerate(data):
            if j < length - 1 and j % 2 == 0:
                print(f"{td.text} {data[j + 1].text}")
        print("------------")

content = request_html()
parse(content)
#print(values)