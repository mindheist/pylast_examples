# Pre-Req - The following example assumes that you already have pylast downloaded and installed
#         - And have generated an API_KEY from last.fm 
# The objective of this example is to leave a shout for an artist of your liking

import pylast
API_KEY = "XXXX"
API_SECRET = "XXX"
username = "XXXX"
password_hash = pylast.md5("XXX")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

# The below get_artist() method takes the title of a song as a parameter and fetches the name of the corresponding artist

artist = network.get_artist("System of a Down")

# the following line prints the name of the artist

print artist 

# this leaves a shout on the artist's page , if you have your username and password filled out correctly above ;you should be able to see the 
# shout on the artist's page 

artist.shout("<<<<3")

