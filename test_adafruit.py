import unittest, requests
from tracker import Tracker
from adafruit import Adafruit

class TestAdafruit(unittest.TestCase):
    def setUp(self):
        tracker_init = Tracker()
        tracker_init.scrape_val()
        self.rsival = tracker_init.fetch_val()
        self.adafruit_init = Adafruit()

    def tearDown(self):
        pass

    def test_send_val_trial(self):

        ''' Test cases for rsival sent to adafruit dashboard'''
        test_rsival = float(self.rsival)
        print(test_rsival)
        if test_rsival >=0 and test_rsival <= 100:
            self.assertGreaterEqual(test_rsival, 0)
            self.assertLessEqual(test_rsival, 100)
            self.adafruit_init.send_val_trial(test_rsival)
            
        
      

if __name__=="__main__":
    unittest.main()



