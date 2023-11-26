# In python method overloading is not possible because in a class we cannot declare multiple methods with same name.
# but we can achieve a similar effect through default values for function parameters or variable-length argument lists.

class Demo1:

    def addAll(self,a,b=0,c=4):
        print(a+b+c)

d=Demo1()

# calling same method with different arguments
d.addAll(100)
d.addAll(100,200)
d.addAll(100,200,300)

print("-------------------------------------")
# Another way to achieve a form of method overloading is by using variable-length argument.

class Demo2():
    def addAll(self,*args):
        # args return a tuple
        # we are adding all the elements in tuple by using inbuilt method sum()
        print(sum(args))
d1=Demo2()
d1.addAll(1)
d1.addAll(1,2)
d1.addAll(1,2,3)
d1.addAll(1,2,3,4)
