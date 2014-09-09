# The objective of this example is to get the 'total number of last.fm listeners' an artist 
#==========================================================================================

# Pre-Req - The following example assumes that you already have pylast downloaded and installed
#         - And have generated an API_KEY from last.fm 

import pylast
API_KEY = "===================="
API_SECRET = "===================="
username = "===================="
password_hash = pylast.md5("====================")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

artist = network.get_artist("Jim Guthrie")

# the get_playcount() methods gets the total number of scrobbles associated with the artist

print "total number of playcounts = " , artist.get_playcount()

# the get_listener_count() methods gets the total number of unique listeners associated with the artist

print "total number of unique listeners = " , artist.get_listener_count()

#Output:
#=======
# python pylast_get_total_listeners 
#total number of playcounts =  2193454
#total number of unique listeners =  56605
