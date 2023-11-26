# abstraction is nothing but hiding implementation details and showing functionality.

# In python, we  can achieve abstraction by using abstract class and abstract methods.
# we can create abstract class by importing abc module and  from that ABC class and @abstractmethod decorator.
# we have to inherit ABC class from our class own class .and it consist of one or more abstract methods and any number of concreate methods .
#  an abstract class can have a constructor, class variables, and instance variables, just like any other class. However, an abstract class cannot be instantiated on its own.

from abc import ABC,abstractmethod
# abc === abstract base class
class Myclass(ABC):

    college="mycollege"
    def __init__(self,name):
        self.name=name
    # concreate method
    def about(self):
        print(self.name,self.college)

    # Abstract Method
    # to represent it is abstract method we use @abstractmethod decorator
    @abstractmethod
    def m1(self):
        pass

# must and should child classes of abstract class have to provide implementation for abstract methods. otherwise we get error.
# if we not provide implentaion for abstarct metods in impelemenation class .then that class is also consider as an abstract class.so that we cannot instatiate it.
class child(Myclass):
    def m1(self):
        print("child class implementation for abstract method")

obj=child("siva")
obj.about()
obj.m1()
