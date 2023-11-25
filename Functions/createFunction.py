
def myfun():
    print("hi")

myfun()
#
def myfun():
    print("hii")
myfun()

#function with return statement
def myfun1():
    return "siva"
print(myfun1())

#function with return statement and paremeters
def myfun1(x,y):
    return x,y
print(myfun1("siva",4.4444))

print("-------------------------------")
def myfun1(s):
    return len(s)
print(myfun1("siva"))

print("-------------------------------")
def myfun1(s):
    return len(s)
print(myfun1("siva"))

print("-------------------------------")
def myfun1(x,y):
    z=x+y
    a=x-y
    return z,a

result1,result2=myfun1(10,6)
# Here we are getting two outputs so we have to store in two different variables.

print(result1,result2)



