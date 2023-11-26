# Operator overloading
# it is the modifying the actual behavior of operator.
# For example operator + is used to add two integers as well as join two strings and merge two lists.
# It is achievable because ‘+’ operator is overloaded by int class and str class.


# How to overload the operators in Python?

# Consider that we have two objects which are a physical representation of a class (user-defined data type) and
# we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know how to add two objects.
# So we define a method for an operator and that process is called operator overloading.
# We can overload all existing operators but we can’t create a new operator. To perform operator overloading,
#  Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator.
#  For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.

# class student:
#     def __init__(self,marks):
#         self.marks=marks
#
# s1=student(89)
# s2=student(94)
#
# s3=s1+s2#TypeError: unsupported operand type(s) for +: 'student' and 'student'

# --------------------------------------------------------------------------------------------------

# overloading behavior of + operator
class student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self, other):
        total=self.marks+other.marks
        return total

s1=student(89)
s2=student(94)

s3=s1+s2 #  student.__add__(s1,s2)
# here s1=self,s2=other and s3 is representation of student type
print(s3)

print(s1.__add__(s2))
print(student.__add__(s1,s2))