import requests
from bs4 import BeautifulSoup

def callval():
    page = requests.get(
    "https://www.moneycontrol.com/technical-analysis/indian-indices/sensex-4/daily")
    soup = BeautifulSoup(page.content, 'html.parser')
    rsival = soup.select('strong')[31].text
    return rsival 





