"""
   Tuple is a built-in data structure with following properties:
   Duplicates: items can occur multiple times.
   Immutable: items cannot be modified after creation.
   Ordered: maintains the order in which items are added.
   Index-based: items are accessed using their position (starting from 0).
   Heterogenous: Can store different data types (integers, strings, booleans, lists).
"""

# tup = ()
# print(tup)

"""Using String"""
# tup = ('Learning', 'Python')
# print(tup)

"""Using List"""
# li = [1, 2, 3, 4, 5, 6]
# print(tuple(li))

"""Using built-in function"""
# tup = tuple('Hello')
# print(tup)

# tup = (5, 'Welcome', 7, 'Learner')
# print(tup)

"""Creating a Tuple with nested tuples"""
# tup1 = (0, 1, 2, 3)
# tup2 = ('python', 'program')
# tup3 = (tup1, tup2)
# print(tup3)

"""Creating a Tuple with repetition"""
# tup1 = ('Python',) * 3
# print(tup1)

"""Creating a Tuple with the use of loop"""
# tup = ('Hello')
# n = 5
# for i in range(int(n)):
#     tup = (tup,)
#     print(tup)

"""Accessing of Tuples"""

"""Accessing Tuple with Indexing"""
# tup = tuple("Hello")
# print(tup[0])

"""Accessing a range of elements using slicing"""
# print(tup[1:4])  
# print(tup[:3])

"""Tuple unpacking"""
# tup = ("Happy", "Python", "Learning")

# This line unpack values of Tuple
# a, b, c = tup
# print(a)
# print(b)
# print(c)

"""Concatenation of Tuples"""
"""
   Tuples can be concatenated using the + operator. This operation combines two or more tuples to create a new tuple.
   Only the same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined.
"""
# tup1 = (0, 1, 2, 3)
# tup2 = ('Welcome', 'Python', 'Platform')

# tup3 = tup1 + tup2
# print(tup3)

"""Slicing of Tuple"""
# tup = tuple('PYTHONLEARNING')

# print(tup[1:])

# Reversing the Tuple
# print(tup[::-1])

# print(tup[4:9])

"""Deleting a Tuple"""
"""
    Since tuples are immutable, we cannot delete individual elements of a tuple.
    However, we can delete an entire tuple using del statement.
    Printing of Tuple after deletion results in an Error.
"""
# tup = (0, 1, 2, 3, 4)
# del tup

"""Tuple Unpacking with Asterisk (*)"""
"""
    The " * " operator can be used in tuple unpacking to grab multiple items into a list.
    This is useful when you want to extract just a few specific elements and collect the rest together.
"""
# tup = (1, 2, 3, 4, 5)

# a, *b, c = tup

# print(a) 
# print(b) 
# print(c)
