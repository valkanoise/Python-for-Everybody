score = input("Enter Score: ")

try:
    s1=float(score)
except:
    print('Bad Score')
    quit()


def computegrade(s):
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


computegrade(s1)