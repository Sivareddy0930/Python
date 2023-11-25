# Default arguments

def fun1(a,b,c=20):
    return a,b,c
print(fun1(10,30))
print(fun1(1,2,3))

print("---------------------------------------")
# position Arugments
def fun2(a,b):
    return a,b
print(fun2(10,30))

print("------------------------------------------")
# Keyword Arguments
# Calling function and passing arguments using keyword
print(fun2(b=1,a=2))


print("---------------------------------------")
# Keyword Arguments
def fun2(a,b):
    return a,b
print(fun2(10,30))

# Calling function and passing arguments using keyword
print(fun2(b=1,a=2))


print("-----------------------------------------------------")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#
# This way the function will receive a tuple of arguments.

def fun(a,b,*c):
    print(a)
    print(b)
    print(c)
fun(1,2,3,4,5,6,7,8,9,)

print("-------------------------------------")
#
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#
# This way the function will receive a dictionary of arguments

def funz(**args):
    print(args["fName"])
    print(args["age"])
    print(args)
funz(fName="Tumu",lName="reddy",mname="venkata siva",age=22)