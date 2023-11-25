from array import *

vals=array('i',[])
sizeOfArray=int(input("enter Size of an Array:"))

for x in range(sizeOfArray):
    value=int(input("enter value:"))
    vals.append(value)
print(vals)

# Searching index of element in an array

findElement=int(input("which element you want:"))

index=0
for x in vals:
    if findElement==x:
        break
    index +=1
print(index)

# using in built method

print("index =",vals.index(40))

