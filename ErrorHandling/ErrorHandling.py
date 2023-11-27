# try except finally
a=10
b=0
try:
    print("connection is opened")
    print(a/b)
except Exception as e:
    print(e)
finally:
    print("connection closed")


