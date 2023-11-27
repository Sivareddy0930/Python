# raise is used to throw a custom Exception.

try:
    raise ValueError("valueError")
except ValueError as e:
    print("valueError:-",e)
    try:
        raise  ArithmeticError("Arithmetic Exception")
    except ArithmeticError as e1:
        print("ArithmeticError:-",e1)
finally:
    print("finally block")
    try:
        raise  TypeError("TypeError")
    except TypeError as e2:
        print("TypeError:-",e2)

