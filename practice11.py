# Comprehensions

# 1. List Comprehensions
# List comprehension can be used to create a new list with less code

# normal for loop
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number * number)
print(squares)

# List Comprehension 
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
print(squares)

numbers = [10, 20, 30, 40, 50]
result = [number * 2 for number in numbers]
print(result)

numbers = [10, 20, 30, 40, 50]
result = []
for number in numbers:
    result.append(number * 2)
print(result)

# name length
names = ["abdullah", "Rahim", "karim"]
lengths = []
for name in names:
    lengths.append(len(name))
print(lengths)

names = ["Abdullah", "Rahim", "Karim"]
lengths = [len(name) for name in names]
print(lengths)

# cube practice 
numbers = [1, 2, 3, 4, 5]
cubes = [number * number * number for number in numbers]
print(cubes)

numbers = [1, 2, 3, 4, 5]
cubes =[]
for number in numbers:
    cubes.append(number * number * number)
print(cubes)

# P2
numbers = [10, 20, 30, 40]
result = [number + 5 for number in numbers]
print(result)

numbers = [10, 20, 30, 40]
result = []
for number in numbers:
    result.append(number + 5)
print(result)

# P3 *3
numbers = [2, 4, 6, 8]
result = [number * 3 for number in numbers]
print(result)

numbers = [2, 4, 6, 8]
result = []
for number in numbers:
    result.append(number * 3)
print(result)


# 2. List Comprehension with if condition
# Even number
# normal for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [
    number for number in numbers
    if number % 2 == 0
]
print(even_numbers)

# Odd number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
for number in numbers:
    if number % 2 != 0:
      odd_numbers.append(number)
print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [
    number for number in numbers
    if number % 2 != 0
]
print(odd_numbers)

# example
numbers = [10, 15, 20, 25, 30, 35]
result = [number for number in numbers if number > 20]
print(result)

# p1, p2, p3
numbers = [5, 10, 15, 20, 25, 30, 35, 40]

result = [number for number in numbers if number > 20]
print(result)

multiples_of_10 = [
    number for number in numbers
    if number % 10 == 0
]
print(multiples_of_10)

odd_numbers = [
    number for number in numbers
    if number %2 != 0
]
print(odd_numbers)


# 3. List comprehension with if/else

numbers = [1, 2, 3, 4, 5,]
results = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]
print(results)

result = [number for number in numbers if number > 3]
print(result)

result = ["Big" if number > 3 else "Small" for number in numbers]
print(result)

# 4. Dictonary Comprehension
numbers = [1, 2, 3, 4, 5]
squares = {
    number : number * number
    for number in numbers
}
print(squares)

# Normal loop vs Dictionary Comprehension
numbers = [1, 2, 3]
squares = {}
for number in numbers:
    squares[number] = number * number
print(squares)

numbers = [1, 2, 3]
squares = {number: number * number for number in numbers}
print(squares)

# P1
numbers = [2, 3, 4]
cubes = {number: number * number * number for number in numbers}
print(cubes)

numbers = [2, 3, 4]
cubes = {number: number ** 3 for number in numbers}
print(cubes)

# 5. Dictionary Comprehension with If condition
marks = {
    "Abdullah": 85,
    "Rahim": 35,
    "Karim": 70,
    "Hasan": 25
}

passed = {
    name : mark
    for name, mark in marks.items()
    if mark >= 40
}
print(passed)

prices = {
    "Pen": 20,
    "Book": 150,
    "Bag": 800,
    "Pencil": 10
}
expensive = {
    name : price
    for name, price in prices.items()
    if price >= 100
}
print(expensive)

# 6. Lambda
# Lambda is a small and anonymous (nameless) function, which is usually written in a single line
def square(number):
    return number * number
print(square(5))

square = lambda number: number * number
print(square(5))

add = lambda a, b: a + b
print(add(10,20))

# Lambda + Comprehensive
numbers = [1, 2, 3, 4, 5]
square = lambda x: x * x
result = [square(x) for x in numbers]
print(result)

numbers = [1, 2, 3, 4, 5]
result = [x * x for x in numbers]
print(result)

#  7. Lambda + map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number * number, numbers))
print(squares)

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)

# 8. Lambda +. filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)
print(even_numbers)

numbner = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(
    filter(lambda number: number % 2 != 0, numbers)
)
print(odd_numbers)

# 9. List Cpmprehensive vs map() and filter()
# number square
# List Comprehensive
numbers = [1, 2, 3, 4, 5]
result = [number * number for number in numbers]
print(result)

# map() and lambda
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda number: number * number, numbers))
print(result)

# Even and Odd
# List. Comprehensive
numbers = [1, 2, 3, 4, 5, 6]
result = [number for number in numbers if number % 2 == 0]
print(result)

numbers = [1, 2, 3, 4, 5, 6]
result = [number for number in numbers if number % 2 != 0]
print(result)

# filter() and Lambda
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda number: number % 2 == 0, numbers))
print(result)

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda number: number % 2 != 0, numbers))
print(result)

# Problem
# Problem 1: List Comprehensive
# Find the double of each number in this list

numbers = [5, 10, 15, 20, 25]
result = [number * 2 for number in numbers]
print(result)

# Problem 2: List Comprehensive + Condition
# Extract only the numbers greater than 10 from this list

numbers = [5, 12, 8, 20, 3, 15, 25]
result = [number for number in numbers if number > 10]
print(result)

# Problem 3: Dictionary Comprehensive
# Create a dictionary using the square of each number un this list.

numbers = [2, 3, 4, 5]
result = {number: number * number for number in numbers}
print(result)

# Problem 4: Dictionary Comprehensive + Condition

marks = {
    "Abdullah": 85,
    "Rahim": 35,
    "Karim": 70,
    "Hasan": 25,
    "Nila": 90
}
passed_students = {
    name: score
    for name, score in marks.items()
    if score >= 40
}
print(passed_students)

# Problem 5: Lambda

cube = lambda number: number * number * number
print(cube(3))

# Problem 6

# list comprehensive odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

# list comprehensive all number square
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers]
print(squares)

# lambda + filter() even number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)