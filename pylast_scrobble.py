# The objective of this example is to 'scrobble a single song' 
#============================================================================
# Pre-Req - The following example assumes that you already have pylast downloaded and installed
#         - And have generated an API_KEY from last.fm 

import pylast
from datetime import datetime
import time

API_KEY = "===================="
API_SECRET = "===================="
username = "===================="
password_hash = pylast.md5("====================")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

# the below line computes the current time , which is one of the parameters for the scrobble method
# A lot of massaging has been done over the default time stamp , will explain this later.

CurrentTimestamp = int(time.mktime(datetime.now().timetuple()))

# scrobble takes three paramters , artist , title of the track and the timestamp computed above

network.scrobble(artist="Jim Guthrie" , title="Toy Computer" , timestamp = CurrentTimestamp )

#Output
#======
# The song scrobbles sucessfully in your last.fm page
