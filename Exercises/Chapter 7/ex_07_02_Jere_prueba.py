count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        line = line.split()
        if total == 0:
            total = float(line[1])
        else:
            total = float(line[1]) + total
print("Average spam confidence:",total / count)

