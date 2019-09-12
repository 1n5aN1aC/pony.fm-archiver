#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib.request, json, pickle, os

#Performs the requesting of the page, and loading soup
def loadSongListPage(pageNum):
    url = 'https://pony.fm/api/web/tracks?page=' + str(pageNum) + '&&order=published_at,asc'
    reader = urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/49.0' })
    page = urllib.request.urlopen(reader).read()
    # Convert json text to python dictionary
    return json.loads(page)

# Create pickle if doesn't exist...
if not os.path.isfile("ponyFMdb.pickle"):
    with open('ponyFMdb.pickle', 'wb') as handle:
        dict = {}
        pickle.dump(dict, handle)

# Open the pickle, and load it into the dict
with open('ponyFMdb.pickle', 'rb') as handle:
    dict = pickle.load(handle)

pageNum = 1
total_pages = 5
added = 0
updated = 0
unchanged = 0
# Loop until we reach the last page
while pageNum <= total_pages:
    print ("Page " + str(pageNum) + " of " + str(total_pages))
    data = loadSongListPage(pageNum)
    total_pages = data['total_pages']
    
    tracks = data['tracks']
    for track in tracks:
        id = track['id']
        if id not in dict:
            dict[id] = track
            added += 1
        else:
            #Check if changed?
            unchanged += 1
    pageNum += 1
print ("Complete.  " + str(added) + " new, " + str(updated) + " updated, and " + str(unchanged) + " unchanged.")

# Save the dict back to the pickle
with open('ponyFMdb.pickle', 'wb') as handle:
    pickle.dump(dict, handle)
