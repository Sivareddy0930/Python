l1=["apple","banana","cherry","berry","melon"]
for x in l1:
    print(x)

print("-------------------------")
# break
for x in l1:
    if x=="cherry":
        break
    print(x)

print("-------------------------")
#continue
for x in l1:
    if x=="cherry":
        continue
    print(x)
print("-------------------------")

for x in l1:
    print(x)
else:
    print("no longer activated")


