# The json.load() function is used to deserialize JSON data from a file-like object. It reads the content from the file and returns a Python object.
# dump(),dumps(),load(),loads() method available in json module.


import json as js

with open('myjsonFile','r') as pythonObject:
    b=js.load(pythonObject)
    print(b)
    # In this example, the content of the 'myjsonFile' file is read and deserialized into a Python object

# Note:-
# This indicates that the object may not be the same if we encode it and then decode it again later.
#  from python object  marks is a tuple type .while encoding to json it converted to array .later while converting json to python object it show list of marks.