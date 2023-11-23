
# Identity operators
# is ---->Returns True if both variables are the same object and at same address
# is not -----> Returns True if both variables are not the same object
# The is operator is used to check if two variables refer to the same object in memory.
# It compares the identity or memory address of the objects, not their values.
# It is often used to test if an object is None or to check if two variables reference the exact same object.

x=["apple","banana"]
y=["apple","banana"]
# content is same but address of bot x and y is different.
z=x

print(x is y)
print(x is z)
print(x==y)
print(x is not y)
print(x is not z)

# The == operator is used to check whether two values are equal.
# It compares the values of the objects, not their identity.
