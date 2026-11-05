# import random

# number = random.randint(1, 100)

# print("Your random number is:", number)


import random

secret_number = random.randint(1, 10)

guess = int(input("Guess the number (1-10): "))

if guess == secret_number:
    print("Congratulations! You won!")

else:
    print("Sorry! The correct number was:", secret_number)