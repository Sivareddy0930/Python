# ConstructorWithMultipleInheritance
class A:

    def __init__(self):
        print("A class Constructor")
    def feature1(self):
        print("This is Feature 1")
class B:
    def __init__(self):

        print("B class Constructor")
    def feature2(self):
        print("This is Feature 2")

class C(A,B):
    def __init__(self):
        #  Method resolution Order
        # based on nearest inherited class
        # it move from left to right Ex:- C(A,B)   here A is nearest and moving from left to right.
        super().__init__()
        print("C class Constructor")
    def feature3(self):
        print("This is Feature 3")

c1=C()