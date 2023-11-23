i=0
while i<10:
    print(i)
    i +=1

print("-------------------------")
# task 2
# break loop if value i=5
i=0
while i<10:
    if i==5:
        break
    print(i)
    i +=1

print("-------------------------")
# task 3
# continue loop if value i=5
i=0
while i<10:
    i += 1
    if i==5:
        continue
    print(i)

# task 4
# while with else statement
i=0
while i<5:
    print(i)
    i +=1
else:
    print("loop is no longer activate")

# Else block is not executed. if the loop consist of break.


