class Demo:
    # static or class variable
    college="parul"
    def __init__(self,name,age):
        # instance Variables
        self.name=name
        self.age=age

    @staticmethod
    def staticMethod(x,y):
        #     we can't access static(class) variables and instance variables here.
        print(x+y)

d1=Demo("siva",22)
d2=Demo("vamsi",17)

d1.staticMethod(2,2)

d2.staticMethod(4,4)
