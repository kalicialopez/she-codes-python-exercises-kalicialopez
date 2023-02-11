# a) The dictionary below represents the cost of individual items in the supermarket. A separate dictionary is given in the table below, this dictionary represents the quantity of each item purchased. Use these two dictionaries to write a program that outputs the cost of each item.
# groceries = {"Baby Spinach": 2.78, "Hot Chocolate": 3.70, "Crackers": 2.10,
#              "Bacon": 9.00, "Carrots": 0.56, "Oranges": 3.08}

# quantity = {"Baby Spinach": 1, "Hot Chocolate": 3,
#              "Crackers": 2, "Bacon": 1, "Carrots": 4, "Oranges": 2}

# Q4 Write a function that takes two parameters; The unit price of an
#  item, and how many units were purchased. Return the total cost as
# a string.

# def total_cost(unit_price, number):
#     cost = unit_price * number
#     return cost
# print(total_cost(4.25, 3))

##############################
# Method 1 - Using dictionary comprehension + keys
# Example to demonstrate working of
# Dictionary Keys Product
# Using dictionary comprehension + keys()

# # Initialize dictionaries
# test_dict1 = {'gfg': 6, 'is': 4, 'best': 7}
# test_dict2 = {'gfg': 10, 'is': 6, 'best': 10}

# # # printing original dictionaries. Must convert the keys and values in the dictionary into strings first.
# print(str(test_dict1))
# print(str(test_dict2))

# # # Using dictionary comprehension + keys()
# # # Dictionary Keys Product
# # # Unsure about (key, 0)
# product = {test_dict2[key] * test_dict1.get(key, 0)
#            for key in test_dict2.keys()}

# # printing result
# print(str(product))

##################################
# pseudo code
# quantity, item, '@', unit price, "=", "$" function for product of unit price and quantity.
# quantity value, groceries key, '@', groceries value, '=', "$", function of product unit price and quantity.

#######################################

# Attempt 1. this did not work, but there is a better way to do this than putting things into lists.
# receipt_list = []
# receipt = ""

# item_list = [key for key in groceries]
# # print(item_list)

# unit_price_list = list(groceries.values())
# # print(unit_price_list)

# quantity_list = list(quantity.values())
# # print(quantity_list)

# total_cost_list = [quantity_list[item] * unit_price_list[item]
#                    for item in range(len(quantity_list))]
# # print(total_cost_list)

# receipt_list.append(
#     [quantity_list, item_list, unit_price_list, total_cost_list])

# print(receipt_list)

# # for item in receipt_list:
# #     number = (item[0])
# #     product = (item[1])
# #     unit_price = (item[2])
# #     total_cost = (item[3])

# # # print(receipt_list)

# #     receipt = + {number} {product} @ ${unit_price} = ${total_cost}

# #     print(receipt)

########################################################
# d.keys() returns a list of all keys in d:
# d.values() returns a list of all values in d:
# d.items() returns a list of tuples containing the key-value pairs in d. The first item in each tuple is the key, and the second item is the key’s value:
# d.get(<key>) searches dictionary d for <key> and returns the associated value if it is found.

# for key in groceries:
#     total = quantity[key] * groceries[key]
#     print(round(total, 2))

# Kristy
# for items, prices in groceries.items()
# maybe not exactly but there was something about iterating against the 2 dictionaries using the groceries.items() or groceries.values() or groceries.keys()

# Technical Note: The .items(), .keys(), and .values() methods actually return something called a view object. A dictionary view object is more or less like a window on the keys and values. For practical purposes, you can think of these methods as returning lists of the dictionary’s keys and values.

# Success! The only issue is I cannot get the final $ to round to 2 dp. I have tried everything!
# for key in groceries.keys():
#     print(
#         f"{quantity[key]} {key} @ ${groceries[key]} = ${quantity[key] * groceries[key]}")


# Q1b

# groceries = {"Baby Spinach": 2.78, "Hot Chocolate": 3.70, "Crackers": 2.10,
#              "Bacon": 9.00, "Carrots": 0.56, "Carrots": 0.56, "Oranges": 3.08}

# quantity = {"Baby Spinach": 2, "Hot Chocolate": 1, "Crackers": 4,
#             "Bacon": 0, "Carrots": 8, "Oranges": 5}

# Success! The only issue is I cannot get the final $ to round to 2 dp. I have tried everything!
# for key in groceries.keys():
#     print(
#         f"{quantity[key]} {key} @ ${groceries[key]} = ${quantity[key] * groceries[key]}")

############################################################################

# Q2 The dictionary below contains several color names and a counter (defaulted to 0). Your task is to iterate over a list of colors and keep track of the number of times each color has occured by updating the corresponding counter in this dictionary.

# Success!
# color_counts = {
#     "blue": 0,
#     "green": 0,
#     "yellow": 0,
#     "red": 0,
#     "purple": 0,
#     "orange": 0,
# }

# colors = ["purple", "red", "yellow", "blue", "purple",
#           "orange", "blue", "purple", "orange", "green"]


# for item in colors:
#     if item in color_counts:
#         color_counts[item] += 1
#     else:
#         color_counts[item] = 1

# for key, value in color_counts.items():
#     print("{}: {}".format(key, value))

# 2b)
# color_counts = {
#     "blue": 0,
#     "green": 0,
#     "yellow": 0,
#     "red": 0,
#     "purple": 0,
#     "orange": 0,
# }

# colors = [
#     "orange", "purple", "blue", "yellow", "green", "green", "purple", "purple", "green",
#     "blue", "green", "orange", "purple", "blue", "green", "orange", "orange", "red", "yellow", "yellow"]

# for item in colors:
#     if item in color_counts:
#         color_counts[item] += 1
#     else:
#         color_counts[item] = 1

# for key, value in color_counts.items():
#     print("{}: {}".format(key, value))

# Q3:Given the list of names below, create a dictionary where each key is a name and the value is the number of times that name occurs in the list.

# names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy", "Joy", "Katie", "Maddie", "Tash", "Nic", "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
#          "Viv", "Anna", "Catherine", "Catherine", "Debby", "Gab", "Megan", "Michelle", "Nic", "Roxy", "Samara", "Sasha", "Sophie", "Teagen", "Viv"]


# Attempt 1: list comprehension. This is only good if there is no original dictionary already made up, which is the case here.
# Success!
# names_counter = {}  # Creating the empty list
# for item in names:  # Creating the for loop
#     names_counter[item] = names_counter.get(item, 0) + 1

# for key, value in names_counter.items():
#     print("{} {}".format(key, value))

# 3b) # Success!
# names = ["Miranda", "Sophie", "Emily", "Taylor", "Anne", "Djuarli", "Anika", "Rosie",
#          "Miranda", "Taylor", "Abby", "Sarah", "Teagen", "Abby", "Abby", "Maddie", "Miranda", "Rosie"]

# names_counter = {}  # Creating the empty list
# for item in names:  # Creating the for loop
#     names_counter[item] = names_counter.get(item, 0) + 1

# for key, value in names_counter.items():
#     print("{} {}".format(key, value))

# Q4: Read the color data from colors_20_simple.csv and save the data in a dictionary where the key is the hex code and value is the corresponding English name.

# Success!
# import csv

# color_codes = {}

# with open("csv_files/colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader)
#     color_codes = {rows[1]: rows[2] for rows in reader}
# # print(type(color_codes))
# for key, value in color_codes.items():
#     print("{}: {}".format(key, value))

# Q5:Modify your code from the previous exercise to save both the English name and RGB code in a list as the value for the corresponding hex code (create a dictionary of lists).

import csv

color_codes = {}

with open("csv_files/colours_20_simple.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    color_codes = {rows[1]: [rows[0], rows[2]] for rows in reader}
for key, value in color_codes.items():
    print("{}: {}".format(key, value))
