import os
freading = open('file1.txt', 'rt' )
poem = freading.read()
freading.close()
freco = open('file2.txt', 'wt')
print(poem, file=freco)
freco.close()
f= open('file2.txt', 'rt')
p = f.read()
print(p)
f.close()
path = 'file1.txt'
os.remove(path)

