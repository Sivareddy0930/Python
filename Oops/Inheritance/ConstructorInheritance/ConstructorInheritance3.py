# while you create child object to get child class and parent class constructor.
# we use super()
class A:

    def __init__(self):
        print("A class Constructor")
    def feature1(self):
        print("This is Feature 1")
class B(A):
    def __init__(self):
        super().__init__()
        print("B class Constructor")
    def feature2(self):
        print("This is Feature 2")

b1=B()