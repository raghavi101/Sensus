from usr.tracker import Tracker
from usr.adafruit import Adafruit

track_init = Tracker()
rsival = track_init.fetchval()

adafruit_init = Adafruit()
adafruit_init.sendval(rsival)

