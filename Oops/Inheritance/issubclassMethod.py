# The issubclass(sub, sup) method is used to check the relationships between the specified classes.
# It returns true if the first class is the subclass of the second class, and false otherwise.


class A:
    def feature1(self):
        print("This is Feature 1")

    def feature2(self):
        print("This is Feature 2")


class B:
    def feature3(self):
        print("This is Feature 3")

    def feature4(self):
        print("This is Feature 4")

class C(A,B):
    def feature5(self):
        print("This is Feature 5")




c1=C()

# issubclass(sub className,Super ClassName)
print(issubclass(C,A))#True
print(issubclass(B,C))#False