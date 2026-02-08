"""Functions"""
# def sum(a, b): """Parameters"""
#     print(f"The sum of numbers is {a+b}")

# sum(12, 10)
# sum(21, 8) """Arguments"""

"""Types of arguments"""

""" 1. Positional arguments """
# def add(a, b):
#     return a+b

# print(add(3, 5)) # 3 is assigned to a, 5 is assigned to b

""" 2. Keyword arguments """
# def introduce(name, age):
#     print(f"Hello, I am {name} and I am {age} years old")

# introduce(age=25, name="John")

""" 3. Default arguments """
# def greet(name="Guest"):
#     print(f"Hello, {name}")

# greet() #Uses default value "Guest"
# greet("Bob") #Uses "Bob"


"""Function to check if string is palindrome or not"""
# def palindrome(string):
#     reverse = ""

#     for i in range(len(string)-1, -1, -1):
#         reverse = reverse + string[i]

#     if string == reverse:
#         print(f"{string} is a palindrome")

#     else:
#         print(f"{string} is not a palindrome")

# palindrome("naman")
# palindrome("harsh")

"""Return"""
# def hello():
#     return "Hello, how are you?"

# print(hello())