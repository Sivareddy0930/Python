# Internally,the object of the class will always call the last constructor if the class has multiple same constructors.
# The constructor overloading is not allowed in Python.

class Demo:
    def __init__(self):
        print("First constructor")

    # second constructor will override the first.
    # same with parameterized constructors also.
    def __init__(self):
        print("Second constructor")

d1=Demo()

# you can't have multiple methods with the same name in a class (unless you're using method overloading with a library like functools.singledispatch)