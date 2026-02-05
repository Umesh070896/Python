"""Accept two numbers and print the greatest between them"""
# num1 = int(input("Enter the first number: "))

# num2 = int(input("Enter the second number: "))

# if num1 > num2:
#     print("num1 is greater")

# elif num2 > num1:
#     print("num2 is greater")

# else:
#     print("Both the numbers are same")


"""Accept the gender from the user as char and print the respective greeting message
   Ex - Good Morning Sir (on the basis of gender)
"""
# gender = input("Enter the gender (M or F): ")

# if gender == "M" or gender == "m":
#     print("Good Morning Sir")

# elif gender == "F" or gender == "f":
#     print("Good Morning Ma'am")

# else:
#     print("Unidentified gender")


"""Accept an integer and check whether it is an even number or odd"""
# number = int(input("Enter the number: "))

# if number%2 == 0:
#     print("The number is even")

# else:
#     print("The number is odd")


"""Accept name and age from the user. Check if the user is a valid voter or not.
   Ex- “hello shery you are a valid voter”
"""
# name = input("Enter the name: ")

# age = int(input("Enter the age: "))

# if age >= 18:
#     print(f"Hello {name}, you are a valid voter")

# else:
#     print(f"Hello {name}, you are not a valid voter")


"""Accept a year and check if it is a leap year or not"""
# year = int(input("Enter the year: "))

# if year%100 == 0 and year%400 == 0:
#     print(f"{year} is a leap year")

# elif year%100 != 0 and year%4 == 0:
#     print(f"{year} is a leap year")

# else:
#     print(f"{year} is not a leap year")


"""Take the input of temperature in celsius and determine the weather
   Below 0°C → "Freezing Cold"
   0°C to 10°C → "Very Cold"
   10°C to 20°C → "Cold"
   20°C to 30°C → "Pleasant"
   30°C to 40°C → "Hot"
   Above 40°C → "Very Hot"
"""
# temprature = int(input("Enter the temprature: "))

# if temprature < 0:
#     print("Freezing cold")

# elif temprature >= 0 and temprature < 10:
#     print("Very cold")

# elif temprature >= 10 and temprature < 20:
#     print("Cold")

# elif temprature >= 20 and temprature < 30:
#     print("Pleasant")

# elif temprature >= 30 and temprature < 40:
#     print("Hot")

# else:
#     print("Very Hot")
