# Gross pay
inph=input('Hours?\n')
inpr=input('Rate?\n')

try:
    hrs=float(inph)
    rate=float(inpr)
    
except:
    print('Error, please enter numeric input')
    quit()

#si trabaja más de 40 cobra regular más 50% en las hs extra
if hrs>40:
    pay=hrs*rate+(hrs-40)*(rate*0.5)
 
#si trabaja 40 hs o menos cobra sueldo regular
else:
    pay=hrs*rate

print('Pay', pay)
