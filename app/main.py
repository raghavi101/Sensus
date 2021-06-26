import sys
sys. path. append(".")
from src.tracker import Tracker
from src.adafruit import Adafruit


track_init = Tracker()
track_init.scrapeval()
rsival = track_init.fetchval()

adafruit_init = Adafruit()
adafruit_init.sendval(rsival)

