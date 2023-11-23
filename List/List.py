# List is a collection which is ordered and changeable. Allows duplicate members.

l=[1,"siva",4.4,"siva",True]
print(l)

# List Constructor

myList= list((1,1,"siva",True,"Siva",4.4444))
print(myList)

# String to list

s="siva"
s1=list(s)
print(s1)

# indexing

print(myList[2])
print(myList[-1])

#splitting

print(myList[2:])
print(myList[:4])
print(myList[-4:-1])

# in keyWord

print("siva" in myList)

if 4.4444 in myList:
    print("avaliable")


# change list item or replace

list1=["apple","banana","cherry","watermelon","berry","curry"]

list1[1]="pomogranate"
print(list1)

list1[2:4]=["aurry","burry"]
print(list1)

list1[1:3]=["zurry"]
print(list1)




# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

list1.insert(0,"melon")

print(list1)


# CRUD operations

# append()

list2=["a","b","c","d"]
list2.append("e")
print(list2)

# insert()

list2.insert(1,"z")
print(list2)

#extend()  it add another list,tuple,set to current list

list1.extend(list2)
print(list1)

tuple=(1,2,3,4)

list1.extend(tuple)
print(list1)

# Deleting

list3=["apple","banana","carrot","cherry","banana","purry","zurry"]

list3.remove("banana")#it remove first occurence of specified element
print(list3)

list3.pop() # it remove last element
print(list3)

list3.pop(1) # it remove specifed indexed elemet
print(list3)

del list3[0] # it remove specifed indexed elemet
print(list3)


# del list3 # it delete all list itself
# print(list3)

list3.clear()# it remove all elements of list but not list.
print(list3)