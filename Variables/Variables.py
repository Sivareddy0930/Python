from builtins import print

print("siva")
a=10
b=a;
print(type(a))
print(type(b))

print(id(a))
print(id(b))

b="siva"

print(b)
print(type(b))
print(id(b))

# A_Z,a-z,0-9, _
lastName="siva"
firstName='reddy'
print(type(firstName))

#---------------------------------------
# assigning multiple values to multiple variables

a=b=c=50
print(a,b,c)

# --------------------

a,b,c="siva",4.4,100

print(a,b,c)

# local variables and global variables

#local variables are limited scope with in the function only.

def localVariables():
    a=10;
    b="python"
    z=100
    # print(b+a+c)   #TypeError: can only concatenate str (not "int") to str
    # TypeError is an exception that occurs when the data type of an object in an operation is inappropriate.

    print(a+z)
localVariables()

# print(z)  NameError: name 'z' is not defined
# NameError: name 'x' is not defined error is raised when the program attempts to access or use a variable that has not been defined or assigned a value.

# Global variables

x=4

def globalVariables():

    # x=8
    print(x)
globalVariables()


#------------------------------------

y=400

y=200
def globalVariables2():


    global y
    print(y)

    y=800
    print(y)

globalVariables2()

print(y)

# ----------------------------------------------


t=True

print(t)
del t
# print(t) NameError: name is not defined.
