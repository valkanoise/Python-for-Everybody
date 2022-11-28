name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

#se arma una lista con los emails
lst = list()
for line in handle:
    if not line.startswith("From "): continue
    line=line.split()
    lst.append(line[1]) #agrega los emails a la lista lst
# print(lst) imprime la lista final
    
 #se arma el diccionario con los emails y la cantidad de envios   
emcount = dict()
for word in lst:
    emcount[word] = emcount.get(word,0)+1
#print(emcount.items()) #imprime el diccionario final

#para buscar el emisor que más emails envió
bigcount = 0#empty at beginning
bigword = None
for word,count in emcount.items():
    if count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)