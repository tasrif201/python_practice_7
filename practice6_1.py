# Practice Problem
# Problem 1- Set
numbers = {10, 20, 20, 30, 40, 40, 50}
print(numbers)

# Problem 2- Set Add
fruits = {"Apple", "Banana"}
fruits.add("Mango")
print(fruits)
fruits.add("Orange")
print(fruits)

# Problem 3- Set Remove
colors = {"Red", "Green", "Blue", "Yellow"}
colors.remove("Green")
print(colors)

# Problem 4- Intersection
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

result = a.intersection(b)
print(result)

# Problem 5- Dictionary
student = {
    "name": "Abdullah",
    "age": 27,
    "department": "CSE",
    "cgpa": 3.50
}
print(student["name"])
print(student["department"])
print(student["cgpa"])

# Problem 6 — Dictionary Update
student = {
    "name": "Abdullah",
    "age": 27,
    "department": "CSE",
    "cgpa": 3.50
}

student["city"] = "Dhaka"
student["cgpa"] = 3.70

print(student)

# Problem 7 — Dictionary Loop 
student = {
    "name": "Abdullah",
    "age": 27,
    "department": "CSE"
}

for key, value in student.items():
    print(key, ":", value)

# Challenges
student = {
    "name": "Abdullah",
    "marks": 75,
    "subjects": ["Python", "Networking", "Security"]
}

print(student["name"])

print(student["marks"])

print(student["subjects"][0])

if student["marks"] >= 40:
    print("Passed")
else:
    print("Failed")

for key, value in student.items():
    print(key, ":", value)