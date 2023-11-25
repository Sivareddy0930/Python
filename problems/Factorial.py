# Factorial of a Number
# 4!=4*3*2*1
def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

factNum=fact(4)
print(factNum)