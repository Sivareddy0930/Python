
from abc import ABC,abstractmethod
# abc === abstract base class
class Myclass(ABC):


    @abstractmethod
    def m1(self):
        print(" It's simply a placeholder or default implementation to give some information about the intended purpose of the method.  ")
        pass

class child(Myclass):
    def m1(self):

        print("child class implementation for abstract method")

class child2(Myclass):
    def m1(self):
        #  if we want to access the m1() function of the base class itself, we can use the object of the child class, but we will have to invoke it through super().
        super().m1()
        print("child2 class implementation for abstract method")

obj=child2()
obj.m1()
