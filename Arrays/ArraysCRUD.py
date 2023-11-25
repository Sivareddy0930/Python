import array as arr
vals=arr.array('i',[10,20,30,40])

# add elements

vals.append(50)
print(vals)
vals.insert(1,100)
print(vals)

vals1=arr.array('i',[100,200,300,400])

# vals=vals+vals1
vals.extend(vals1)
print(vals)

print("----------------------------------------")
# update

vals[0]=1000
print(vals)

print("----------------------------------------")

# delete
del vals[1]
print(vals)

vals.remove(1000)
print(vals)

vals.pop(6)
print(vals)

vals.pop()
print(vals)


print("----------------------------------------")

# read

print(vals[0])


print("----------------------------------------")
