# Encapsulation is process of wrapping variables and methods into a single unit.
# by using encapsulation we can achieve dataHiding and Abstraction
# data hiding can be done by using access modifiers like private ,protected,public.

class Vehical:
    def __init__(self,Wheels):
        self._Wheels=Wheels#protected instance variable---------------it access with in class and in derived class.
                             # protected variables can access inside class and  in derived class also

class Car(Vehical):
    def __init__(self):
        self.w

c=Car("v8 disiel")

c.publicMethod1()

print(c._Car__engine)#Name Mangling
