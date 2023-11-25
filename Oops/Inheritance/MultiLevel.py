# MultiLevel Inheritance
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

class C(B):
    def feature5(self):
        print("This is Feature 5")




c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()