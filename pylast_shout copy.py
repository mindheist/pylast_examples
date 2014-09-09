# Pre-Req - The following example assumes that you already have pylast downloaded and installed
#         - And have generated an API_KEY from last.fm 
# The objective of this example is to leave a shout for an artist of your liking

import pylast
API_KEY = "===================="
API_SECRET = "===================="
username = "===================="
password_hash = pylast.md5("====================")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

# In the below line - get_artist() method takes the title of the artist as a parameter , fetches and stores it in the variable artist

artist = network.get_artist("System of a Down")


# the below line leaves a shout on the artist's page , if you have your username and password filled out correctly above ;you should be able to see the 
# shout on the artist's page 

artist.shout("<<<<3")

# We could do more with the above skeleton code

