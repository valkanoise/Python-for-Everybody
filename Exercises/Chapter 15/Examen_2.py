import sqlite3

#abre la base de datos sql
conn = sqlite3.connect('domaindb.sqlite')
#cursor() es como hacer un handle de la base de datos
cur = conn.cursor() 

#si la base de datos existe la borra
cur.execute('DROP TABLE IF EXISTS Counts')

# crea una tabla con dos columnas: org y count
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#se ingresa el archivo con todos los mails y se mira linea por linea
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    remitente = pieces[1]
    dominio = remitente.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (dominio,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (dominio,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (dominio,))
        
#guarda los datos de la memoria en el archivo
conn.commit()

#selecciona las columnas, y ordena las 10 primeras y las pone en lineas
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

#va linea por linea del sql filtrado arriba
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
