# The objective of this example is to 'get the music Brainz ID for an artist' 
#============================================================================
# Pre-Req - The following example assumes that you already have pylast downloaded and installed
#         - And have generated an API_KEY from last.fm 


import pylast
API_KEY = "===================="
API_SECRET = "===================="
username = "===================="
password_hash = pylast.md5("====================")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

artist = network.get_artist("System of a Down")

# the get_mbid() method gets the music brainz id corresponding to the artist

print "the music brainz id for system of a down is " , artist.get_mbid()

# Output
#=======
#python pylast_get_mbid 
# the music brainz id for system of a down is  cc0b7089-c08d-4c10-b6b0-873582c17fd6
# from https://musicbrainz.org/artist/cc0b7089-c08d-4c10-b6b0-873582c17fd6/details
# Name:	System of a Down
# MBID:	cc0b7089-c08d-4c10-b6b0-873582c17fd6
# Last updated:	2013-12-19 07:56 UTC
# Permanent link:	https://musicbrainz.org/artist/cc0b7089-c08d-4c10-b6b0-873582c17fd6
# XML:	https://musicbrainz.org/ws/2/artist/cc0b7089-c08d-4c10-b6b0-873582c17fd6?inc=aliases
