# for adding and updateing we use  update() method and key indexing concept----- car[key]=value
car={
    "company":"Tata",
    "engine":"v8 desiel",
    "cost":1000000,
    }
print(car)

# Adding an item to the dictionary is done by using a new index key and assigning a value to it.
car["model"]="Tata Benz"
print(car)

# update() method is used to add new key:value pair to dict.

car.update({"owner":"siva"})
print(car)


car.update({"owner":"siva","EngineType":"desielEngine"})
print(car)