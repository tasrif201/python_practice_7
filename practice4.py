# Loops

print(1)
print(2)
print(3)
print(4)
print(5)

for i in range(1, 6):
    print(i)

# for loop
# for loop means variable is sequence

for i in range(5):
    print(i)

# range
for i in range(1,5):
    print(i)

# print 1 - 10
for i in range (1, 11):
    print(i)

# Even number print
for i in range (1, 11):
    if i % 2 == 0:
        print(i)

# Off number print
for i in range (1, 11):
    if i % 2 != 0:
        print(i)

# for loop print
names = ["Abdullah", "Aizan", "Rahim", "Karim"]
for name in names:
    print(name)

# list
# list means which all together many value
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# While lopp
# while loop means as long as condition is true, the loop wil continue running.
count = 1
while count <= 5:
    print(count)
    count = count + 1

break
# break means loop is totally off
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 11):
    if i == 9:
        break
    print(i)

# Cotinue
# continue just present iteration skip.but loop does not off
# continue = skip this one
for i in range(1, 7):
    if i == 4:
        continue    
    print(i)

# for + break
for i in range (1,11):
    if i == 8:
        break
    print(i)


# for + continue
for i in range (1, 15):
    if i == 7:
        continue
    print(i)


# while + break
count = 1
while count <= 10:
    if count == 6:
        break
    print(count)
    count = count + 1

count = 2
while count <= 10:
    if count == 8:
        break
    print(count)
    count = count + 3

# while + continue 
count = 1
while count <= 5:
    if count == 3:
        continue
    print(count)
    count = count + 1

count = 1
while count <= 5:
    if count == 3:
        count = count + 1
        continue 
    print(count)
    count = count + 1

# Practice 1 - 1 -10 plus total
total = 0
for i in range (1, 11):
    total = total + i
print("Total:", total)

# Practice 2 - Multiplication table
number = 5
for i in range (1, 11):
    print(number, "x", i, "=", number * i)

number = 20
for i in range (1, 11):
    print(number, "x", i, "=", number * i)

# User input + loop
number = int(input("Enter a number: "))
for i in range (1, 11):
    print(number, "x", i, "=", number * i)


# problem 1
for i in range (1, 21):
    print (i)

# problem 2
for i in range (1, 21):
    if i % 2 == 0:
        print(i)

# problem 3
for i in range (1, 21):
    if i % 2 != 0:
        print(i)

number = 1
for i in range (1, 21):
    if i % 2 == 0:
        print(i)
    number = number + 1

# Problem 4 
total = 0
for i in range (1, 11):
    total = total + i
print("total:", total)

# problem 5
number = int(input("Enter a number: "))
for i in range (1, 11):
    print(number, "x", i, "=", number * i)

# problem 6
for i in range (1,11):
    if i == 5:
        break
    print(i)

count = 1
while count <= 10:
    if count == 6:
        break
    print(count)
    count= count + 1



# problem 7 
for i in range (1, 11):
    if i == 5:
        continue
    print(i)

count = 1
while count <= 10:
    if count == 5:
        count = count + 1
        continue
    print(count)
    count = count + 1