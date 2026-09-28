# scope, lamba, map(), and filter(),(intro)
# 1. Scope
# Scope means where a variable can be accessed.

# Local scope 
# A variable created inside a function can generally only be used within that function.
def my_function():
    name = "Abdullah"
    print(name)
my_function()

# Global Scope
# If a variable is created outside a function, it is in the global scope.
name = "Abdullah"
def my_function():
    print(name)
my_function()

# 2. Lambda
# Lambda is a small and generally one-line function.
add = lambda a, b: a+b
print(add(10, 30)) 

square = lambda x : x * x
print(square(5))

# 3. map()
# Using map(), you can apply the same function to every item in a list.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x : x * x, numbers))
print(squares)

# 4. filter()
# filter() is used to extract only the values from a list that satisfy our condition.
numbers = [1, 2,3, 4, 5]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)

# 5. map() vs filter()
# map()
# Changes/processes the value of each item.
numbers = [1, 2, 3]
result = list(map(lambda x : x * 2, numbers))
print(result)

# filter()
# Selects items based on a condition.
numbers = [1, 2, 3, 4]
result = list(filter(lambda x: x > 2, numbers))
print(result)

# 6. All together
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squares = list(map(lambda x: x * x, even_numbers))

print(even_numbers)
print(squares)

# Practice 
# Practice 1 - Scope
name = "Abdullah"
def test():
    age = 27
    print(name)
    print(age)
test()

# Practice 2 — Lambda
cube = lambda x: x ** 3
print(cube(3))

# Practice 3 — map()
numbers = [10, 20, 30, 40, 50]
result = map(lambda x: x * 2, numbers)
print(list(result))

# Practice 4 — filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 != 0, numbers)
print(list(result))