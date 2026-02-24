"""
   Set is a built-in data structure with following properties:
   Non Duplicates: If try to insert the same item again, it overwrites previous one. Every item will be unique.
   Mutable: elements can be added or removed after their creation, the individual item within the set cannot be changed directly.
   Unordered: All items are accessed without any specific order and we cannot access items using indexes.
   Heterogenous: Can store different data types (integers, strings, booleans).
"""

s = {10, 50, 20}
print(s)
print(type(s))

"""Using heterogeneous elements"""
s = {"Python", "for", 10, 52.7, True}
print(s)

"""Python sets cannot have duplicate values"""
s = {"Python", "Learning", "Python"}
print(s)

"""Type Casting"""
# set() method in python is used to convert other data types, such as lists or tuples, into sets.

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding an element to the set
s.add("d")
s.add("e")
print(s)

# Removing an element from the set
s.remove("a")
print(s)

"""Frozen Sets"""
# A frozenset is an immutable version of a set. Its elements cannot be changed after creation, but you can perform operations like union, intersection and difference. Use frozenset() to create one.

# Normal set (mutable)
s = set(["a", "b", "c"])
print("Normal Set:", s)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)

# Note: Frozensets are immutable, so methods like add() or remove() cannot be used.

"""Set Methods"""

# Union of Sets: union() function combines two sets and returns a new set with all unique elements.
a = {1, 2, 3}
b = {3, 4, 5}
u = a.union(b)
union = a | b
print(u)
print(union)

# Intersection of Sets: intersection() function returns a new set containing elements that are common to both sets.
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
intersection = a & b
print(i)
print(intersection)

# Difference of Sets: difference() function returns a set containing elements that are in the first set but not in the second set.
a = {1, 2, 3}
b = {2, 3, 4}
d1 = a.difference(b)
difference1 = a - b
d2 = b.difference(a)
difference2 = b - a
print(d1)
print(difference1)
print(d2)
print(difference2)

# Symmetric Difference of Sets: symmetric_difference() function returns a new set containing elements that are present in both the sets excluding the common elements.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
sd = a.symmetric_difference(b)
systematic_difference = b ^ a
print(sd)
print(systematic_difference)

# Clearing a Set: clear() function removes all elements from a set, leaving it empty.
s = {1, 2, 3}
s.clear()
print(s)