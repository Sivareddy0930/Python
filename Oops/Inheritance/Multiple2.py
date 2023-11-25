# Multiple Inheritance with Method Resolution order
class A:
    def feature(self):
        print("This is Feature of class A")


class B:
    def feature(self):
        print("This is Feature of class B")


#    Method Resolution order is applied from left to right
class C(A, B):
    # class C(B,A):
    def m1(self):
        super().feature()  # A class method is called
        print("m1() of class C")


c1 = C()
c1.m1()
