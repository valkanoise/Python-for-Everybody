import json
import sqlite3

#abre o crea una nueva base de datos
conn = sqlite3.connect('rosterdb.sqlite')
#abre la base de datos y crea un file handle
cur = conn.cursor()

# Do some setup
#Borra las 3 tablas si existe y crea 3 tablas nuevas con sus id y columnas
#executescript() permite ejecutar varios comandos SQL separados por ';' entre comandos
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

#se indica el json que se quiere ingresar
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

#estructura de los datos ingresados en el json
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

#se abre el json y se lee completamente
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2]

    print((name, title, role))

#para cada linea (entry) del json inserto su información en las tablas
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

# si el conn.commit() queda indexato graba en cada loop y tarda mucho si lo saco guarda al hdd cuando termina
#    conn.commit()
conn.commit()
    

