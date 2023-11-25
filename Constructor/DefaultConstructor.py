# constructor which is not declared in class. that is provided by python itself for creation of object and its  attributes or variables initalization purpose

class Demo:
    name="siva"
    age=22
    # Here default constructor is added automatically
    def m1(self):
        print(self.name,self.age)
d1=Demo()
d2=Demo()
d1.m1()