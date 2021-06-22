from Adafruit_IO.client import Client, Feed, Data
import tracker

ADAFRUIT_IO_KEY = 'aio_wVUg01nJefE97yBetiKjKw5GIj6u'

ADAFRUIT_IO_USERNAME = 'sraghavi'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)



aio.send('gaugemeter', value=tracker.callval())

#success