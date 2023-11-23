car={
    "company": "Tata",
    "engine": "v8 desiel",
    "cost": 1000000,
    "engineType":"desielEngine"
}

# for loop
# by default we get keys. when we iterate a dictionary using for loop .we can get values and key-value pair also by using methods.

for x in car:
    print(x)
print("---------------------------")


# keys()

for x in car.keys():
    print(x)
print("---------------------------")
# values()
for x in car.values():
    print(x)
print("---------------------------")

# items()

for x in car.items():
    print(x)
    # print(type(x))

