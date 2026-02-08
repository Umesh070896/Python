"""List is a built-in data structure that can hold an ordered collection of items.
   Duplicates: items can occue multiple times.
   Mutable: items can be modified, replaced, or removed.
   Ordered: maintains the order in which items are added.
   Index-based: items are accessed using their position (starting from 0).
   Heterogenous: Can store mixed data types (integers, strings, booleans, even other lists).
"""

# numbers = [1, 2, 3, 4, 5] # List of integers
# fruits = ['apple', 'banana', 'cherry'] # List of strings
# mixed = [1, 'hello', 3.14, True] # Mixed data types

# print(numbers)
# print(fruits)
# print(mixed)

"""List indexing"""
#+ve index    0  1   2   3   4   5
# numbers = [12, 13, 14, 15, 16, 17]
#-ve index   -6  -5  -4  -3  -2  -1

# print(numbers[0])
# print(numbers[1])
# print(numbers[-1])

"""List slicing"""
# numbers = [12, 13, 14, 15, 16, 17]

# print(numbers[0:5])

"""List traversing"""
# numbers = [12, 13, 14, 15, 16, 17]

# 1st way using index (recommended)
# for i in range(len(numbers)):
#     print(i)
#     print(numbers[i])


# 2nd way directly on values
# for i in numbers:
#     print(i)


"""List methods"""

"""Adding Elements into List"""
"""
    append(): Adds an element at the end of the list.
    clear(): removes all items.
    extend(): Adds multiple elements to the end of the list.
    insert(): Adds an element at a specific position.
"""
# a = []

# a.append(10)  
# print("After append(10):", a)  

# a.insert(0, 5)
# print("After insert(0, 5):", a) 

# a.extend([15, 20, 25,])  
# print("After extend([15, 20, 25]):", a)

# a.clear()
# print("After clear():", a)


"""Removing Elements from List"""
"""
    remove(): Removes the first occurrence of an element.
    pop(): Removes the element at a specific index or the last element if no index is specified.
    del statement: Deletes an element at a specified index.
"""
# a = [10, 20, 30, 40, 50]

# a.remove(30)  
# print("After remove(30):", a)

# popped_val = a.pop(1)  
# print("Popped element:", popped_val)
# print("After pop(1):", a) 

# del a[0]  
# print("After del a[0]:", a)


"""Updating Elements into List"""
# numbers = [10, 20, 30]
# # Modift the value at index 1 (2nd element)
# numbers[1] = 40

# print(numbers)
