# The filter() method accepts two arguments in Python: a function and an iterable such as a list.
# The function is called for every item of the list, and a new iterable or list is returned that holds just those elements that returned True when supplied to the function.

myList=[1,2,3,4,5,6,7,8,9]
newList=list(filter(lambda item:item%2==0,myList))
print(newList)