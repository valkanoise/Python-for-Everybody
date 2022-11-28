name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
emails = list()

for line in handle:
    if line.startswith("From: "):
        words = line.split()
        emails.append(words[1])
    
for sender in emails:
    counts[sender] = counts.get(sender,0) + 1

who = None
sent = None

for sender,count in counts.items():
    if who is None or count > sent:
        who = sender
        sent = count

print(who,sent)