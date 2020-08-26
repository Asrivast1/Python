# Jumping through the links
import urllib.request, urllib.parse, urllib.error, urllib, ssl
from bs4 import BeautifulSoup
# By passing the ssl security patch
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter the URL:") # Enter the url to be openend
count = int(input('Enter count:')) # Number of times the process is to be repeated
position = int(input('Enter position:'))-1 # Finding the link at the specified position
html = urllib.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
href = soup('a')
for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')