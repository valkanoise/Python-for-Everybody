name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt" #no pongo nada y abre el archivo
handle = open(name)

emcount = dict() #creo el diccioanrio
for line in handle:
    if not line.startswith("From "): 
        continue #selecciono lines con "From "sin dos puntos
    x = line.split() # cada linea se separa en palabras
    x = x[1] # tomo sólo la palabra en la segunda posición = emisor email
    emcount[x] = emcount.get(x, 0) +1 #arma el diccionario con emails y su conteo
#print(emcount.items()) #imprime el diccionario finalizado/completo
    

#para buscar el emisor que envió más emails
bigcount = None #defino variale vacia
bigword = None #defino variable vacia
for word,count in emcount.items(): #iteración dos variables en simultáneo: word(key) y count(valore del key)
    if bigcount == None or count > bigcount: #busca el emisor que envió más emails
        bigcount = count #busca el mayor nro de envios 
        bigword = word #asigna a bigword aquel email con mayor nro de envios
print(bigword, bigcount)


