import unittest, requests
from tracker import Tracker

class TestTracker(unittest.TestCase):
    def setUp(self):
     
        track_init = Tracker()
        track_init.scrape_val()
        self.rsival = track_init.fetch_val()

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



