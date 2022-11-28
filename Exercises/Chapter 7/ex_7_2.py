fname=input('Enter a file name: ')

try:
    handle=open(fname)
except:
    print('Invalid file name',fname)
    quit()

count=0
suma=0
for line in handle:
    line=line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        pos=line.find(':') #busco posicion de los :
        val = float(line[pos+2:]) #extraigo el valor desde line desde los :+2 posiciones hasta el final, lo hago float y asigno a la variable val
        suma=suma+val
                
print('Average spam confidence=', suma/count)


