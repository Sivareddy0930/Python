# In the case of Call by Value, when we pass the value of the parameter during the calling of the function, it copies them to the function's actual local argument.
# In the case of Call by Reference, when we pass the parameter's location reference/address, it copies and assigns them to the function's local argument.

# So, while Python is not strictly "pass by value" or "pass by reference," understanding the mutability of objects is crucial for predicting how changes inside a function may affect variables outside of it.


# Mutable Types:
#
# Objects of mutable types can be modified after creation.
# Changes to the object are reflected in the same object.
# Examples of mutable types in Python include:
# Lists (list)
# Dictionaries (dict)
# Sets (set)
# Byte arrays (bytearray)


# ----------------------------
# Immutable Types:
#
# Objects of immutable types cannot be modified after creation.
# Any operation that appears to modify an immutable object actually creates a new object with the modified value.
# Examples of immutable types in Python include:
# Integers (int)
# Floats (float)
# Strings (str)
# Tuples (tuple)
# Frozensets (frozenset)
# Immutable versions of data types (e.g., bytes, namedtuple)




# Example for call by value


def myfun1(value):
    print(value+"reddy")
s="siva "
myfun1(s)
print(s)



def myfun1(value):
    value.append("reddy")
    print(value)
s=["siva"]
myfun1(s)
print(s)