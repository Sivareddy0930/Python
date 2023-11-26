# Encapsulation is process of wrapping variables and methods into a single unit.
# by using encapsulation we can achieve dataHiding and Abstraction
# data hiding can be done by using access modifiers like private ,protected,public.

class Car:
    def __init__(self):
        self.company="Tata"#public instance variable------------------it can accees allover.
        self._model="nexon"#protected instance variable---------------it access with in class and in derived class.
        self.__engine="v8 diesel"#private instance variable-----------it access only with in class.

c=Car()
