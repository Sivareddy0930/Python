l1=[100,50,40,23,65,4]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
# ---------------------------------------------
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
l2=["apple","Banana","cherry","Zoo","berry"]
l2.sort()
print(l2)
# ---------------------------------------------
l2=["apple","melon","cherry","jerry","berry"]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)

#---------------------------------------------------
# You can also customize your own function by using the keyword argument key = function.

def myfun(n):
    return abs(n-50)
# Based on lowest difference values are sorted.
# 100-50=50
# 50-50=0
# 40-50=10
# ......
l3=[100,50,40,23,65,4]

l3.sort(key=myfun)

print(l3) #[50, 40, 65, 23, 4, 100]
# --------------------------------------------------------------------
# if you want to reverse list .regardless of the alphabet ?
# we use reverse() method .it reverse the list without depnds on values.
l4=["apple","Banana","cherry","Zoo","berry"]
l4.reverse()
print(l4)

