# Problem 1- Indexing
names = ["Abdullah", "Rahim", "Karim", "Hasan"]
print(names[0])
print(names[2])
print(names[3])

# Promlem 2- Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

# Problem 3- Append
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

# Problem 4- Remove
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)

# Problem 5- Sort
numbers = [50, 40, 30, 20, 10]
numbers.sort()
print(numbers)

# Problem 6- List + Loop
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# Problem 7- Tuple
countries = ("Bangladesh", "Norway", "Finland", "Germany")
print(countries[1])


# Level 1- Indexing
Problem 1
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[2])

# Problem 2
names = ["Abdullah", "Rahim", "Karim", "Hasan"]
print(names[-1])

# Problem 3
numbers =[10, 20, 30, 40, 50]
print(numbers.index(40))


# Level 2- Slicing
# Problem 4
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])

# Problem 5
names = ["A", "B", "C", "D", "E"]
print(names[2:])

# Problem 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:8:2])


# Level 3- List Method
# Problem 7
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

# Problem 8
fruits = ["Apple", "Mango"]
fruits.insert(1, "Banana")
print(fruits)

# Problem 9
colors = ["Red", "Green", "Blue", "Yellow"]
colors.remove("Blue")
print(colors)

# Problem 10
numbers = [10, 20, 30, 40]
numbers.pop(2)
print(numbers)


# Level 4- List + Loop
# Problem 11
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# Problem 12
numbers = [10, 15, 20, 25, 30, 35]
for number in numbers:
    if number % 2 == 0:
        print(number)

# Problem 13
numbers = [10, 15, 20, 25, 30, 35]
for number in numbers:
    if number % 2 != 0:
        print(number)


# Level 5- Tuple
# Problem 14
countries = ("Bangladesh", "Norway", "Finland", "Germany")
print(countries[2])

# Problem 15
countries = ("Bangladesh", "Norway", "Finland", "Germany")
print(countries.index("Germany"))

# Problem 16
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])



# Challenge
numbers = [25, 10, 45, 30, 15, 50]

print(numbers)

numbers.sort()
print(numbers)

print(numbers[0])

print(numbers[-1])

print(numbers.index(30))
