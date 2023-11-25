# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name
# that can be executed on many objects or classes.

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
#
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()

class Car:
    def move(self):
        print("car is moving")
class Boat:
    def move(self):
        print("Boat is moving")
class Plane:
    def move(self):
        print("Plane is moving")

c=Car()
b=Boat()
p=Plane()

for vehical in (c,b,p):
    vehical.move()
 # However, notice that we have not created a common superclass or linked the classes together in any way. Even then,
# we can pack these three different objects into a tuple and iterate through it using a common vehical variable. It is possible due to polymorphism.