score = input("Enter Score: ")

try:
    s=float(score)
except:
    print('Bad Score')
    quit()

if s>=0.0 and s<=1.0:
    if s>= 0.9:
        print("A")
    elif s>= 0.8:
        print('B')
    elif s>= 0.7:
        print('C')
    elif s>= 0.6:
        print('D')
    elif s< 0.6:
        print('F')

else:
    print('Bad Score')
    quit()


