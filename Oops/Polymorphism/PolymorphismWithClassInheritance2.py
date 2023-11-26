#due to inheritance  all variables ,functions and constructors are avaliable in child class
class Vehicle:
    s="siva"
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
    print(Vehicle.s)
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

print(bus.s)


