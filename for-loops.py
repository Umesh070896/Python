"""For loops in numbers"""
# Print from 1 to 20
# for i in range(1, 21):
#     print(i)

# Print from 20 to 50
# for i in range(20,51):
#     print(i)

# Print from 16 to 1
# for i in range(16,0,-1):
#     print(i)

# Print from -5 to -15
# for i in range(-5,-16,-1):
#     print(i)

# Print table of number
# 1st approach
# number = int(input("Enter the number: "))

# for i in range(number, (number*10 + 1), number):
#     print(i)

# 2nd approach
# number = int(input("Enter the number: "))

# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")


"""For loops in strings"""
# 1st approach
# text = "HELLO WORLD!" 
# print(len(text))

# for i in range(len(text)):
#     print(text[i])


# 2nd approach
# text = "HELLO WORLD!"

# for i in text:
#     print(i)


"""Practice Questions"""

"""Accept an integer and Print hello world n times"""
# number = int(input("Enter the number: "))

# for i in range(number):
#     print("Hello World")


"""Print natural number up to n"""
# number = int(input("Enter the number: "))

# for i in range(1, number+1):
#     print(i)


"""Reverse for loop. Print n to 1"""
# number = int(input("Enter the number: "))

# for i in range(number, 0, -1):
#     print(i)


"""Take a number as input and print its table"""
# number = int(input("Enter the number: "))

# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")


"""Sum up to n terms"""
# n = int(input("Enter the number: "))
# total = 0

# for i in range(n+1):
#     total += i

# print(f"The total of {n} terms is {total}")


"""Factorial of a number"""
# n = int(input("Enter the number: "))
# fact = 1

# for i in range(n, 1, -1):
#     fact *= i

# print(f"The factorial of {n} is {fact}")


""" Print the sum of all even & odd numbers in a range separately """
# lowerRange = int(input("Enter the lower range: "))
# upperRange = int(input("Enter the upper range: "))

# sumOfEvenNumbers = 0
# sumOfOddNumbers = 0

# for i in range(lowerRange, upperRange+1):
#     if i%2 == 0:
#         sumOfEvenNumbers += i
#     else:
#         sumOfOddNumbers += i

# print(f"The sum of even numbers is {sumOfEvenNumbers}")
# print(f"The sum of even numbers is {sumOfOddNumbers}")


"""Print all the factors of a number"""
# number = int(input("Enter the number: "))

# for i in range(1, number+1):
#     if number%i == 0:
#         print(i)


"""Accept a number and check if it a perfect number or not
   A number whose sum of factors is equal to the number itself
   Ex - 6 = 1, 2, 3 = 6
"""
# number = int(input("Enter the number: "))

# sumOfFactors = 0

# for i in range(1, number):
#     if number%i == 0:
#         sumOfFactors += i

# if sumOfFactors == number:
#     print("It is a perfect number")
# else:
#     print("It is not a perfect number")


"""Check wether the number is prime or not"""
# number = int(input("Enter the number: "))

# count = 0

# for i in range(1, number+1):
#     if number%i == 0:
#         count += 1

# if count == 2:
#     print("It is a prime number")

# else:
#     print("It is not a prime number")


"""Reverse a string without using in build functions"""
# text = input("Enter the string: ")

# reverse = ""

# for i in range(len(text)-1, -1, -1):
#     reverse = reverse + text[i]

# print(f"The reverse of {text} is {reverse}")


"""Check string is Palindrome or not"""
# text = input("Enter the string: ")

# reverse = ""

# for i in range(len(text)-1, -1, -1):
#     reverse = reverse + text[i]

# if text == reverse:
#     print("The string is a palindrome")

# else:
#     print("The string is not a palindrome")


"""Count all letters, digits, and special symbols from a given string
    Given: str1 = "P@#yn26at^&i5ve"
    Expected Outcome:
    Total counts of chars are 8, digits are 3, and symbols are 4
"""
# text = input("Enter the string: ")

# charactersCount = 0
# digitsCount = 0
# symbolsCount = 0

# for i in range(0, len(text)):
#     if text[i].isdigit():
#         digitsCount += 1
    
#     elif text[i].isalpha():
#         charactersCount += 1
    
#     else:
#         symbolsCount += 1

# print(f"Total counts of chars are {charactersCount}, digits are {digitsCount}, and symbols are {symbolsCount}")
