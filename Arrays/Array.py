# arrays in python used to store same kind of data.
# array in python are dynamic in size.
# array(typecode,list of elements)
# typecode represent datatype of an array.
# to use array in python we have import array module

from array import *

vals=array('i',[1,2,3,4,5,1])
print(vals)
print(type(vals))#<class 'array.array'>
print(len(vals))

# buffer_info() provide address of an array and its size.
print(vals.buffer_info())#(1962057111856, 6)

print(vals.count(1))# it counts number of 1 are there in array.

print(vals.typecode)#type of data stored is 'i'

print("---------------------------------------------------------------------")
# copy array

vals1=vals
print(vals1)

vals2=vals.__copy__()
print(vals2)