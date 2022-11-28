# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

all_links = list()
count = 1
url = "http://py4e-data.dr-chuck.net/comments_436658.xml"
pos = int(18)

while count < 8:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        link = tag.get('href', None)
        all_links.append(link)
    url = all_links[pos - 1]
    name = re.findall('by_([^ ]+).html', url)
    print(name)
    count = count + 1
    all_links.clear()
        



    
                 