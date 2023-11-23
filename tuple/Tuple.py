# A tuple is a collection which is ordered,unchangeable and allow duplicates.
# so adding and remove is not possible in tuple

tup=(1,2,3,4,"siva",True,"siva",4.4444)
print(tup)

# tuple constructor
t1=tuple((1,"siva",4.4444,"siva",True))

print(t1)
print(type(t1))

# tuple with one item
l1=["siva"]
print(type(l1))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
t2=("Reddy",)
print(type(t2))#tuple

t2=("Reddy")
print(type(t2))#str

# String to Tuple
string1="siva"
t3=tuple(string1)
print(t3)

# using Asterisk *

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.

# tuple
t1=("siva","reddy",1,2,3,4,4,3,2,1,True,4.4444)
(firstName,lastName,*values)=t1
print(firstName)
print(lastName)
print(values)

