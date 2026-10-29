# Exceptions	try/except/else/finally

# 1. Exceptions
# Exception is an error condition that occurs while a program is running. If it is not handled
# it can cause the program’s normal execution to stop.

a = 10
b = 0
result = a / b
print(result)

# 2. try and except
# try : Write the code that may cause an exception inside the try block.
# Except: Use except to handle a specific exception that occurs in the try block.

a = 10
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("You can not divide by zero!")
print("Program finished")

# 3. Handling Multiple Exception

try:
    a = int(input("Enter firest number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers!")

except ZeroDivisionError:
    print("You cannot divide by Zero!")

# 4. else
# In exception handling, the else block is used when no exception occurs in the try block.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid Input!")

else:
    print("Your number is:", number)

# 5. finally
# The finally block usually executes in all cases, whether an exception occurs or not.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input!")

finally:
    print("Program execution completed.")

# 6. All together : try, expect, else, finally
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter valid numbers!")

except ZeroDivisionError:
    print("Cannot dividenby zero!")

else:
    print("Result:", result)

finally:
    print("Calculation attempt finished.")

# 7. raise
age = -5
try:
    if age < 0:
        raise ValueError("Age cannot be negative!")
    
    print("Age:", age)

except ValueError as error:
    print(error)

# Practice
# Problem 1 : Safe Division

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# Problem 2: Integer Conversion

user_input = input("Enter a number: ")

try:
    number = int(user_input)

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful")

finally:
    print("Program finished")

# Problem 3: Age Checker

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")
    
    print("Valid age")

except ValueError as e:
    print("Invalid age:", e)

finally:
    print("Program finished")