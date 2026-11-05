# CSV & JSON (Data File Handling)

# CSV = Comma-Separated Values

# Python with CSV

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "city"])
    writer.writerow(["Abdulah", 27, "Dhaka"])
    writer.writerow(["Rahim", 25, "Chittagong"])
    writer.writerow(["Karim", 24, "Sylhet"])

print("CSV file created successfully")

# Data Read CSV file

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# only students

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    next(reader) 

    for row in reader:
        print(row[0])

# DictReader
# only data read

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(student["name"], student["city"])


# JSON = JavaScript Object Notation

# Puthon with JSON file

import json

student = {
    "name": "Abdullah",
    'age': 27,
    "city": "Dhaka",
    "skills": ["Pytjon", "Software Testing", "Cybersecurity"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully")

# Data read JSON file

import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(student["name"])
print(student["age"])
print(student["skills"])

# dumps(), dump(), load(), loads()

import json
student = {"name": "Abdullah", "age": 27}

json_text = json.dumps(student)

print(json_text)
print(type(json_text))


import json
json_text = '{"name": "Abdullah", "age": 27}'

student = json.loads(json_text)

print(student["name"])
print(type(student))


# Practice Project: Student Data Manager

# Task A : CSV - Student Information Manager

import csv

# step 1 : user information
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Step 2: Save Data
with open("students.csv", "a", newline="") as file:

    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["Name", "Age", "City"])

    writer.writerow([name, age, city])

print("\nData saved successfully")

# Step 3: Read Data

print("\nStudent Information:")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# Part B: JSON - Student Programming Language Manager

import json

# Step 1: User Information

name = input("Enter your name: ")

language = input("Enter your programming language: ")

# Step 2: Create Dictionary
student = {
    "name": name,
    "programming_language": language
}

# Step 3: Save JSON Data
with open("student1.json", "w") as file:

    json.dump(student, file, indent= 4)

print("\nData saved successfully")

# Step 4: Read JSON Data
with open("student1.json", "r") as file:

    data = json.load(file)

# Step 5: Display Data 
print("\nName:", data["name"])

print("Programing Language:", data["programming_language"])