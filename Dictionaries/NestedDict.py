# A dictionary can contain dictionaries, this is called nested dictionaries.
myFamily={
    "child1":{
        "name":"siva",
        "age":22
    },
    "child2":{
        "name":"vamsi",
        "age":17
    }
}

# accessing data

print(myFamily["child2"]["name"])


# Task
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries.

branch1={
    "barnchName":"cse",
    "strength":10000
    }
branch2={
    "barnchName":"it",
    "strength":500
}
branch3={
    "branchName":"mech",
    "strength":250
}


dept={
    "branch1":branch1,
    "branch2":branch2,
    "branch3":branch3
}
print(dept)