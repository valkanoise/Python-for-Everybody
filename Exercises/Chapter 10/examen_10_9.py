name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hcount=dict()
for line in handle:
    if not line.startswith("From "): continue
    horario=line.split()[5] #primer split y selecciono la h:m:s en posicion 5
    hora=horario.split(':')[0] #segundo split con ':' como condicion de split y selecciono solamente h
    hcount[hora]=hcount.get(hora,0)+1 #armo el diccionario a medida que aparecen las hora y las suma

#print(hcount.items())
ordenado=sorted(hcount.items())

for h,n in ordenado: #dos variables de iteración en diccionario hhcount que está ordenado de menor a mayor
    print(h, n)
