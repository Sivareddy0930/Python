# single Level Inheritance
class A:
    def feature1(self):
        print("This is Feature 1")

    def feature2(self):
        print("This is Feature 2")


class B(A):
    def feature3(self):
        print("This is Feature 3")

    def feature4(self):
        print("This is Feature 4")


b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()