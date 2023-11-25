
class Demo:
    # static or class variable
    college="parul"
    def __init__(self,name,age):
        # instance Variables
        self.name=name
        self.age=age

    def instanceMethod(self):
        self.college="myclg"
        print(self.name,self.age,self.college)

    def m1(self):
        print(self.college)


    @classmethod
    def m2(cls):
        print(cls.college)


d1=Demo("siva",22)
d2=Demo("vamsi",17)

d1.instanceMethod()
d1.m1()
d1.m2()
d2.instanceMethod()
d2.m1()
d1.m2()