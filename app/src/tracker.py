import requests
from bs4 import BeautifulSoup

class Tracker:
    def scrapeval(self):

        ''' Desirable rsi value is scraped using beautiful soup '''

        page = requests.get(
        "https://www.moneycontrol.com/technical-analysis/indian-indices/sensex-4/daily")
        soup = BeautifulSoup(page.content, 'html.parser')
        self.rsival = soup.select('strong')[31].text

    def fetchval(self):
  
        ''' rsi value from scareval() is returned '''

        return self.rsival

    







