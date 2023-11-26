# if there is a bird that behave like a duck, walk like a duck,quack like a duck, swim lake a duck then it should be a duck.
# similarly, if there is an object that is ide and it has an method execute() thats it.we not consed about which class object it is,
# instead we consed about it should have the method execute() .

class pycharm:
    def execute(self):
        print("compiling")
        print("running")

class Mycharm:
    def execute(self):
        print("compiling")
        print("running")
        print("bug checking")

class code:
    def executeCode(self,ide):
        ide.execute()

ide=pycharm()
ide=Mycharm()

c1=code()

c1.executeCode(ide)


# In Python, the idea of duck typing is expressed through the concept "If it walks like a duck and quacks like a duck, then it must be a duck."
# This means that if an object behaves like a certain type (by having the necessary methods or attributes),
# it can be treated as an instance of that type, regardless of its actual class or type.