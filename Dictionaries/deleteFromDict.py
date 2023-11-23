car={
    "company":"Tata",
    "engine":"v8 desiel",
    "cost":1000000,
    "model":"tata100"
    }

# pop() method is used to delete specified key and value.

car.pop("model")
print(car)

# popitem() it remove last added key-value pair
car.popitem()
print(car)

del car["engine"]
print(car)

# clear()
car.clear()
print(car)