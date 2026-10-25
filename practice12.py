# Strings, Strings methods and manipulation

# 1. What is string?
# A string is a text consisting of one more characters, written inside quotation marks.
name = "Abdullah"
country = "Bangladesh"
age = "27"
message = "I am learning Python"

print(name)
print(age)
print(country)
print(message)

# 2. String Indexing
name = "Python"
print(name[0])
print(name[1])
print(name[5])

# Negative Indexing
name = "Python"
print(name[-1])
print(name[-3])
print(name[-4])


# 3. Strinf Slicing
text = "Programming"
print(text[0:4])
print(text[0:7])
print(text[3:])
print(text[:5])

text= "Python"
print(text[:])
print(text[::-1])
print(text[::-2])


# 4. Important String Methods
# upper()
text = "hello python"
print(text.upper())

# lower()
text = "HELLO PYTHON"
print(text.lower())

# title()
text = "learn python programming"
print(text.title())

# strip()
text = "  Abdullah  "
print(text.strip())

# replace()
text = "I like Java"
print(text.replace("Java", "Python"))

# capitalize()
text = "python programming"
result = text.capitalize()
print(result)

# count()
text = "python programming"
result = text.count("python")
print(result)

# find()
text = "python programming"
result = text.find("programming")
print(result)

# startswith()
text = "python programming"
result = text.startswith("python")
print(result)

# endswith()
text = "file.txt"
result = text.endswith(".txt")
print(result)

text = "file.pdf"
result = text.endswith(".txt")
print(result)

# join()
words = ["I", "love", "Python"]
result = " ".join(words)
print(result)

letters = ["a", "b", "c"]
result = "-".join(letters)
print(result)

# isalpha()
text = "hello"
result = text.isalpha()
print(result)

# isdigit()
text = "2026"
result = text.isdigit()
print(result)

# All together

text = "python programming"

print(text.capitalize())
print(text.count("python"))
print(text.find("programming"))
print(text.startswith("python"))
print("hello".isalpha())
print("2026".isdigit())

# 5. String Concatenation
first_name = "Abdullah"
last_name = "Al Amin"
full_name = first_name + " " + last_name
print(full_name)

# String + Number
# Solve 1: str()
age = 27
print("My age is " + str(age))

# Solve 2: f-string
age = 27
print(f"My age is {age}")

# 6. String Immutability
text = "Python"
text = "J" + text[1:]
print(text)

# 7. Practical Project - Username Cleaner

username = input("Enter you name: ")

username = username.strip()
username = username.upper()

print("Username:", username)


# Practice Problem
# Practice 1: upper()
text = "  hello python  "
print(text.strip().upper())

# Problem 1: lower()
text = "HELLO PYTHON"
result = text.lower()
print(result)

# Problem 2: replace()
text = "I love Java"
result = text.replace("Java", "Python")
print(result)

# Problem 3: Slicing
text = "Abdullah Al Amin"
result = text[0:8]
print(result)

# Problem 4: strip(), lower()
email = input("Enter you email: ")
result = email.strip().lower()
print(result)