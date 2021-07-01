from Adafruit_IO.client import Client, Feed, Data
import os


class Adafruit :

    def __init__(self):

        '''Environment variables for the local system are set up to establish connection '''

        self.ADAFRUIT_IO_KEY = os.environ.get('IO_KEY')
        self.ADAFRUIT_IO_USERNAME = os.environ.get('IO_USERNAME')
        self.aio = Client(self.ADAFRUIT_IO_USERNAME, self.ADAFRUIT_IO_KEY)

    def send_val(self, rsival):

        ''' Client connection is established to adafruit.io and rsi value is rallied to the gaugemeter feed'''

        self.rsival=rsival
        self.aio.send('gaugemeter', value=rsival)


    def send_val_trial(self, test_rsival):

        ''' Sensus_test '''

        self.aio.send('gaugemeter-test', test_rsival)








 



