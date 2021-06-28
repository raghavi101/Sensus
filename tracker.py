import requests
from bs4 import BeautifulSoup

class Tracker:

    def __init__(self):
        pass


    def scrape_val(self):

        ''' Desirable rsi value is scraped using beautiful soup '''

        page = requests.get(
        "https://www.moneycontrol.com/technical-analysis/indian-indices/sensex-4/daily")
        soup = BeautifulSoup(page.content, 'html.parser')
        self.rsival = soup.select('strong')[31].text

    def fetch_val(self):
  
        ''' rsi value from scareval() is returned '''

        return self.rsival

    







