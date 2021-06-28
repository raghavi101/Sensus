import unittest, requests
from bs4 import BeautifulSoup
from tracker import Tracker

class TestTracker(unittest.TestCase):
    def setUp(self):
     
        page = requests.get(
        "https://www.moneycontrol.com/technical-analysis/indian-indices/sensex-4/daily")
        soup = BeautifulSoup(page.content, 'html.parser')
        self.rsival = soup.select('strong')[31].text

    def tearDown(self):
        pass

    def test_scrape_val(self):

        ''' Test cases for rsival'''
  
        test_rsival = float(self.rsival)
        if test_rsival >=0 and test_rsival <= 100:
            self.assertGreaterEqual(test_rsival, 0)
            self.assertLessEqual(test_rsival, 100)
        print(self.shortDescription())


if __name__=="__main__":
    unittest.main()



