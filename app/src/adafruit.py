from Adafruit_IO.client import Client, Feed, Data
import os


class Adafruit :

    def __init__(self):

        '''Environment variables for the local system are set up to establish connection '''

        self.ADAFRUIT_IO_KEY = os.environ.get('IO_KEY')
        self.ADAFRUIT_IO_USERNAME = os.environ.get('IO_USERNAME')
        

    def sendval(self, rsival):

        ''' Client connection is established to adafruit.io and rsi value is rallied to the gaugemeter feed'''

        aio = Client(self.ADAFRUIT_IO_USERNAME, self.ADAFRUIT_IO_KEY)
        self.rsival=rsival
        aio.send('gaugemeter', value=rsival)










 



