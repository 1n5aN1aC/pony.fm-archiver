#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup
import urllib2, json, cPickle

#Performs the requesting of the page, and loading soup
def loadSongListPage(pageNum):
    url = 'https://pony.fm/api/web/tracks?page=' + str(pageNum) + '&&order=published_at,asc'
    reader = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/49.0' })
    page = urllib2.urlopen(reader).read()
    # Convert json text to python dictionary
    return json.loads(page)

# Open the pickle, and load it into the dict
with open('ponyFMdb.pickle', 'rb') as handle:
    dict = cPickle.load(handle)

pageNum = 1
total_pages = 5
while pageNum <= total_pages:
    added = 0
    exists = 0
    
    data = loadSongListPage(pageNum)
    total_pages = data['total_pages']
    
    tracks = data['tracks']
    for track in tracks:
        id = track['id']
        if id not in dict:
            dict[id] = track
            added += 1
        else:
            exists += 1
    
    print "Page " + str(pageNum) + ", added:" + str(added) + ", exists:" + str(exists)
    pageNum += 1

# Save the dict back to the pickle
with open('ponyFMdb.pickle', 'wb') as handle:
    cPickle.dump(dict, handle)