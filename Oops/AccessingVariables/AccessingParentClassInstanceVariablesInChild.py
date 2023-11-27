# Accessing Parent Class Instance Variables In Child class.

class A:
    def __init__(self,age):
        self._name="siva"#protected instance variable
        self.age=age#public instance variable

class B(A):
    def __init__(self,age):
        super().__init__(age)
        print(self._name,self.age)
b=B(22)