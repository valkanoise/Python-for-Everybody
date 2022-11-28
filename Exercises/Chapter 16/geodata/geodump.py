import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0

#va fila por fila de la base de datos: row[es el lugar] y row[1] es la geodata en JSON
for row in cur :
    data = str(row[1].decode()) #miramos la geodata
    try: js = json.loads(str(data)) #hace un parse y string del JSON
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "") #le saca las comillas simples ' mediante reemplazo
    try :
        print(where, lat, lng)

#acá empieza a crear el archivo where.js con los datos limpios para ingresar al html
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

