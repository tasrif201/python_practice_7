# # Level 1 — Basic

# # 1. Hello World

# print("Hello, World!")

# # 2. Personal Information
# name = "Abdullah"
# age = 27
# country = "Bangladesh"

# print(name)
# print(age)
# print(country)

# name = "Abdullah"
# age = 27
# country = "Bangladesh"

# print("Name:", name)
# print("Age:", age)
# print("Country:", country)

# # 3 & 4 Calculator
# # Addition
# a = 20
# b = 30
# result = a + b
# print(result)

# # subtraction 
# result = a - b
# print(result)

# # Multiplication
# result = a * b
# print(result)

# # Division
# result = a / b
# print(result)

# # Area of Rectangle
# length = 10
# width = 5

# area = length * width

# print(area)

# # Level 2- Conditions

# # 6. Even/odd
# number = 24
# if number % 2 == 0:
#     print("This number is Even")
# else:
#     print("This number is Odd")

# # 7. Positive / Negative / Zero
# number = int(input("Number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("0")

# # 8. Greater Number
# a = 25
# b = 40
# if a > b:
#     print("a is Greater")
# else:
#     print("B is greater")

# # 9. Largest of 3
# a = 20
# b = 35
# c = 15
# if a > b and a > c:
#     print("a is the largest")
# elif b > a and b > c:
#     print("b is the lagerst")
# else:
#     print("c is the largest")

# # 10. Smallest of 3
# a = 20
# b = 35
# c = 15
# if a < b and a < c:
#     print("a is the smallest")
# elif b < a and b < c:
#     print("b is the smallest")
# else:
#     print("c is the smallest")

# # 11. Grade Calculator
# marks = int(input("Marks: "))
# if marks >= 80:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("B")
# elif marks >= 50:
#     print("C")
# elif marks >= 40:
#     print("D")
# else:
#     print("F")

# # 12. ATM
# balance = 5000
# withdraw = 3000
# if withdraw <= balance:
#     balance = balance - withdraw
#     print("Withdraw successful")
#     print("Remaining balance: ", balance)
# else:
#     print("Insufficient balance")

# # Level 3 - Loop

# # 13. Print 1–10

# for i in range (1, 11):
#     print(i)

# # 14. Even Numbers
# for i in range (1, 21):
#     if i % 2 == 0:
#         print(i)

# # 15. Odd Numbers
# for i in range (1, 21):
#     if i % 2 != 0:
#         print(i)

# # 16. Sum 1–10
# total = 0
# for i in range (1, 11):
#     total = total + i
# print("Total: ", total) 

# # 17. Multiplication Table
# number = int(input("Number: "))
# for i in range (1, 11):
#     print(number, "x", i, "=", number * i)

# # 18. Countdown
# for i in range (10, 0, -1):
#     print(i)


# # Level 4 - List and Tuples

# # 19. List Indexing
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# print(fruits[3])
# print(fruits[2])

# # 20. List Slicing
# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[1:4])

# # 21. List Methods
# numbers = [50, 20, 40, 10, 30]
# numbers.sort()
# print("Sorted:", numbers)
# print("Smallest:", min (numbers))
# print("Largest:", max(numbers))

# # 22. List + Loop
# numbers = [10, 20, 30, 40, 50]
# for number in numbers:
#     print(number)

# # 23. List থেকে Even Numbers
# numbers = [10, 15, 20, 25, 30, 35, 40]
# for number in numbers:
#     if number % 2 == 0:
#         print(number)


# # Level 5 — Sets

# # 24. Duplicate Remove
# numbers = [10, 20, 20, 30, 30, 40, 10]
# numbers = set(numbers)
# print(numbers)

# # 25. Common Numbers
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# result = a.intersection(b)
# print(result)


# # Level 6 — Dictionaries
# # 26. Student Information
# student = {
#     "name": "Abdullah",
#     "age": 27,
#     "department": "CSE",
#     "cgpa": 3.50
# }
# print("Name:", student["name"])
# print("Age:", student["age"])
# print("Department:", student["department"])
# print("CGPA:", student["cgpa"])

# # 27. Dictionary Update
# student["city"] = "Dhaka"
# student["cgpa"] = "3.70"
# print(student)

# # 28. Dictionary + If/Else
# student = {
#     "name": "Abdullah",
#     "marks": 75
# }
# if student ["marks"] >= 40:
#     print("Passed")
# else:
#     print("Failed")


# # Level 7 — Challenge

# # 29. Student Result System

# student = {
#     "name": "Abdullah",
#     "marks": [75, 82, 68, 90, 55]
# }

# print("Name:", student["name"])

# print("Marks:")
# for mark in student["marks"]:
#     print(mark)

# total = 0
# for mark in student["marks"]:
#     total = total + mark
# print("Total:", total)

# average = total / len(student["marks"])
# print("Average:", average)

# if average >= 80:
#     print("A+")
# elif average >= 70:
#     print("A")
# elif average >= 60:
#     print("B")
# elif average >= 50:
#     print("C")
# elif average >= 40:
#     print("D")
# else:
#     print("Result: F")


# 30.Mini ATM System

balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
         print("Balance:", balance)
    
    elif choice == 2:
        withdraw = int(input("Enter withdraw amount: "))
        
        if withdraw <= balance:
             balance = balance - withdraw
             print("Withdraw successful")
             print("Remaining Balance:", balance)
        
        else:
            print("Insufficient Balance")

    elif choice == 3:
        deposit = int(input("Enter your deposit amount: "))
        if deposit >= 0:
            balance += deposit
            print ("Balance:", balance)

        else: print("Balance invalid")   

    elif choice == 4:
        print("Thank you")
        break
    
    else:
        print("Invalid option")