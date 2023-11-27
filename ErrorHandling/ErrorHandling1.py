# try except finally
a=10
b='b'
try:
    print("connection is opened")
    print(a/b)
except ArithmeticError as e:
    print("ArithmeticError:-",e)
except NameError as e:
    print("NameError:-",e)

except TypeError as e:
    print("TypeError:-",e)
except Exception as e:
    print(e)
finally:
    print("connection closed")


