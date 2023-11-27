# Accessing Parent Class Variables In Child class.

class A:
    name="siva"#public class variable
    _age=22#protected class variable
class B(A):
    def __init__(self):
        print(self.name,self._age)
b=B()