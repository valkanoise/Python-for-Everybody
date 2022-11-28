# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#importo Urlib para poder ingresar archivos desde la web
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

all_links = list() #lista para guardar los links
url = input('Enter Url: ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

#defino posición y repetición
ipos = input('Position: ')
pos = int(ipos)
irep = input('Repeat: ')
rep = int(irep)


count = 1
while count <= rep: #acá va variable rep, lo hace la cantidad de repeticiones deseada
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser') #captura los elementos del html
    tags = soup('a') #se captura en tags todos los links de la web entre <a> y </a>
    for tag in tags:
        link = tag.get('href', None)
        all_links.append(link)
    url = all_links[pos - 1] #acordarse que la lista empieza en 0, por eso se resta 1 a la posicion deseada
    name = re.findall('by_([^ ]+).html', url) #extrae solamente el nombre con expresión regular
    print(name)
    count = count + 1
    all_links.clear() #borra la lista
        



    
                 