# Set & Dictionaries
# Set : Keep the unique values
# Set methods : aad(), remove(), Discard(), union(), intersection()
# Dictionary : Store date in key-value format.
# Dictionary methods: keys(), values(), items(), get(), update(), pop()
# Practical Use: Student, Product, User data etc.abs

# 1. Set
# A set is a collection where duplicate values are not stored.
numbers = {10, 20, 30, 20, 10}
print(numbers)

# 2. List vs Set
# List 
numbers = [10, 20, 20, 30]
print(numbers)
# Set
numbers = {10, 20, 20, 30}
print(numbers)

# 3. Set (toiri kora)
fruits = {"Apple", "Banana", "Mango"}
print(fruits)
# The order of the output may not be fixed
# A set does not have an index

#  4. add()
fruits = {"Apple", "Mango"}
fruits.add("Banana")
print(fruits)

# 5. remove()
fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Banana")
print(fruits)

# 6. discard()
fruits = {"Apple", "Banana", "Mango"}
fruits.discard("Orange")
print(fruits)

fruits = {"Apple", "Banana", "Mango"}
fruits.discard("Apple")
print(fruits)

# 7. Set Length
numbers = {10, 20, 30, 40}
print(len(numbers))

# 8. in by search
fruits = {"Apple", "Banana", "Mango"}
print("Apple" in fruits)

fruits = {"Apple", "Banana", "Mango"}
print("Orange" in fruits)

# 9. Set + Loop
fruits = {"Apple", "Banana", "Mango"}
for fruit in fruits:
    print(fruit)

numbers = {10, 20, 30, 40, 50}
for number in numbers:
    print(number)

numbers = {10, 20, 10, 30, 20}
for number in numbers:
    print(number)

# 10. Union
# Use union() to combine all the unique items feom two sets.
a = {1, 2, 3}
b = {3, 4, 5}
result = a.union(b)
print(result)

# 11. Intersection
#  Use intersection() to find the common items between two sets.
a = {1, 2, 3}
b = {2, 3, 4}
result = a.intersection(b)
print(result)

# 12. Practical Example- Duplicate Remove
numbers = [10, 20, 20, 30, 30, 40, 10]
unique_numbers = set(numbers)
print(unique_numbers)

# Dictionary
# 13. Dictionary
student = {
    "name": "Abdullah",
    "age": 27,
    "department": "CSE" 
} 

# 14. Dictonary to Value print 
student = {
    "name": "Abdullah",
    "age": 27,
    "department": "CSE" 
} 
print(student["age"])
print(student["department"])
print(student["name"])

# 15. Dictionary Value Change
student = {
    "name": "Abdullah",
    "age": 27
}
student["age"] = 28
print(student)

# 16. Add new key/value
student = {
    "name": "Abdullah",
    "age": 27
}
student["city"] = "Dhaka"
print(student)

#  17. get()
# Can use get() to safety retrieve a value from a key
student = {
    "name": "Abdullah",
    "age": 27
}
print(student.get("name"))
print(student.get("email"))

# 18. keys()
student = {
    "name": "Abdullah",
    "age": 27,
    "city": "Dhaka"
}
print(student.keys())

# 19. Values()
student = {
    "name": "Abdullah",
    "age": 27,
    "city": "Dhaka"
}
print(student.values())

# 20. items()
student = {
    "name": "Abdullah",
    "age": 27,
    "city": "Dhaka"
}
print(student.items())

# 21. Dictionary + Loop
student = {
    "name": "Abdullah",
    "age": 27,
    "city": "Dhaka"
}
for key, value in student.items():
    print(key, ":", value)

# 22. update()
# To add new data or change exiting data simultaneously
student = {
    "name": "Abdullah",
    "age": 28
}
student.update({
    "age": 27,
    "city": "Dhaka"
})
print(student)

# 23. pop()
# To remove a key from a dictionary
student = {
    "name": "Abdullah",
    "age": 27,
    "city": "Dhaka"
}
student.pop("age")
print(student)

# 24. Practical Example - Student Data
student = {
    "name": "Abdullah",
    "age": 27,
    "department": "CSE",
    "cgpa": 3.48
}
print("Name:", student["name"])
print("Age:", student["age"])
print("Department:", student["department"])
print("CGPA:", student["cgpa"])

# 25. Dictionary + if/else
student = {
    "name": "Abdullah",
    "marks": 75
}
if student ["marks"] >= 40:
    print("Passed")
else:
    print("failed")