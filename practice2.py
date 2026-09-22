# Data Types - String, int, float, bool, conversion

#string(str)
name = "Abdullah"
country = "Bangladesh"
university = "AIUB"

print(type(name))

#interger(int)
age = 26
student = 25
year = 2026

print(type(age))

#float
#Decimal number = float
price = 99.99
cgpa = 3.48
height = 5.11

print(type(cgpa))

#Boolean
#bool= true/false
is_student = True
is_married = False

print(type(is_student))
print(type(is_married))

print(age > 18)
print(age > 30)

#type conversion
#type conversion is one data type to change another data type
age = "25"
print(type(age))

age = "26"
age = int(age)
print(type(age))

#Common type covertion functions
#str
age = 26
age = str(age)
print(type(age))

#int
number = "50"
number = int(number)
print(type(number))

#float
number = 10
number = float(number)
print(type(number))

#bool
number = 10
print(bool(number))