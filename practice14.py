# File Handling (Read/Write Text Files)

file = open("student.txt", "w")

# 
# file = open("student.txt", "w")
file.write("Hello Python")
file.close()

# write()
with open("student.txt", 'w') as file:
    file.write("Name: Abdullah\n")
    file.write("Subject: Python\n")
    file.write("Goal: Learn Programming\n")
print("File written successfully!")

# read()
with open("student.txt", "r") as file:
    content = file.read()
print(content)

# append()
with open("student.txt", "a") as file:
    file.write("Status: Learing Python\n")
print("New information added!")

# readlines()
with open("student.txt", "r") as file:
    lines = file.readlines()
print(lines)

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

# try-except with File Error Handle
try:
    with open("stduent.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not Found!")


# Practice task: Personal Notes App

# Step 1: Take input
name = input("Enter your name: ")
note = input("Enter your note: ")

# Step 2: Save information to files
with open("notes.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Note: {note}\n")

print("\nNote saved successfully!")

# Step 3: Read information from file
with open("notes.txt", "r") as file:
    content = file.read()

# Step 4: Display save information
print("\nYour saved note:")
print(content)