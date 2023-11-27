
f=open("data1","r")
content=f.read()
print(content)

f.close()

print("--------------------------------------------------------------")
#  using with statement.

with open("data1","r") as f1:
    content=f1.read()
    print(content)
f1.close()

print("--------------------------------------------------------------")

# in Python, you need to use either double backslashes or a raw string (prefixing the string with r) to avoid the escape character issue

# reading csv file

with open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.csv','r') as f1:
    content=f1.read()
    print(content)
f1.close()

print("--------------------------------------------------------------")
# reading json file

with open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.json','r') as f1:
    content=f1.read()
    print(content)
f1.close()

print("--------------------------------------------------------------")
# reading json file with specified no.of characters.

with open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.json','r') as f1:
    content=f1.read(10)
    print(content)
f1.close()

print("--------------------------------------------------------------")
# reading json file first line

with open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.json','r') as f1:
    content=f1.readline()
    print(content)
f1.close()

print("--------------------------------------------------------------")
# reading json file first line

with open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.json','r') as f1:
    content=f1.readline()
    print(content)
f1.close()


print("--------------------------------------------------------------")
# reading json file using looping

with open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.json','r') as f1:
    for i in f1:
        print(i)
f1.close()

