# we want to pass a list to function as an arugment and funtion have to return how many no.of odd and evens are there in list.

def countOddAndEven(lst):
    even,odd=0,0
    for x in lst:
        if x%2==0:
            even +=1
        else:
            odd +=1
    return even,odd

lst=[1,2,3,4,5,6,7,8,9]

EvenCount,OddCount=countOddAndEven(lst)

print("EvenCount={},OddCount={}".format(EvenCount,OddCount))