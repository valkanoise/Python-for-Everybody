import urllib.request

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
for line in fhand:
    print(line.decode().strip())
