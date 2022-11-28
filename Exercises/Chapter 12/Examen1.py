# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = ('http://py4e-data.dr-chuck.net/comments_498967.html')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span') #busca el contenido dentro del tag <span>
suma=0
count=0
for tag in tags:
# Look at the parts of a tag
#    print('Contents:', tag.contents[0]) #imprime el contenido del tag
    num=int(tag.contents[0]) #integra el nro del tag
    suma= suma+num
    count=count+1

print('Count', count)
print('Total', suma)
    

