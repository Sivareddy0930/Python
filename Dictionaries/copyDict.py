car={
    "company": "Tata",
    "engine": "v8 desiel",
    "cost": 1000000,
    "engineType":"desielEngine"
}

# copying
car2=car

print(car2)
print(type(car2))

# copy()

car3=car.copy()
print(car3)

# copying through constructor

car4=dict(car)
print(car4)


