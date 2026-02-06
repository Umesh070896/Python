# Print 1 to 30
# num = 1

# while num <= 30:
#     print(num)
#     num += 1

"""Separate each digit of a number and print it on the new line"""
# num = int(input("Enter the number: "))

# while num > 0:
#     print(num%10)
#     num = num//10

"""Accept a number and print its reverse"""
# num = int(input("Enter the number: "))

# reverse = 0

# while num > 0:
#     reverse = reverse*10 + num%10
#     num = num//10

# print(reverse)

"""Accept a number and check if it is a palindrome"""
# num = int(input("Enter the number: "))

# original = num
# reverse = 0

# while num > 0:
#     reverse = reverse*10 + num%10
#     num = num//10

# if original == reverse:
#     print("The number is palindrome")

# else:
#     print("The number is not palindrome")

"""Create a random number guessing game with python"""
import random

secretNumber = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Please guess the number between 1 and 10: "))

    if guess == secretNumber:
        print(f"Your guess is correct.")
        break

    elif secretNumber < guess:
        print("Go a little lower")
    
    elif secretNumber > guess:
        print("Go a little higher")

    attempts -= 1

print(f"Game over!! The correct number was {secretNumber}")


