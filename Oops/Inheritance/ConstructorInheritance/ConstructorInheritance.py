class A:

    def __init__(self):
        print("A class Constructor")
    def feature1(self):
        print("This is Feature 1")
class B(A):
    def feature2(self):
        print("This is Feature 2")


# if your parent class has constructor and child class doesnt then while you create a child class object then it will call parent class constructor.
# because child class doesnt have constructor.so parent class constructor is called.
# if both classes have constructor and we created a child object .then only child constructor is called.

b1=B()