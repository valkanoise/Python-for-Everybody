import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#se ingresa la dirección del xml
url = input('Enter location: ')
if len(url) < 1: url = ('http://py4e-data.dr-chuck.net/comments_42.json')
print('Retrieving', url)

#se abre el xml y se convierte en string con read()
output = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(output), 'characters')

#creamos el objeto con los datos del Json
info = json.loads(output)
#organizamos el json para poder verlo prolijo y analizarlo
#print(json.dumps(info,indent=4))
# se puede ver que el json tiene un diccionario {note: blabla , comments: [{dic1, dic2, ....dicN]]]

suma=0
cantidad=0
for item in info['comments']:
    name = item['name']
    count = item['count']
    cantidad=cantidad+1
    suma=suma+int(count)

print('Count',cantidad)
print('Sum',suma)
    
    