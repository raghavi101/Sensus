from Adafruit_IO.client import Client, Feed, Data
import os
import tracker

ADAFRUIT_IO_KEY = os.environ.get('IO_KEY')

ADAFRUIT_IO_USERNAME = os.environ.get('IO_USERNAME')

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

aio.send('gaugemeter', value=tracker.callval())




 



#success