# Q1 Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers.

# Attempt 1
# Storing in a list, or range? need counter.

# number = int(input("Enter a number:"))
# sum = 0
# while number != "":
#     sum += number
#     number = int(input("Enter a number:"))
# print(sum)


# Attempt 2 - CLOSE!
# number = " "
# total = 0
# while True:
#     number = (input("Enter a number:"))
#     if number == " ":
#         break
# print(int(total) - 1)

# Attempt 3
# num_list = []
# total = 0

# while True:
#     num = int(input("Enter a number"))
#     num_list.append(num)
#     print(sum(num_list))
#     if num == "":
#         break

#  Attempt 4 (I THINK THIS IS THE ANSWER but it won't accept empty string?)
# sum = 0

# while True:
#     number = int(input("Enter a number:"))
#     if number == "":
#         break
#     sum += number
#     print(sum)

# CORRECT ANSWER
# num_list = []

# while True:
#     num = input("Enter a number")
#     if num == " ":
#         print(sum(num_list))
#         break
#     else:
#         num_list.append(int(num))

# Q2 Ask the user to enter a number. Print all the odd numbers between 0 and that number (inclusive).
# I feel this question is best suited to a for loop?

# maximum = int(input("Enter a number:"))
# number = 1

# while number <= maximum:
#     if (number % 2 != 0):  # if number is divisible by 2 and does not equal 0.
#         print(number)
#         number += 2
#         # loops for 1 all the way through to the max input by user.

# Q3 Select a number. Ask the user to enter a number, output whether their
#   number is less than or greater than the selected number.
#   repeat this process until the user guesses the correct number.

# number = 25
# guess = int(input("Guess the number: "))

# while True:
#     if guess == number:
#         print("Correct!")
#         break
#     elif guess < number:
#         print("Too low!")
#         guess = int(input("Guess the number: "))
#     elif guess > number:
#         print("Too high!")
#         guess = int(input("Guess the number: "))
