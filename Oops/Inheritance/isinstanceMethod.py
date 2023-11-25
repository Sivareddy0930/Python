# The isinstance() method is used to check the relationship between the objects and classes.
# It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.


class A:
    def feature1(self):
        print("This is Feature 1")

    def feature2(self):
        print("This is Feature 2")


class B:
    def feature3(self):
        print("This is Feature 3")

a1=A()
b1=B()

print(isinstance(b1,B))#True
print(isinstance(b1,A))#False