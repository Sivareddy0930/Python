# Encapsulation is process of wrapping variables and methods into a single unit.
# by using encapsulation we can achieve dataHiding and Abstraction
# data hiding can be done by using access modifiers like private ,protected,public.

class Vehical:
    def __init__(self,wheels):
        self._company="Tata"
        self._wheels=wheels#protected instance variable---------------it access with in class and in derived class.
                             # protected variables can access inside class and  in derived class also

class Car(Vehical):
    def __init__(self,wheels):
        super().__init__(wheels)
        print(self._company)

c=Car(4)

