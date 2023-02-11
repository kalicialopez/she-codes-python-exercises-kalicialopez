def create_greeting(name):
    greeting = f"Hello, {name}"
    return greeting


print(create_greeting("chilli"))
print(create_greeting("Daisy Sparkles"))

# Challenge: Write a function that takes an integer as a parameter and returns the integer multiplied by 3.


def number(value):
    product = int(value) * 3
    return product


print(number(3))


# Challenge: Write a function that takes an integer as a parameter and returns the equation for integer multiplied by 3.


# Challenge: Write a function that converts length in cm to length in inches.
def convert_cm_to_in(length_cm):
    length_in_inches = length_cm / 2.54
    return length_in_inches


print(convert_cm_to_in(3))

# Challenge: Write a function that converts length in in to length in cm.


def convert_in_to_cm(length_in):
    length_in_cm = length_in * 2.54
    return length_in_cm


print(convert_in_to_cm(4))

# Challenge: Write a function that calculates the mean.


def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean


print(calculate_mean(3.5, 4.2))

# If i wanted to use this mean elsewhere, I would convert it into a variable.

use_mean = calculate_mean(3, 4)

print(use_mean * 2)

# Amanda's Code for functions

# def create_greeting(name):
#     greeting = f"Hello, {name}"
#     return greeting
# print(create_greeting("Chilli"))
#
# name = input("What is your name? ")
# print(create_greeting(name))
# EXERCISE - FUNCTION THAT TAKES AN INTEGER AS A PARAMETER AND OUTPUTS INTEGER TIMES 3
# def times_three(number):
#     return number * 3
# print(times_three(5))
# print(times_three(7))
# EXAMPLE
# def convert_cm_to_in(length_cm):
#     length_in_inches = length_cm / 2.54
#     return length_in_inches
# print(convert_cm_to_in(20))
# def convert_in_to_cm(length_in):
#     length_in_cm = length_in * 2.54
#     return length_in_cm
# print(convert_in_to_cm(7))
# EXAMPLE WITH MULTIPLE PARAMETERS, AND MULTIPLE RETURN ITEMS
# def calculate_mean(a, b):
#     total = a + b
#     mean = total / 2
#     return mean, total
# return [mean, total] - Returns a list
# print(calculate_mean(3,4))
# EXERCISES
# Q1
# def temp_converter(f_temp):
#     c_temp = (f_temp - 32) * 5 / 9
#     return c_temp
# print(temp_converter(32))
# print(temp_converter(0))
# print(temp_converter(350))
# Q2
# def odd_even(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
# print(odd_even(2))
# print(odd_even(7))
# print(odd_even(-1))
# Q3
# def calculate_mean(numbers):
#     sum = 0
#     counter = 0
#     for num in numbers:
#         sum += num
#         counter += 1
#     return sum / counter
# print(calculate_mean([4, 3, 2, 6]))
# print(calculate_mean([10, 5, 6]))
# Q4
