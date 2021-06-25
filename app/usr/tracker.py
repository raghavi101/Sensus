import requests
from bs4 import BeautifulSoup

class Tracker:
    def __init__(self):
        page = requests.get(
        "https://www.moneycontrol.com/technical-analysis/indian-indices/sensex-4/daily")
        soup = BeautifulSoup(page.content, 'html.parser')
        self.rsival = soup.select('strong')[31].text

    def fetchval(self):
        return {self.rsival}

    







