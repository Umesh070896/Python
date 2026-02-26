"""Error"""
# Serious problems in the program logic that stops the code from running at all which cannot be handled.
# Examples include Syntax error, Indentation error, etc.

# Syntax Error (Error)
# print("Hello world"  # Missing closing parenthesis

"""Exception"""
# Exceptions are unexpected events that occurs during the execution of a program, which disrupts the normal flow.
# It occurs at runtime and can be managed using exception handling.
# Example includes invalid input, missing files, etc.

# ZeroDivisionError (Exception)
# n = 10
# res = n / 0 # Dividing a number by 0 raises a ZeroDivisionError
# print(res) # This line will never run

"""
  Python provides four main keywords for handling exceptions:
    try: Wrap the block of code that might cause an exception.
    except: Handle the exception if it occurs.
    else: Executes only if no exception occurs in try.
    finally: Run code no matter what, whether there’s an exception or not.
"""
try:
    n = int(input("Enter the number: "))
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")


"""Another way if we dont know exception type"""
try:
    n = int(input("Enter the number: "))
    res = 100 / n
    
except Exception as error:
    print("Error: ", error)
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

"""Raise an exception"""
# It is used to manually throw an exception.
# Basic Syntax: raise ExceptionType("Error message")

age = int(input("Enter the age: "))

try:
    if age < 10 or age > 18:
        raise ValueError("Age must be between 10 and 18")
    else:
        print("Welcome to the club!")

except Exception as err:
    print(f"Error occured: {err}")

print("The club will start soon")


