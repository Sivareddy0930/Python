
r=open(r'E:\Python\FileHandling\ReadingFile\MyImage.jpg','rb')

content =r.read()

with open('showMyImage.jpg','wb') as f:
    f.write(content)
f.close()
