groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}

# Print dictionary
print(groceries)

# print key
print(groceries["Baby Spinach"])

# Add item to dictionary
groceries["Avocadoes"] = 1.00
print(groceries)

# Changing the price of hot chocolate
groceries["Hot Chocolate"] = 2.70

print(groceries)

# Deleting an item from dictionary
del groceries["Crackers"]
print(groceries)

# For loop
for item in groceries:
    print(f"{item}: ${groceries[item]}")

# Quicker way to acccess items than for loop
# This species the keys in your list. It's the 'dictionary' version of index for lists.
for item, price in groceries.items():
    print(f"{item}: ${price}")

# item is a method instead of a placeholder, as it is in lists.
# Would use a dictionary if the data is paired/there is a consistent relationship between
# To find index in a dictionary
#   Inumerate ()
