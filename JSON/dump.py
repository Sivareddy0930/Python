#The json.dump() function is used to serialize a Python object (obj) to a JSON formatted string and write it to a file-like object.
# This function is suitable for writing JSON data to a file.
# dump(),dumps(),load(),loads() method available in json module.


import json as js

# python Object
student={"name":"siva","age":22,"salary":45000.99,"male":True,"marks":(98,89,79,100),"college":{"CollegeName":"parul","branch":"CSE","friend":None}}
#           string      number(int)   number(float)  boolean       tuple                        object

with open("myjsonFile",'w') as writeFile:
    js.dump(student, writeFile)
    # It takes two positional arguments: the data object that needs to be serialized and the file-like object that needs to receive the bytes and storeing purpose.


    # There are instances when a lot of JSON data needs to be analyzed and debugged.
    # It can be done by giving extra arguments to the json. dumps() and json.dump() functions, such as indent and sort_keys.