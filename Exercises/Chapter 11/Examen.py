name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_498965.txt"
handle = open(name)

import re
numlist=list()
for line in handle:
    line=line.strip()
    stuff=re.findall('[0-9]+',line)
    if stuff == [] : continue #descarto las líneas vacías
    
#uso for para cuando hay másde un valor por línea y poder separarlos y sumarlos inidividualmente a la lista numlist        
    for item in stuff: #en aquellas líneas que hay más de un valor o más las separo y transformo a INT
        item=int(item)
        numlist.append(item)

      
  
#ahora cuento los nros y los sumo para clacular el total
count=0    
suma=0
for i in numlist:
    count=count+1
    suma=suma+i
    
#Para sumar todo se podría usar la función sum()
#total=sum(numlist)
#print(total)
    
print('The sum of',count,'number is',suma)

