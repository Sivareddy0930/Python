# difference() Return a set that contains the items that only exist in set x, and not in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# difference() method return new set with values
z=x.difference(y)
print(z)#{'banana', 'cherry'}


#difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# difference_update() method update the specified set.with values

x.difference_update(y)
print(x)#{'banana', 'cherry'}


# intersection() means it returns matched items from both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.intersection(y)
print(z)#{'apple'}

# intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)#{'apple'}

#symmetric_difference() is used to find the values that are not matched from both sets and return new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.symmetric_difference(y)
print(z)#{'banana', 'microsoft', 'google', 'cherry'}

#symmetric_difference_update() is used to find the values that are not matched from both sets and update current set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(z)#{'banana', 'microsoft', 'google', 'cherry'}


# union()  used to combine two sets and return new set.it is same as update() method.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.union(y)
print(z)#{'cherry', 'banana', 'apple', 'microsoft', 'google'}

# isdisjoint()  Returns whether two sets have a intersection or not
# issubset()    Returns whether another set contains this set or not
# issuperset()  Returns whether this set contains another set or not




