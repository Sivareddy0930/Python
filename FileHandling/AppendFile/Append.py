# Append (‘a’): Opens the file for writing, creating it if necessary.
# The handle is positioned at the end, allowing data to be inserted after existing content.
# it will not override the data.it append the data .
# The file pointer exists at the end of the previously written file if exists any.

f=open("Data1",'a')
# already some data is there in Data1 file.

f.write("\n newly added data ")

f.close()


# _________________________________
list1=["\n siva \n","reddy \n","tumu \n","venkata"]
f=open("Data1",'a')
# already some data is there in Data1 file.

f.writelines(list1)

f.close()

