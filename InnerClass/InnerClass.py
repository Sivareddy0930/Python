class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.comp=self.Computer()
    #     object  of inner class inside outer class constructor

    def studentDetails(self):
        print(self.name,self.age)
        # accessing inner class details
        self.comp.computerDetails()
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


