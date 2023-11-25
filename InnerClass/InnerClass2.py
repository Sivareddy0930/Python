class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def studentDetails(self):
        print(self.name,self.age)


    # inner class

    class Computer:
        def __init__(self):
            self.company="ASUS"
            self.cpu="i5"
            self.ram="8GB"

        def computerDetails(self):
            print(self.company,self.cpu,self.ram)


s1=Student("siva",22)
s2=Student("vamsi",17)

s1.studentDetails()
s2.studentDetails()

# creating object of inner class outside the outer class  by using outer class name
comp=Student.Computer()
# accessing inner class details
comp.computerDetails()

