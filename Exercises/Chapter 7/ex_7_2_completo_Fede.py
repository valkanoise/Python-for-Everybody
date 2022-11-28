#fname=input('Enter a file name: ')

#try:
#    handle=open(fname)
#except:
#    Print('Invalid file name',fname)
#    quit()

handle = open('mbox-short.txt')

count=0
suma=0
for line in handle:
    line=line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        pos=line.find(':')
        val = float(line[pos+2:])
        suma=suma+val
        print(line, 'Valor=', val)
        
print('Total=',count, 'Suma=',suma, 'Promedio=', suma/count)


