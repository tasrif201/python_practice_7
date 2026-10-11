# Arguments	Default, keyword, *args, **kwargs
# 1. Default Argument
# If no argument is provided, the function uses a default vaule. This is why we use a defaut argument.
def greet(name="Abdullah"):
    print("Hello", name)
greet()
greet("Rahim")

def introduce(name, country="Bangladesh"):
    print(name, "is from", country)

introduce("Abdullah")
introduce("John", "Canada")

# 2. Keyword Arguments
def student(name, age):
    print(name, age)
student("Abdullah", 27)
student(age= 27, name= "Abdullah")

def introduce(name, age, country):
    print("Name:", name)
    print("Age:", age)
    print("Country:", country)

introduce(
    country="Bangladesh",
    name="Abdullah",
    age=27
)

# 3. *args
def add(*args):
    total = 0

    for number in args:
        total = total + number
    
    return total
print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50))
print(add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

def test(*args):
    print(args)
test(10, 20, 30)

#  4. **kwargs
def student_info(**kwargs):
    print(kwargs)

student_info(
    name="Abdullah",
    age=27,
    department="CSE"
)

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_info(
    name="Abdullah",
    age=27,
    department="CSE"
)

# 5.*args vs **kwargs
def test(*args):
    print(args)
test(10, 20, 30)

def test(**kwargs):
    print(kwargs)
test(name="Abdullah", age=27)


# 6. All together

def student(name, age=18, *args, **kwargs):
    print("Name:", name)
    print("Age:", age)
    print("Extra:", args)
    print("Information:", kwargs)

student(
    "Abdullah",
    27,
    "CSE",
    "AIUB",
    city="Dhaka",
    country="Bangladesh"
)

# Practice 1
def greet(name="Abdullah"):
    print("Hello", name)
greet()
greet("Rahim")

# Practice 2
def add(*args):
    total = 0

    for number in args:
        total = total + number
    
    return total
print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50))

# Practice 3
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_info(
    name="Abdullah",
    age=27,
    department="CSE"
)