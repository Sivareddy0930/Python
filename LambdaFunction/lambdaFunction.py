# Lambda Functions in Python are anonymous functions, implying they don't have a name.
# We can also use the lambda keyword in Python to define an unnamed function.

# if you want to use function only once that consist of single statement, and it doesn't have any name then we go for lambda function.



# Syntax
# lambda arugments:expression

# This function accepts any count of inputs but only evaluates and returns one expression. That means it takes many inputs but returns only one output.

l=lambda a,b:a+b
print(l(2,2))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Example:-

def fun(n):
    return lambda a:a*n
mylambda=fun(10)
# here fun(10) is called and here n=10.
# outer function return a lamda function that is stored in mylambda and it accept a arugment a.
# a=4
print(mylambda(4))