# Q1 Ask the user for a number. Use a loop to print the times tables for that number.
# a)
# number = input("Enter a number:")
# for count in range(1, 4):
#    multiplication = (int(count) * (int(number)))
#    print(f"{number} * {count} = {multiplication}")

# b)
# number = input("Enter a number:")
# for count in range(1, 8):
#     multiplication = (int(count) * (int(number)))
#     print(f"{number} * {count} = {multiplication}")

# c)
# number = input("Enter a number:")
# for count in range(1):
#    multiplication = (int(count) * (int(number)))
#    print(multiplication)

# Q2 Ask the user for a number. Use a for loop to sum from 0 to that number.
# a)

# HELP: Correct answer but the number of prints is equivalent to the the number of values within the range!!!?
start = 0
end = int(input("Enter a number:"))
for item in range(end):
    total = sum(range(start, end + 1))
    break
    print(int(total))

# Q3 Given a list, use a for loop to sum all the numbers in the list.
# a)
# random_numbers = [3, 5, 9, 1]

# total = 0
# # for num in random_numbers:
# #     total = total + num
# print(total)

# b)
# random_numbers = [-3, -5, 9, 1]

# total = 0
# for num in random_numbers:
#     total = total + num
# print(total)

# c)
# random_numbers = []

# total = 0
# for num in random_numbers:
#     total = total + num
# print(total)
