# for num in range(10):
#    print(num)

# for num in range(1, 11):
#    print(num)

# for num in range(0, 11, 2):
#    print(num)

# Challenge:
# for num in range(0, 101):
#     print(num)

# Challenge:
# for num in range(0, 101, 5):
#    print(num)

# How to use a for loop to repeat code for every item in a list
# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# for item in range(len(chilli_wishlist)):
#    print(chilli_wishlist[item])


# for item in chilli_wishlist:
#    print(item)

# Challenge: Adapt the for loop to print a message for each item in the list, e.g. "Chilli wants: item".
# for item in range(len(chilli_wishlist)):
#     print(f"Chilli wants: {chilli_wishlist[item]}")

# Challenge: Use a for loop to print each item in a list from a previous exercise or example.
# Taken from lists exercises; Prints
# foods = [
#     "orange",
#     "apple",
#     "banana",
#     "strawberry",
#     "grape",
#     "blueberry",
#     ["carrot", "cauliflower", "pumpkin"],
#     "passionfruit",
#     "mango",
#     "kiwifruit"
# ]

# for item in foods:
#     print(item)


# Nested Loops
# chilli_wishlist = [
#     ["igloo"],
#     ["donut toy", "tennis ball", "crocodile toy"],
#     ["chicken", "peanut butter"],
#     ["cardboard box", "kong", "ding mat"]
# ]

# for category in chilli_wishlist:
#     for item in category:
#        print(item)

# Challenge: Use a for loop to print each item in a list from a previous nested list exercise or example.
# Taken from lists exercises Q2;
# Format and print the following list to appear as name: email

# mailing_list = [
#     ['chilli', 'chilli@thechihuahua.com'],
#     ['Roary', 'roary@moth.catchers'],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"]
# ]

# My answer (entry refers to )
# for entry in mailing_list:
#     print(f"{entry[0]}: {entry[1]}")


# # Wen's Answer;
# for entry in mailing_list:
#     name, email = entry  # name and email variable corresponds with sublists
#     print(f"{name}: {email}")

# # Wens answer 2 BEST PRACTICE.Naming the columns/sublists.
# for name, email in mailing_list:
#     print(f"{name}: {email}")

# WHILE LOOPS
# Example 1
# How to use a while loop to repeat code until a certain condition is met.
# In the example below; while the guess isn't equal to a, the user input question will continue to pop up.
#   if i i put guess = input("guess a letter: ") at the start, then I am defining the guess variable, and that is not what we want here.

# guess = ""
# while guess != "a":
#     guess = input("Guess a letter: ")

# Example 2 - here, the output is 10. The condition for the loop is met, as
# counter is equal to or less than 10, so it will print counter which is 10.
# It doesn't have to perform the operation counter = counter + 1, as condition
# already met

# counter = 10
# while counter <= 10:
#     print(counter)
#     counter = counter + 1


# Example 3 - Here, output is 2,3,4,5,6,7,8,9,10. Because the counter = counter
# + 1 is nested within the while statement, starting from 2, 1 will be added to
# counter until the condition is met.

# counter = 2
# while counter <= 10:
#     print(counter)
#     counter = counter + 1

# Challenge
# Ask the user to continually enter names until a blank string is entered.
# This loop does not work without a space. User must press enter only, no space for this loop to continue.
# name = " "
# while name != "":
#    name = input("Type a name:")
