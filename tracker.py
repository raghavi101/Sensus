import requests

from bs4 import BeautifulSoup

page = requests.get(
    "https://www.moneycontrol.com/technical-analysis/indian-indices/sensex-4/daily")
soup = BeautifulSoup(page.content, 'html.parser')

first_h1 = soup.select('strong')[35].text
print(first_h1)

