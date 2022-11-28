fname = input('Filename: ')
fhand = open(fname)
#fhand = open('romeo.txt')

palabra=list() #defino una variable tipo lista y vacia

for line in fhand: #para cada linea dentro del archivo...
    words=line.split() #separo cada linea en una lista de palabras (words)
    for i in words: #para cada una de las palabras de cada linea...
        if palabra==None or not i in palabra: #si la palabra no esta en "palabra"la agrega
            palabra.append(i)

palabra.sort() #organiza las palabras de la lista
print(palabra)

