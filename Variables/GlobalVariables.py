a=10

def m1():
    # it is local variable a
    a=20
    print(a)
m1()
print(a)

print("----------------------------------")
# if we want to use global variable in a funtion that is update in function.we have to use global keyword .

a=10

def m1():
    # it is global variable a
    global  a
    a=20
    print(a)
m1()
print(a)

print("----------------------------------")
# i want to use global variables and local variables in a funtion that have same variable name have to use global keyword .

a=10
b=4
def m1():
    # local variable a
    a=1000
    print("local variable a:",a)

    # to get all local variables in function  for mainupliation purpose .we use globals() to get all variables.

    x=globals()['a']
    print("global variable a as x:",x)

m1()
print(a)

print("----------------------------------")
# i want to use global variables and local variables in a funtion that have same variable name have to use global keyword .

a = 10
b = 4


def m1():
    # local variable a
    a = 1000
    print("local variable a:", a)

    # to get all local variables in function  for mainupliation purpose .we use globals() to get all variables.

    x = globals()['a']
    print("global variable a as x:", x)


# if we want to update global variable inside a function that has a variable with same name as global.
# we can update following way.

    y=globals()['a']=100
    print("updated global variable a as y:", y)

m1()
print(a)