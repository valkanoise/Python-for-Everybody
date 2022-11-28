count = 0
total = 0

while True:
    num = input("Enter a number: ")
    if num == "done": 
        break
    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + inum
    

print(total, count, total/count)
