# The objective of this example is to get the 'total playcount' for an artist 
#================================================================================
# Pre-Req - The following example assumes that you already have pylast downloaded and installed
#         - And have generated an API_KEY from last.fm 

import pylast
API_KEY = "===================="
API_SECRET = "===================="
username = "===================="
password_hash = pylast.md5("====================")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

# In the below line - get_artist() method takes the title of the artist as a parameter , fetches and stores it in the variable artist

artist = network.get_artist("System of a Down")

# the following line gets the total playcount associated with the artist. This is the total number of scrobbles for the artist.

print artist.get_playcount()

#Output
#=======
# If you run this script on the commandline 
#python pylast_getplaycount 
#202441127


