# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the
# same name that can be executed on many objects or classes.

# Polymorphism With class Inheritance

#  the child classes in Python also inherit methods and attributes from the parent class.
#  We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.

# Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

class Vehicle:
    def __init__(self, Brand, wheels):
        self.Brand = Brand
        self.wheels = wheels

    def move(self):
        print("Vehicle Move")


class Car(Vehicle):
    def move(self):
        print("Car is Moving")

class Bike(Vehicle):
    pass

class Bus(Vehicle):
    def move(self):
        print("Bus is Moving")



c=Car("tata",4)
b=Bike("Bajaj",2)
bus=Bus("Mahindra",6)

c.move()
print(c.Brand,c.wheels)
b.move()
print(b.Brand,b.wheels)
bus.move()
print(bus.Brand,bus.wheels)




