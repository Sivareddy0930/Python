# raise is used to throw a custom Exception.

try:
    raise ValueError("valueError")
except ValueError as e:
    print("valueError:-",e)
    raise  ArithmeticError("Arithmetic Exception")
finally:
    print("finally block")

# If an exception occurs in the except block itself (e.g., while handling the original exception),it can lead to a nested exception.
# This new exception will propagate up the call stack, just like any other exception.