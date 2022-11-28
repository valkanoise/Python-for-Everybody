name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_498965.txt"
handle = open(name)

import re
print( sum( [int(i) for i in  re.findall('[0-9]+',handle.read()) ] ) )

#seria imprimir la suma de nros enteros i para todos aquellos nros enteros
#edncontrados dentro del archivo handle al leerlo completamente.