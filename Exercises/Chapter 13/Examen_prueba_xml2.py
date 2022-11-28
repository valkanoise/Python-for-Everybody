import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
if len(url) < 1 : url = ('http://py4e-data.dr-chuck.net/comments_42.xml')
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

for i in tree:
    for a in i:
        for b in a:
            print(b)