#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup
import urllib2, json, cPickle, urllib, os

# Open the pickle, and load it into the dict
with open('ponyFMdb.pickle', 'rb') as handle:
    dict = cPickle.load(handle)

currentFile = ""

try:
    for key, value in dict.iteritems():
        streams = value['streams']
        dlLink = streams['mp3']
        track  = str(value['id'])
        
        currentFile = "dl/" + track + ".mp3"
        if not os.path.isfile(currentFile):
            try:
                testfile = urllib.URLopener()
                testfile.retrieve(dlLink, currentFile )
                print track + " done!"
            except Exception:
                print track + " failed: " + value['title']
except KeyboardInterrupt:
    os.remove(currentFile)