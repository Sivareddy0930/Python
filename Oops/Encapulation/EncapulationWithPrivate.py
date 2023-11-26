# Encapsulation is process of wrapping variables and methods into a single unit.
# by using encapsulation we can achieve dataHiding and Abstraction
# data hiding can be done by using access modifiers like private ,protected,public.

class Car:
    def __init__(self,engine):
        self.__engine=engine#private instance variable-----------it access only with in class.
        # private variables can access inside class and  outside also by using
        # Public method or getter methods to access private members
        # Name Mangling to access private members


    def publicMethod1(self):
        print("accessing private date from public method or getter method ",self.__engine)

c=Car("v8 disiel")

c.publicMethod1()

print(c._Car__engine)#Name Mangling
