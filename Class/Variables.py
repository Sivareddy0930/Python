# instance variables and class(static)  variables are two types of variables in a class.

# instance variables are variables that are declared inside init method.
# class variables are declared outside init and inside class.

class car:
    # class or static variables

    wheels=4
    def __init__(self):
        # instance Variables
        self.company="BMW"
        self.milage="100kmph"

car1=car()
car2=car()
car1.company="Tata"
print(car1.company,car1.milage,car1.wheels)
print(car2.company,car2.milage,car2.wheels)
