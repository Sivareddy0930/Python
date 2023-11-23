# remove() used to remove specified element.
# if specified element is not exist it will throw error
s1={1,2,3,4,"python"}

s1.remove("python")
# s1.remove("python100")
print(s1)

# discard() used to remove specified element.
# # if specified element is not exist it will not throw any error.

s1.discard(100)
print(s1)


# pop() is used to remove the element randomly.

s1.pop()
print(s1)

# del is used to delete the set itself

del s1
# print(s1)


# clear() to delete all elemnts but not set .

s2={6,7,8,9}
s2.clear()
print(s2)