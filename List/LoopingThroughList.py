l=["siva",1,4.4444,True,"10000"]

for x in l:
    print(x)

print("----------------------------------------")
# using indexing with range,len

for i in range(len(l)):
    print(l[i])

print("---------------------------------------")
# while loop

i=0

while i<len(l):
    print(l[i])
    i=i+1