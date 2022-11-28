fhand = open('mbox-short.txt')

count=0
for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence'):
        print(line)
        count= count+1

print(count)