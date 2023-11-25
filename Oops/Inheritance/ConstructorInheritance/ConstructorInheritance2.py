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

b1=B()
# child class constructor is called.