# Factorial of a Number with recursion
# 4!=4*3*2*1

result=1
def fact(n):
    global result
    if n>0:
        result=result*n
        fact(n-1)
    return result

factNum=fact(4)
print(factNum)


print("---------------------------------------")
# second approach
def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)

factNum=fact(4)
print(factNum)
