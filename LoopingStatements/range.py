# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.

for x in range(5):
    print(x)

print("-------------------------------------------")

# range(startIndex,endIndex,increment):

for x in range(3,30,3):
    print(x)

print("--------------------------------------------")

# for with else
for x in range(2):
    print(x)
else:
    print("nothing to achieve")
# else will not execute when we use break in looping.

print("-------------------------------------------------")

# nested for loop

for x in range(5):
    for y in range(5):
        print(x,y)
