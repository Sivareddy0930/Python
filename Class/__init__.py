# In order to make an instance of a class in Python, a specific function called __init__ is called.
# Although it is used to set the object's attributes, it is often referred to as a constructor.

# The self-argument is the only one required by the __init__ method.
# This argument refers to the newly generated instance of the class.
# To initialise the values of each attribute associated with the objects, you can declare extra arguments in the __init__ method.

# example
class Computer:
    def __init__(self,cpu,ram):
        # SELF represents the instance of class.
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("configuration ="+self.cpu,self.ram)

com1=Computer("i5","16 GB ram")
com2=Computer("i7","8 GB ram")

com1.config()
com2.config()