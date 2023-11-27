
f=open('data4','w+')
f.write("looking for  a job ")

# after writing cursor is at end.
# Move the file pointer to the beginning
f.seek(0)

content=f.read()
print(content)
f.close()
