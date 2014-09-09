import pylast
API_KEY = "XXXX"
API_SECRET = "XXX"
username = "XXXX"
password_hash = pylast.md5("XXX")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

artist = network.get_artist("System of a Down")
artist.shout("<<<<3")

