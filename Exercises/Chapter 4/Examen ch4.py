def computepay(h,r):
    if h>40:
        p=h*r+(h-40)*(r*0.5)
    else:
        p=h*r
    return p

ih = input("Enter Hours:")
h=float(ih)
ir = input("Rate per Hour:")
r=float(ir)

pay = computepay(h,r)

print("Pay",pay)