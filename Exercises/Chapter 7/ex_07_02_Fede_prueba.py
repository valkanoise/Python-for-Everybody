# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count=0
total=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(':')
    val=line[pos+1:]
    fval=float(val)
    count= count+1
    total= total+fval
    
print("Average spam confidence:", total/count)