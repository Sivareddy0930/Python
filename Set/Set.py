#A set is a collection which is unordered, changeable, and unindexed.

set1={1,2,4.4444,"siva",1,True,1,"siva",1}
# internally 1 is considerd as true and 0 is consider as false.

print(set1)#{1, 2, 'siva', 4.4444}

# length of set
set2={True,1,2,4.4444,"siva",1,True,1,"siva",1}

print(set2)
print(len(set2))

# type

print(type(set2))

# set() Constructor

set3=set(("siva","reddy",1,4,True,4.4444))

print(set3)
print(type(set3))


#accessing set items

for x in set3:
    print(x)

if "siva" in set3:
    print("siva is present in set3")


