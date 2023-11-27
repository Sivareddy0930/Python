# The json.loads() function is used to deserialize a JSON-encoded string (s) into a Python object.
# dump(),dumps(),load(),loads() method available in json module.


import json as js

jsonString='{"name": "John", "age": 30, "city": "New York"}'

b=js.loads(jsonString)
print(b)
# In this example, the JSON-encoded string is deserialized into a Python object (data).


# Note:-
# This indicates that the object may not be the same if we encode it and then decode it again later.
#  from python object  marks is a tuple type .while encoding to json it converted to array .later while converting json to python object it show list of marks.