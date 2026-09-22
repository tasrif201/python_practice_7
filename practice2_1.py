#Level-1 Basic Data Types

#Practice 1- Personal Information
name = "Abdullah Al Amin "
age = 26
country = "Germany"

print(name)
print(age)
print(country)

#Practice 2- Check Data Types
name = "Abdullah"
age = 26
height = 5.11
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#Practice 3- Different Numnbers
a = 10
b = 20
c = 30.5

print(type(a))
print(type(b))
print(type(c))


#Level 2- Type Coversion

#Practice 4- String ---> Integer
age = "26"
print(type(age))
age = int(age)
print(type(age))
print(age)

#Practice 5- Integer ---> String
age = 26
print(type(age))
age = str(age)
print(type(age))

#practice 6- Integer ---> Float
number = 10
number = float(number)
print(number)
print(type(number))

# Practice 7- Float ---> Integer
price = 99.99
price = int(price)
print(price)
print(type(price))


# Level 3- Calculations

# Practice 8- Add Two Numbers
num1 = 40
num2 = 70
result = num1 + num2
print(result)

# Practice 9- String Numbers
num1 = "40"
num2 = "70"
result = num1 + num2
print(result)

num1 = "40"
num2 = "70"
result = int(num1) + int(num2)
print(result)


# Level 4- Boolean Practice

# Practice 10
age = 25
print(age > 18)
print(age < 18)
print(age == 25)

# Practice 11
is_student = True
print(is_student)
print(type(is_student))

# Practice 12
age = 15
is_adult = age >= 18
print(is_adult)

age = 26
is_adult = age >= 18
print(is_adult)

age = 18
is_adult = age >= 18
print(is_adult)


# Challenge Level

# Challenge 1
name = "Abdullah Tasrif"
print(type(name))
print(name)

age = 26
print(type(age))
print(age)

cgpa = 3.28
print(type(cgpa))
print(cgpa)

country = "United States of America"
print(type(country))
print(country)

is_student = True
print(is_student)
print(type(is_student))


# Challenge 2
number = "100"
num3 = 50
result = int(number) + num3
print(result)


# Challenge 3
price = "99.50"
price1 = 10.50
result = float(price) + price1
print(result)


# Challenge 4 
a ="10"
b = 5
result = int(a) + b
print(result)

a = "10"
b = 5
print(int(a) + b)


# Challenge 5
age = 20 
is_adult = age >= 18
print(is_adult)