x=10
y=10

if(x>y):
    print("x is greatest")
elif(x<y):
    print("y is greatest")
else:
    print("both are equal")

# Ternary Operators, or Conditional Expressions.

print("x is greatest") if (x>y) else print("y is greatest") if(x<y) else print("Both are same")

# task 2

x=100

if(x>40):
    print("x is great")
else:
    print("not")

# Ternary Operator

print("x is great") if(x>40) else print("not")

print("---------------------------------------------------------")

x=111
y=2222
z=333

if x>y:
    if x>z:
        print(x)
    else:
        print(z)
else:
    if y>z:
        print(y)
    else:
        print(z)

# ternary operator
result= x if x>y and x>z else y if y>z else z

print(result)
