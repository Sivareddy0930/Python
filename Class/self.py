# The self-parameter refers to the current instance of the class and accesses the class variables.
# We can use anything instead of self, but it must be the first parameter of any function which belongs to the class.
class Human:
    def __init__(self):
        self.name="siva"
        self.age=22

    def setAge(self):
        self.age=17
hum1=Human()
hum2=Human()

hum2.name="vamsi"
hum2.setAge()
# here hum2 is object that mapped to self of setAge() method.so particularly hum2 age is changed

print(hum1.name)
print(hum1.age)
print(hum2.name)
print(hum2.age)

