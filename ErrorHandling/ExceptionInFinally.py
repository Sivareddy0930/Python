# raise is used to throw a custom Exception.

try:
    raise ValueError("valueError")
except ValueError as e:
    print("valueError:-",e)
    raise  ArithmeticError("Arithmetic Exception")
finally:
    print("finally block")
    raise TypeError("Type Error in Finally Block")


# If an exception occurs in the finally block, it takes high precedence over any exception that might have occurred in the try block or the except block.

# The exception raised in the finally block will propagate up the call stack, and any previous exceptions will be suppressed. This is known as an "exception override" behavior.
# finally block excption is consider as major exception then others.

# In this case, the TypeError raised in the finally block will override the  ValueErrorand Arithmetic Exception, and only the TypeError will be propagated.