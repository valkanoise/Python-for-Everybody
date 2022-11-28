#fname = input("Enter file name: ")
#fhandle=open(fname)
fhandle=open('mbox-short.txt')

count=0
for line in fhandle:
    if not line.startswith("From "): #agarra todos los FROM y FROM: (con y sin :)
        continue
    line=line.split()
    line=line[1]
    print(line)
    count=count+1

print("There were", count, "lines in the file with From as the first word")






