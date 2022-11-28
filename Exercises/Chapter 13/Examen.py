import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#se ingresa la dirección del xml
url = input('Enter location: ')
if len(url) < 1: url = ('http://py4e-data.dr-chuck.net/comments_42.xml')
print('Retrieving', url)

#se abre el xml y se convierte en string con read()
output = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(output), 'characters')

#a partir del string de xml se arma el arbon con element Tree
tree = ET.fromstring(output)
# se crea un objeto que busca todos los tags comment que contienen name y count
comment = tree.findall('.//comment')
print('Count:', len(comment))

# se ingresa a cada comment y se busca el name y el count, se integra y se suman
suma=0
for i in comment:
    name = i.find('name').text
    count = int(i.find('count').text)
    suma = suma + count
print('Sum:',suma)