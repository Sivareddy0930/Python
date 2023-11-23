car={
    "company":"Tata",
    "engine":"v8 desiel",
    "cost":1000000,
    }

print(car["company"])


# get()
print(car.get("engine"))

# The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
# They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.

# keys()
# The keys() method will return a list of all the keys in the dictionary
l1=car.keys()
print(l1)
print(type(l1))

# values()
# The values() method will return a list of all the values in the dictionary
print(car.values())
print(type(car.values()))

# items()
# The items() method will return each item in a dictionary, as tuples in a list.

print(car.items())
print(type(car.items()))