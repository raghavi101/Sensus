from Adafruit_IO.client import Client
import unittest, os
from adafruit import Adafruit

class TestAdafruit(unittest.Testcase):

    connection = None

    def setUp(self):
        self.ADAFRUIT_IO_KEY = os.environ.get('IO_KEY')
        self.ADAFRUIT_IO_USERNAME = os.environ.get('IO_USERNAME')
        self.connection = Client(self.ADAFRUIT_IO_USERNAME, self.ADAFRUIT_IO_KEY)

    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):
        self.assertTrue(self.connection.is_connected())


    def test_send_val(self,rsival):
        ''' Test cases for adafruit.sendval()'''

        self.assertGreaterEqual(rsival, 0)
        self.assertLessEqual(rsival, 100)


if __name__=="__main__":
    unittest.main()



