class Computer:

    # __init__()  is a constructor .which is used to initialize object variables and irt called automatically.
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