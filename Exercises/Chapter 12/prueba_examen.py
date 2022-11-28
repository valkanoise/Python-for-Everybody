import urllib.request

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')
for line in fhand:
    print(line.decode().strip())
