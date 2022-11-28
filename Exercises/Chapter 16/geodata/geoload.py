import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

#acá de cargan los datos de la Key de Google (si se tienen)
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

#si no hay Key de google usa el sitio de Chuck
if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

#se crea la base de datos si no existe
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

#Crea la tabla Locations y los campos address y geodata
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#abre el archivo con distintos lugares, incluida mi dirección "Los incas y triunvirato"
fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break
#para cada linea del archivo saca los espacios de ambos lados y el /n y lo asigna en address
    address = line.strip()
    print('')
#aca selecciona los datos (JSON) de geolocalización de cada dirección de where.data  
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))
#aca chequea si la data de geolocalizacion (JSON) previamente seleccionada está en la base de datos
#si está vuelve a empezar el loop    
    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
#si la data (json) no está sigue con el script = pass
    except:
        pass

#para las address que no están en la db encodea y arma el link para pedir la geodata a la api de Google
    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

#abre la información de geolocalizacion obtenida para cada nueva address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

#abre el archivo json son recibido,si no tira error el JSON esta OK
# si tira error, con expcept se imprime para ver qué paso
    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

#chequea que el haya un JSON, que tenga status OK y que tenga resultados
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

#inserta los datos recibidos de google en la database, el lugar y la geodata en JSON
    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
