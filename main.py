
from tracker import Tracker
from adafruit import Adafruit


track_init = Tracker()
track_init.scrape_val()
rsival = track_init.fetch_val()

adafruit_init = Adafruit()
adafruit_init.send_val(rsival)

