# Method Overriding allows us to change the implementation of a function in the child class which is defined in the parent class.

# Method resolution order in Python is the order in which a python program resolves or searches for a class in case of multiple inheritance.
# It play's a crucial role for programs using multi-inheritance.
# In multi-inheritance a class is derived from more than one base class, hence inheriting all properties of the base class
# In this approach -> the method or attributes are first searched in the child class. If it is not present then the seraching moves a level up -- to the immediate parent class. And if again no luck, then the searching continues following the same search approach.
# It follows the depth-first search approach.

class A:
    def func1(self):
        print("A class func1")

    def func2(self):
        print("A class func2")


class B(A):
    def func1(self):
        print("B class func1")

class C(A):
    def func1(self):
        print("C class func1")

class D(C,B):
    # It follows the depth-first search approach.
    # B and C are in same Depth.
    pass
    # def func1(self):
    #     print("D class func1")

d=D()
d.func1()