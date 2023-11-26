# Method Overriding allows us to change the implementation of a function in the child class which is defined in the parent class.

class A:
    def func1(self):
        print("A class func1")

    def func2(self):
        print("A class func2")


class B(A):
    def func1(self):
        print("B class func1")

b=B()
b.func1()