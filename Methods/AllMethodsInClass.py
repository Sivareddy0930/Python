# Class method vs Static Method
# The difference between the Class method and the static method and instance method is:
#
# A class method takes cls as the first parameter while a static method needs no specific parameters and instance method take self as first parmeter.
# Instance methods can access and modify both class attributes and instance attributes.
# A class method can access or modify the class(or) static variables but not instance variables.
#  static methods cannot accessor modify class attributes or instance attributes.
# Static methods have no implicit first argument. Neither cls nor self is passed as the first argument.
# Static methods are just functions that you can call from the class or instance of the class.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

# When to use the class or static method?
# We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
# We generally use static methods to create utility functions.


class Demo:
    # static or class variable
    college="parul"
    def __init__(self,name,age):
        # instance Variables
        self.name=name
        self.age=age
        print("constructor")

    def instanceMethod(self):
        print(self.name,self.age)
        print("This is instance method belongs to Objects of a class")

    @classmethod
    def classMethod(cls):
        print("This is class method belongs to class")

    @staticmethod
    def staticMethod():
        print("This is static method belongs to a class")

d1=Demo("siva",22)

d1.instanceMethod()
d1.classMethod()
d1.staticMethod()