# by default input() function take every input as string.
x=int(input("enter a number"))
y=int(input("enter a number"))
print(x+y)

# get a charcter
x=input("enter a char")
# x=input("enter a char")[0]
print(type(x))#str
print(x)
print(x[0])

# get expression as input  from user.
# we can done by using eval() function

z=eval(input("enter expression:- "))
print(z)
