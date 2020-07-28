# Using the socket method
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # It makes the socket
mysock.connect(('data.pr4e.org', 80)) # It forms a connection between the socket to the server
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # \n\n can also be used for this
mysock.send(cmd) # Socket connection consisits of sending and receiving the info, send requests made to be sent before to establish a relation
while True:
    data = mysock.recv(512)
    if (len(data) < 1) : break
    print(data.decode(),end='') # To print the data received it needs to be decoded
mysock.close() # Final step is closing of socket
# Using urlib for the same
import urllib.request, urllib.parse, urllib.error, ssl
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # it does all the steps from making a socket, forming a connection, send info and receiving and closing too
for line in fhand : print(line.decode().strip())
# Printing the word count from a website
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words : counts[word] = counts.get(word, 0) + 1
print(counts)
# Using Beautiful Soup and bypassing SSL security patch and taking out numbers in a table from the web and doing a sum of the numbers so obtained
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen("http://py4e.data.dr-chuck.net/comments_726707.html", context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup("span")
sum = 0
for tag in tags : sum += int(tag.contents[0])
print(sum)
# Jumping through the links
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input()
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
href = soup('a')
for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
# Using Element Tree
import xml.etree.ElementTree as ET
data = '''<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''
tree = ET.fromstring(data) # fromstring() reads the XML file and checks its syntax
print('Name:',tree.find('name').text) # This finds the text include with the tag
print('Attr:',tree.find('email').get('hide')) # This finds the attribute within the tags
# findall() creates a tree like structure (a list) of the text and attribute node within the tags
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
# Using the json package
import json
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''
info = json.loads(data) # loads() converts the json file into readable text format
print('Name:',info["name"]) # info returns the text within the tag
print('Hide:',info["email"]["hide"]) # Getting into subfolders can be done as follows
# Downloading images from google search for datasets using python script - Web Scraping Hack
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"Crops", "limit":9,'print_urls':True}
paths = response.download(arguments)
print(paths)