# Write only (‘w’): Opens the file for writing, overwriting existing data if the file already exists.
# The handle is set at the beginning of the file, and a new file is created if none exists.

f=open('data1','w')
# f.write("i am siva \n")
# f.write("And i am from Ap ")
f.write("looking for  a job ")
f.close()

print("-------------------------------------")
f=open('data2','w')
f.write("looking for  a job ")
f.write(('some  Data'))
f.close()

print("-------------------------------------")
# overriding existing data from data2 file
f=open('data2','w')
f.write("some data")
f.write(('looking for  a job '))
f.close()

print("-------------------------------------")
list=["siva \n","reddy \n","tumu \n","venkata \n"]
f=open('data3','w')
f.writelines(list)
f.close()


print("-------------------------------------")
list=["siva \n","reddy \n","tumu \n","venkata \n"]
# it replace all data with this values.
f=open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.json','w')
f.writelines(list)
f.close()