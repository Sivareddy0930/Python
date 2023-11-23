# List Comprehension is a shortest syntax when you want to create new List based on existing list.


list1=[1,20,3,40,5]
list2=[]
# find even numbers
for x in list1:
    if x%2==0:
        list2.append(x)
print(list2)

# using comprehension
# newlist = [expression for item in iterable if condition == True]
# expression is nothing but an outcome.
list3=[x for x in list1 if x%2==0]
print(list3)

#------------------------------------------------
# find words that consist letter "a"
l1=["apple","banana","cherry","aurry","berry"]

l2=[x for x in l1 if "a" in x]

print(l2)

#------------------------------------------

# create a list with values 10

l3=[i for i in range(10)]
print(l3)

#-------------------------------------------
# transform list items to uppercase
# we can do manipulation on expression
l4=["siva","appple","banana","cherry"]

l5=[x.upper() for x in l4]
print(l5)

#---------------------------------------------
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
l6=["apple","banana","cherry","berry","melon"]
l7=[x  if x!="banana" else "orange" for x in l6]
print(l7)