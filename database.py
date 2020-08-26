# Reading through a json file and adding the count parts of the file and giving the sum.
import json, urllib.request, urllib.parse, urllib.error
serviceurl = "http://py4e-data.dr-chuck.net/comments_726710.json"
url = urllib.request.urlopen(serviceurl)
data = url.read().decode()
info = json.loads(data)
i = 0
for items in info["comments"]: i+=int(items["count"])
print(i)
# Getting the location and the place id from the json file format of dr.chuck - Geojson api
import json, urllib.request, urllib.parse, urllib.error
target = 'http://py4e-data.dr-chuck.net/json?' # The replacement of google api
local = input('Enter location: ') # The address that we aim to search for
url = target + urllib.parse.urlencode({'address': local, 'key' : 42}) # urlencoding the url with geojson api along with key and the address that we want to look for
print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data) # Reading the json file
print(json.dumps(js, indent = 4)) # Printing the json file that we received from the url
print('Place id', js['results'][0]['place_id']) # textual identifier that uniquely identifies a place as within Google Maps.