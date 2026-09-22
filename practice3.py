# Conditions - Operators, if/elif/else

# 1. Condition
# Condition means Check the answer which is right or wrong
age = 26
print(age >= 18)
age = 16
print(age >= 18)


# 2.Comparison Operator
# ( == , equals), ( != , not equals), ( > , greater), ( < , lessthen), ( >= , greater or equals), ( <= , lessthen or equals)
age = 26
print(age > 18)
print(age < 18)
print(age == 20)
print(age != 20)
print(age >= 18)
print(age <= 18)


# 3. If Statement
# if uses when it is true
age = 20
if age >= 18:
    print("You are an adult")

# 4.Indentation
# After if and before print() that must be 4 spaces
age = 20
if age >= 18:
    print("You are an adult")
# So if,elif,else that should be write code 4 spaces


# 5.else
# If if condition is false then else is print
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")


# 6. Elif
# when check many condition so that use elif
marks = 76
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("Fail")


# 7. Real- life example
# Price = 1000 - 10% discount
# Price = 500  - 5% discount
# Otherwise - No discount
price = 1300
if price >= 1000:
    print("10% discount")
elif price >= 500:
    print("5% discount")
else:
    print("No discount")

price = 700
if price >= 1000:
    print("10% discount")
elif price >= 500:
    print("5% discount")
else:
    print("No discount")

price = 400
if price >= 1000:
    print("10% discount")
elif price >= 500:
    print("5% discount")
else:
    print("No discount")


# 8. and, or, not
# These re all Logical operator
# and
# Two conditions are same and true
age = 40
if age >= 18 and age <= 40:
    print("Eligible")

# or
# one will be true
day = "Friday"
if day == "Friday" or day == "Saturday":
    print("Weekend")

day = "Saturday"
if day == "Friday" or day == "Saturday":
    print("Weekend")

# not
# It is true is false and false is true
is_raining = False
if not is_raining:
    print("Go Outside")


# Practice

# Practice 1- Positive/Negative
number = 10
if number > 0:
    print("Positive")
else:
    print("Negative")

number = -5
if number > 0:
    print("Positive")
else:
    print("Negative")

# Practice 2- Even/odd
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Practice 3- Pass/Fail
marks = 55
if marks >= 40:
    print("Passed")
else:
    print("Failed")

marks = 30
if marks >= 40:
    print("Passed")
else:
    print("Failed")

# Practice 4- Grade
marks = 85
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

marks = 75
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


marks = 65
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

marks = 55
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

marks = 45
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# Challenge 1
age = 26
if age >= 18:
    print("Adult")
else:
    print("Minor")

age = int(input("Your age:"));
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Challenge 2
number = int(input("Number: "));
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("0")

number = 7
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("0")

number = -3
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("0")

number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("0")

# Challenge 3
marks =int(input("Marks: "));
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")