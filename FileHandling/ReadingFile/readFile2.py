# f.read() reads the entire content of the file as a single string.
# f.readline() reads the first line of the file.
# f.readlines() reads all lines of the file and returns them as a list of strings.

f=open(r"C:\Users\siva\Desktop\DummyData\MOCK_DATA10.json","r")
content=f.read()
print(content)
f.close()

print("------------------------------------------------------------------------")
f=open(r"C:\Users\siva\Desktop\DummyData\MOCK_DATA10.json","r")
content=f.readline()
print(content)
f.close()

f=open(r"C:\Users\siva\Desktop\DummyData\MOCK_DATA10.json","r")
content=f.readlines()
print(content)
f.close()
