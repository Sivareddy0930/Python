#  Decorator are used to modify the behavior of the function.
#  Decorators provide the flexibility to wrap another function to expand the working of wrapped function, without permanently modifying it.
# In Decorators, functions are passed as an argument into another function and then called inside the wrapper function.

# example

def divi(x,y):
    return x/y
print(divi(2,4))
# ------------------------------------------
print("-----------------------------------------------------------")
# we want to change the behavior of the function -----> to that always my function take  greatest number as a numerator from passed arugments.

def div(x,y):
    return x/y

def outer_div(func):
    def innerfun(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)

    return innerfun
div1=outer_div(div)

print(div1(2,4))

# debug program for better understanding
