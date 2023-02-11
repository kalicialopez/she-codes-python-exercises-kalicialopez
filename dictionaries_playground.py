groceries = {'Baby Spinach': 2.78, 'Hot Chocolate': 3.70,
             'Crackers': 2.10, 'Bacon': 9.00, 'Carrots': 0.56, 'Oranges': 3.08, }

# print(groceries)
## output = {'baby Spinach': 2.78, 'Hot Chocolate': 3.7, 'Crackers': 2.1, 'Bacon': 9.0, 'Carrots': 0.56, 'Oranges': 3.08}

# looking at a specific value
# print(groceries['Baby Spinach'])

# adding a new item
groceries["Avocadoes"] = 1.00
# print(groceries)

# Changing the value of an existing item
groceries["Hot Chocolate"] = 2.70
# print(groceries)

# removing an item from the dictionary
del groceries["Crackers"]
# print(groceries)

# iterating over the dictionary
# for item in groceries:
#    print(f"{item}: ${groceries[item]}")

# print()

# another way to iterate over the dictionary, .items is a method. Using for item, price we are looking at it like a list?
for item, price in groceries.items():
    print(f"{item}: ${price}")
