"""
   Dictionary is a built-in data structure that stores data in key-value pairs with following properties:
   Duplicates: Keys must be unique but you can have duplicates in value.
   Mutable: Key-value pairs can be added, updated or removed after their creation.
   Ordered: It follows an insertion order.
   Heterogenous: Can store different types of keys and values like integers, strings, booleans, lists or even another dictionary.
"""

data = { "name": "Jake", "age": 22 }
print(data)

# Using dict() function
d = dict(a = "Python", b = "for", c = "fun")
print(d)

"""Accessing Dictionary Items"""
# A value in a dictionary is accessed by using its key.
# This can be done either with square brackets [ ] or with the get() method.
# Both return the value linked to the given key.

d = { "name": "Katherine", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])
print(d[(1, 2)])

# Access using get()
print(d.get("name"))

"""Adding and Updating Dictionary Items"""
# New items are added to a dictionary using the assignment operator (=) by giving a new key a value.
# If an existing key is used with the assignment operator, its value is updated with the new one.

d = {1: 'Python', 2: 'Learning', 3: 'For'}

# Adding a new key-value pair
d["4"] = "Fun"

# Updating an existing value
d[1] = "Python dictionary"
print(d)

"""Removing Dictionary Items"""
# Dictionary items can be removed using built-in deletion methods that work on keys:

# del: removes an item using its key
# pop(): removes the item with the given key and returns its value
# clear(): removes all items from the dictionary
# popitem(): removes and returns the last inserted key–value pair

d = {1: 'Python', 2: 'Learning', 3: 'For', 4: 'Fun'}

# Using del 
del d[4]
print(d)

# Using pop() 
val = d.pop(1)
print(val)

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
d.clear()
print(d)

"""Iterating Through a Dictionary"""
d = {1: 'Python', 2: 'Program', 3: 'Learning'}

# Iterate over keys
for key in d:
    print(key)
    print(d[key])

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")