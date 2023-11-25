class Demo:
    name="siva"
    age=22

    # for every object creation constructor is called automatically
    def __init__(self):
        print("NoArg constructor")
    def m1(self):
        print(self.name,self.age)
d1=Demo()
d2=Demo()
d1.m1()