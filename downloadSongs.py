#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib.request, json, pickle, urllib, os, re

# Open the pickle, and load it into the dict
with open('ponyFMdb.pickle', 'rb') as handle:
	dict = pickle.load(handle)

currentFile = ""
currentNum = 1

try:
	for key, value in dict.items():
		streams = value['streams']
		dlLink = streams['mp3']
		track  = str(value['id'])
		
		currentFile = "dl/" + track + ".mp3"
		if not os.path.isfile(currentFile):
			try:
				testfile = urllib.request.URLopener()
				urllib.request.urlretrieve(dlLink, currentFile )
				print (track + " done! (" + str(currentNum) + " of " + str(len(dict)) + ")")
			except Exception:
				try:
					print (track + " failed: " + value['title'])
				except Exception:
					print ("Printing the name of the file that failed has failed.")
		currentNum += 1
except KeyboardInterrupt:
	os.remove(currentFile)