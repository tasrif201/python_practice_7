# Python : List & Tuples

# 1. List = Storing multiple data together
# 2. indexing = Finding a specific item
# 3. Slicing = Extracting a portion of a list
# 4. list Methods = append(), remove(), insert(), porp(), sort()
# 5. Tuples = A data collection like a list, but it can not be modified

# 1. List
# A list is used to store multiple values in a single variable
# and a list can also contain different types of data
fruits = ["Apple", "Banana", "Mango", "Orange"]
student = ["Abdullah", 27, 3.28, True]

# 2. List indexing 
# in a Python list, each item has an index number
# The index strats from 0
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0])
print(fruits[3])

# 3. Negative Indexing
# In python, indexing can also be done from the end of list.
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[-1])
print(fruits[-4])

# 4. List Item Change 
# List item can be changed
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)

# 5. List Length
#  use len() to find out how many items are in a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(len(fruits))

# 6. List Slicing
# Slicing = Extracting a portion of a list
numbers = [10, 20, 30, 40 , 50, 60, 70, 80, 90, 100, 200]
print(numbers[0:4])

#7. More example slicing
# Frist 2
numbers = [10, 20, 30, 40 , 50, 60, 70, 80, 90, 100, 200]
print(numbers[:2])

# 2 or any to last
numbers = [10, 20, 30, 40 , 50, 60, 70, 80, 90, 100, 200]
print(numbers[5:])
print(numbers[2:])

# full list copy
print(numbers[:])

# 8. Step Slicing
# list[start:stop:step]
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[0:6:2])

# 9. List in search 
#  use in to check weather an item exists in a list
fruits = ["Apple", "Banana", "Mango"]
print("Mango" in fruits)
print("Orange" in fruits)

# 10. append()
# append() is used to add a new item to the end of a list.
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

# 11. insert()
# We use insert() to add an item at a specific position.
fruits = ["Apple", "Mango"]
fruits.insert(1, "Banana")
print(fruits)

fruits = ["Apple", "Mango"]
fruits.insert(3, "Banana")
print(fruits)

fruits = ["Apple", "Mango", "Orange"]
fruits.insert(2, "Banana")
print(fruits)

# 12. remove()
# To remove a specific value
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)

# 13. pop()
# pop() can remove an item using its index
fruits = ["Apple", "Banana", "Mango"]
fruits.pop(1)
print(fruits)

fruits = ["Apple", "Banana", "Mango"]
fruits.pop()
print(fruits)

#14. sort()
# number sort 
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)
# string sort
names = ["Karim", "Abdullah", "Rahim"]
names.sort()
print(names)

# 15. reverse()
# To reverse the order of a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print(numbers)

#16. count()
# To find out how many times a value appears:
numbers = [10, 20, 30, 10, 20, 10]
print(numbers.count(30))

numbers = [10, 20, 30, 10, 20, 10]
print(numbers.count(20))

numbers = [10, 20, 30, 10, 20, 10]
print(numbers.count(10))

#17. index()
# To find out which index an item is at:
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits.index("Orange"))

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits.index("Apple"))

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits.index("Mango"))

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits.index("Banana"))

# 18. clear()
# To empty the entire list:
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.clear()
print(fruits)

# 19. List + Loop
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(fruit)

fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(fruits)

#20. Tuple
# tuple look like similiar to list
# tuple syntax ()
# fruits =("Apple", "Banana", "Mango")
# fruits[0] = "Orange"
# Because the values in a tuple cannot be changed.

# 21. List vs Tuple
# list: syntax [], change, add, remove, indexing, slicing, loop
# tuple: syntax (), indexing, slicing, loop
# list = changeable
# tuple = unchangeable

# 22. Tuple indexing
colors = ("Red", "Green", "Blue", "White")
print(colors[2])
print(colors[1])
print(colors[3])
print(colors[0])

# 23. tuple slicing
numbers =(10, 20, 30, 40, 50, 60)
print(numbers[1:4])

# Tuple Method
# count
numbers = (10, 20, 30, 20, 10, 20)
print(numbers.count(20))
print(numbers.count(10))

# index
numbers = (10, 20, 30, 40)
print(numbers.index(30))