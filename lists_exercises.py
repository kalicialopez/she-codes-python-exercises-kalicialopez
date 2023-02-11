# Q1 Given the list of foods below, output:
# foods = ["orange", "apple", "banana", "strawberry", "grape", "blueberry", [
#    "carrot", "cauliflower", "pumpkin"], "passionfruit", "mango", "kiwifruit"]

# print(len(foods))

# orange
# print(foods[0])

# banana
# print(foods[2])

# kiwifruit
# print(foods[9])

# ['orange', 'apple', 'banana']
# print(foods[0:3])

# ['passionfruit', 'mango', 'kiwifruit']
# print(foods[7:10])

# pumpkin
# print(foods[6][2])

# Q2 Format and print the following list:

# mailing_list = [
#    ['chilli', 'chilli@thechihuahua.com'],
#    ['Roary', 'roary@moth.catchers'],
#    ["Remus", "remus@kapers.dog"],
#    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#    ["Ivy", "noreply@goldendreamers.xyz"]
# ]

# print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
# print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
# print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
# print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
# print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")

# Q3 Ask the user for three names, add them to a list, then print the list.
# name_1 = input("Enter a name")
# name_2 = input("Enter a name")
# name_3 = input("Enter a name")

# name_list = [name_1, name_2, name_3]
# print(name_list)

# Q4 Using the following starter code:

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

# Produce the following lists:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

d = [a, b, c]
e = a + b + c

print(d)
print(e)
