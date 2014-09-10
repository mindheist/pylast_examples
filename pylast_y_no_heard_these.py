import pylast
API_KEY = "===================="
API_SECRET = "===================="
username = "===================="
password_hash = pylast.md5("====================")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)
user = network.get_user(username)

L4 = user.get_top_artists()
#for index,item in enumerate(L4):
#	print index,item[0]

a = L4[0]
artist_number_one = a[0]
print " "
print "==========================================="

print "Your Most Favorite Artist is" , a[0]
print "==========================================="

#print a[0] ,"top songs are "
#print "==========================================="

set1= set()
set2 = set()
set3 = set()
L9 = artist_number_one.get_top_tracks()
for item in L9:
	#print item.item.title
	set1.add(item.item.title)
	#print item[]
	#print dir(item)
	#print dir(item.item)
	#break
    #L50.append(item[0])
    #print item.item.artist, " - ", item.item.title
    #break
#print set1
#print "==========================================="
#print "Songs of " , a[0] ," you have heard all these years"
#print "==========================================="
L10 = user.get_artist_tracks(a[0])
for item in L10:
	#print type(item)
	#print item.track.title
	set2.add(item.track.title)
	#print item.track
	#print dir(item)
#print set2
#for index,item in enumerate(L10):
#	print index,item

print" "
print" _______       ___       _______  __    __    ______      "
print"|       \     /   \     |   ____||  |  |  |  /  __  \     "
print"|  .--.  |   /  ^  \    |  |__   |  |  |  | |  |  |  |    "
print"|  |  |  |  /  /_\  \   |   __|  |  |  |  | |  |  |  |    "
print"|  '--'  | /  _____  \  |  |     |  `--'  | |  `--'  '--. "
print"|_______/ /__/     \__\ |__|      \______/   \_____\_____\ "
print" "

print "==========================================="
print " "
print"__   __  _  _  ___    _  _ ___   _   ___ ___    _____ _  _ ___ ___ ___ ___ "
print"\ \ / / | \| |/ _ \  | || | __| /_\ | _ \   \  |_   _| || | __/ __| __|__ \ "
print" \ V /  | .` | (_) | | __ | _| / _ \|   / |) |   | | | __ | _|\__ \ _|  /_/"
print"  |_|   |_|\_|\___/  |_||_|___/_/ \_\_|_\___/    |_| |_||_|___|___/___|(_) "
print " "
#print "Havent you heard these ??"
print "==========================================="
print " "
set3= set1-set2
mylist = list(set3)
for index,item in enumerate(mylist):
	print index,item