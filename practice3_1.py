# Level 1- Basic (if/else)

# 1. Positive or Negative
number = 15
if number > 0:
    print("Positive")
else:
    print("Negative")

number = -10
if number > 0:
    print("Positive")
else:
    print("Negative")

number = int(input("Number: "));
if number > 0:
    print("Positive")
else:
    print("Negative")

# 2. Even or Odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

number = 15
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

number = 22
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

number = int(input("Number: "));
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Adult or Minor
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

age = 12
if age >= 18:
    print("Adult")
else:
    print("Minor")

age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

age = 30
if age >= 18:
    print("Adult")
else:
    print("Minor")

age = int(input("Age: "));
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 4. Pass or Fail
marks = 65
if marks >= 40:
    print("Passed")
else:
    print("Failed")

marks = 39
if marks >= 40:
    print("Passed")
else:
    print("Failed")

marks = 40
if marks >= 40:
    print("Passed")
else:
    print("Failed")

marks = 100
if marks >= 40:
    print("Passed")
else:
    print("Failed")

marks = int(input("Marks: "));
if marks >= 40:
    print("Passed")
else:
    print("Failed")


# Level 2- elif

# 5.Grade Calculator
marks = 92
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

marks = 82
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

marks = 72
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

marks = 62
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

marks = 52
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

marks = 42
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

marks = int(input("Marks: "));
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

# 6. Number Comparison
number = 100
if number > 100:
    print("Greater than 100")
elif number < 100:
    print("Less than 100")
else:
    print("Exactly 100")

number = 150
if number > 100:
    print("Greater than 100")
elif number < 100:
    print("Less than 100")
else:
    print("Exactly 100")

number = 60
if number > 100:
    print("Greater than 100")
elif number < 100:
    print("Less than 100")
else:
    print("Exactly 100")

number = int(input("Number: "));
if number > 100:
    print("Greater than 100")
elif number < 100:
    print("Less than 100")
else:
    print("Exactly 100")

# 7. Temperature
temperature = 34
if temperature >= 30:
    print("Temperature is Hot")
elif temperature >= 20:
    print("Temperature is Normal")
elif temperature >= 10:
    print("Temperature is Cool")
else:
    print("Temperature is Cold")

temperature = 24
if temperature >= 30:
    print("Temperature is Hot")
elif temperature >= 20:
    print("Temperature is Normal")
elif temperature >= 10:
    print("Temperature is Cool")
else:
    print("Temperature is Cold")

temperature = 14
if temperature >= 30:
    print("Temperature is Hot")
elif temperature >= 20:
    print("Temperature is Normal")
elif temperature >= 10:
    print("Temperature is Cool")
else:
    print("Temperature is Cold")

temperature = 4
if temperature >= 30:
    print("Temperature is Hot")
elif temperature >= 20:
    print("Temperature is Normal")
elif temperature >= 10:
    print("Temperature is Cool")
else:
    print("Temperature is Cold")

temperature = int(input("Temperature: "));
if temperature >= 30:
    print("Temperature is Hot")
elif temperature >= 20:
    print("Temperature is Normal")
elif temperature >= 10:
    print("Temperature is Cool")
else:
    print("Temperature is Cold")

# 8. Age Category 
age = 6
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

age = 14
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

age = 23
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

age = 65
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

age = int(input("Age: "));
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# and
age = 25
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior")

age = int(input("Age: "));
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior")


# Level 3- Operators Practice 

# 9. 2 Number Compare
a = 25
b = 15
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)
else:
    print("Both numbers are equals")

a = 15
b = 25
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)
else:
    print("Both numbers are equals")

a = 25
b = 25
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)
else:
    print("Both numbers are equals")

a = int(input("A: "));
b = int(input("B: "));
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)
else:
    print("Both numbers are equals")

# 10. Login Check
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

username = "admins"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

username = str(input("Username: "));
password = str(input("Password: "));
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid usernam or password")


# 11. Voteing Eligibility 
age = 25
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

age = int(input("Age: "));
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# 12. Discount Calculator
price = 2500
if price >= 2000:
    print("20% discount")
elif price >= 1000:
    print("10% discount")
else:
    print("No discount")

price = 1500
if price >= 2000:
    print("20% discount")
elif price >= 1000:
    print("10% discount")
else:
    print("No discount")

price = 500
if price >= 2000:
    print("20% discount")
elif price >= 1000:
    print("10% discount")
else:
    print("No discount")

price = int(input("Price: "));
if price >= 2000:
    print("20% discount")
elif price >= 1000:
    print("10% discount")
else:
    print("No discount")


# Level 4- Hard

#12. Lagest Number
a = 25
b = 35
c = 15
if a > b and a > c:
    print("Largest number is", a)
elif b > a and b >c:
    print("Largest number is", b)
else:
    print("Largest number is", c)

a = int(input("A: "));
b = int(input("B: "));
c = int(input("C: "));
if a > b and a > c:
    print("Largest number is", a)
elif b > a and b >c:
    print("Largest number is", b)
else:
    print("Largest number is", c)

a = 25
b = 25
c = 15
if a >= b and a >= c:
    print("Largest number is", a)
elif b >= a and b >= c:
    print("Largest number is", b)
else:
    print("Largest number is", c)

# 13. Smallest number
a = 25
b = 35
c = 15
if a < b and a < c:
    print("Smallest number is", a)
elif b < a and b < c:
    print("Smallest number is", b)
else:
    print("Smallest number is", c)

a = 15
b = 20
c = 15
if a <= b and a <= c:
    print("Smallest number is", a)
elif b <= a and b <= c:
    print("Smallest number is", b)
else:
    print("Smallest number is", c)

a = int(input("A: "));
b = int(input("B: "));
c = int(input("C: "));
if a < b and a < c:
    print("Smallest number is", a)
elif b < a and b < c:
    print("Smallest number is", b)
else:
    print("Smallest number is", c)

# 15. Leap year
year = 2024
if year % 4 == 0:
    print("This is Leap year")
else:
    print("This is not Leap year")

year = 2022
if year % 4 == 0:
    print("this is Leap year")
else:
    print("This is not Leap year")

year = int(input("Year: "));
if year % 4 == 0:
    print("This is Leap year")
else:
    print("This is not Leap year")


# Level 5- Real Programming Practice

# 16. ATM
balance = 5000
withdraw = 3000
if withdraw <= balance:
    print("withdraw successful")
else:
    print("Insufficient balance")

balance = 5000
withdraw = 7000
if withdraw <= balance:
    print("Withdraw successful")
else:
    print("Insufficient balance")

balance = 5000
withdraw = int(input("Withdraw: "));
if withdraw <= balance:
    print("withdraw successful")
else:
    print("Insufficient balance")

balance = 5000
withdraw = 3000
if withdraw <= balance:
    balance = balance - withdraw
    print("withdraw successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")

# 17. Exam Eligibility
attendance = 85
marks = 50
if attendance >= 75 and marks >=40:
    print("Eligible for exam")
else:
    print("Not eligible for exam")

attendance = 50
marks = 30
if attendance >= 75 and marks >=40:
    print("Eligible for exam")
else:
    print("Not eligible for exam")