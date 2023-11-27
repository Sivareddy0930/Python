"""
 Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
 """

 #String
a="siva"
b='siva learning python'
c="""Siva is going to learn machine learning
     in comming  days. """

print(a)
print(b)
print(c)

print( a+" "+b)
print(a," ",b)
print(a*2)

#Numeric type

a=100000000
b=4.4444
c=4.0+4j

print(a,b,c)

# isinstance(object,className)

print(isinstance(c,complex))


# Sequence type

list=[1,"siva",4.4,True,4j]
print(list)

tuple=("siva",100,1000.9999,100j,True)
print(tuple)

ran=range(9)
print(ran)

# mapping type

dict={"name":"siva",'age':22}
print(dict)

# set Types

set={"siva",1,"siva",True,4j,4.4}
print(set)

frozenset=frozenset({"siva",1,1,1,4.4,True})
print(frozenset)

# Boolean type

Bool=True
print(Bool)

# None type
x=None
print(x)

