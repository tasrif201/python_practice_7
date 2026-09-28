# 🐍 Python Functions — Parameters & Return

# 1. Function
# Function is a reusable block of code that can call repeatedly whwnever needed.abs
def say_hello():
    print("Hello Abdullah!")

say_hello()

# 2. Parameter
# use a parameter to pass a value from outside into a function.
def greet(name):
    print("Hello", name)

greet("Abdullah")
greet("Rabib")

# 3. Multiple Parameter
def add(a, b):
    print(a + b)

add(20, 30)

# 4. Return
# return is used to send the result of a function back outside.
def add(a, b):
    result = a + b
    return result

answer = add(20, 30)
print(answer)

# 5. print() vs return
def add(a, b):
    return a + b

result = add(20, 30)

final_result = result * 2

print(final_result)

# 6.Calculator Function
def calculator (a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)

calculator(20, 30)

# 7. ruturn calculator 
def add (a, b):
    return a+b

def subtract (a, b):
    return a-b

def multiply (a, b):
    return a*b

def divide (a, b):
    return a/b

print(add(20, 40))
print(subtract(20, 40))
print(multiply(20, 40))
print(divide(20, 40))

# 8. Function + If/Else
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
result = check_number(20)
print(result)

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
result = check_number(-2)
print(result)

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
result = check_number(0)
print(result)

# 9. Function + List
def find_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

numbers = [10, 20, 30, 40]

result = find_sum(numbers)
print(result)

# Practice
# Problem 1
def add (a, b):
    result = a + b
    return result

answer = add(10, 20)
print(answer)

# Problem 2
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(24)
print(result)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(27)
print(result)

# Problem 3 
def find_largest(a, b, c):
    largest = a

    if b > largest:
        largest = b
    
    if c > largest:
        largest = c
    return largest

result = find_largest(10, 50, 30)
print(result)

# Problem 4

def check_result(marks):
    if marks >= 40:
        return "Passed"
    else:
        return "Failed"
result = check_result(27)
print(result)

def check_result(marks):
    if marks >= 40:
        return "Passed"
    else:
        return "Failed"
result = check_result(70)
print(result)