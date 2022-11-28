file=input('Enter a file name: ')

try:
    handle=open(file)
except:
    Print('Invalid file name',file)
    quit()

count=0
for line in handle:
    line=line.rstrip().upper()
    print(line)
    count+1


