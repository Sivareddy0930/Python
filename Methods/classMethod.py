class Demo:
    # static or class variable
    college="parul"
    def __init__(self,name,age):
        # instance Variables
        self.name=name
        self.age=age

    @classmethod
    def classMethod(cls):
        cls.college="university"

        # we cannot access instance variables in class methods
        print(cls.college)


d1=Demo("siva",22)
d2=Demo("vamsi",17)

d1.classMethod()

d2.classMethod()
