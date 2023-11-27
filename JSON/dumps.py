# The json.dumps() function is used to serialize a Python object (obj) to a JSON formatted string
# and This function returns the resulting JSON string instead of writing it to a file.
# the Python dictionary data is serialized to a JSON string, and the resulting string is printed.
# dump(),dumps(),load(),loads() method available in json module.


import json as js

# python Object
student={"name":"siva","age":22,"salary":45000.99,"male":True,"marks":(98,89,79,100),"college":{"CollegeName":"parul","branch":"CSE"},"friend":None}
#           string      number(int)   number(float)  boolean       tuple                        object

b=js.dumps(student)
print(b)
    # It just takes one argument, which is Python data, to be serialized. We don't write data file to store it.