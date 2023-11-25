class Computer:
    def config(self):
        print("16 Gb ram,i5")

# creating object

comp1=Computer()#object 1
# Computer()  is a constructor and comp1 is reference.

# accessing method using object

Computer.config(comp1)
# comp1 is collected by self parameter to represent current instance
# ---------------------------------------------------------------------
comp1.config()
# this is same as Computer.config(comp1).
# internally comp1 is considered as parameter .
