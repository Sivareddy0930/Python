# ConstructorWithMultiLevelInheritance
class A:

    def __init__(self):
        print("A class Constructor")
    def feature1(self):
        print("This is Feature 1")
class B(A):
    def __init__(self):

        print("B class Constructor")
    def feature2(self):
        print("This is Feature 2")

class C(B):
    def __init__(self):
        #  Method resolution Order
        # based on nearest inherited class   Ex:- C(B)   here B is nearest
        super().__init__()
        print("C class Constructor")
    def feature3(self):
        print("This is Feature 3")

c1=C()