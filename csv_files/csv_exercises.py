# Q1 Write a program that reads in colours_20_simple.csv and output the colour data.
import csv

# with open("csv_files/colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(f"{line[0]} {line[1]} {line[2]}")


# Q2 Write a program that reads in colours_20_simple.csv and outputs the colour data in order English,Hex then RGB.
# with open("csv_files/colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(f"{line[2]}, Hex: {line[1]}, RGB: {line[0]}")

# Q3: Write a program that reads in colours_20.csv and output the colour data in order English, Hex, then RGB.
# with open("csv_files/colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")

# Q4:
# a) Using the same colour csv files, write a program that outputs the number of times each of the following colours appear in the English Name:
# Red
# Green
# Blue
# Yellow

# Method 5 - SUCCESS with Implementing Brigittes' pointers.

# Tip 1: rather than split the colour names into discrete words and use "yellow" == word. You can use "Yellow" in English_Colour.

# Tip 2: if you wanted to use nested loops rather than hardcode each of the ifs you could set your counter variables up as a list of lists with say
# colour_counts = [["yellow", 0], ["red", 0], ["green", 0], ["blue", 0]]

# Tip 3: for i in english_colours:
#    if "yellow" in i:
#        yellow += 1

# colour = []
# colour_counts = [
#     ["Red", 0],
#     ["Green", 0],
#     ["Blue", 0],
#     ["Yellow", 0]
# ]
# with open("csv_files/colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colour.append(line[4])
#     for item in colour:
#         if "red" in item:
#             colour_counts[0][1] += 1
#         if "green" in item:
#             colour_counts[1][1] += 1
#         if "blue" in item:
#             colour_counts[2][1] += 1
#         if "yellow" in item:
#             colour_counts[3][1] += 1
#     for colour, count in colour_counts:
#         print(f"{colour}: {count}")


# Attempt 4 - success. This works but if there is a better way to code the counting of words it would be better.
# english_colours = []
# colours = [word for line in english_colours for word in line.split()]

# red = 0
# green = 0
# blue = 0
# yellow = 0

# with open("csv_files/colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         english_colours.append(line[4])
#         colours = [word for line in english_colours for word in line.split()]
#     # print(colours)

#     for i in colours:
#         if i == "red":
#             red += 1
#     print(f"Red: {red}")

#     for i in colours:
#         if i == "green":
#             green += 1
#     print(f"Green: {green}")

#     for i in colours:
#         if i == "blue":
#             blue += 1
#     print(f"Blue: {blue}")

#     for i in colours:
#         if i == "yellow":
#             yellow += 1
#     print(f"Yellow: {yellow}")


# Attempt 3 - this did not work and I don't know why. Split is a valid method?
#    english_colours_split = english_colours.split(" ")

# Attempt 2 - Did not work.
# for i in english_colours:
#     if "red" in english_colours:
#         red += 1
#     print(f"Red:  {red}")
#     if "green" in english_colours:
#         green += 1
#     print(f"Green:  {green}")
#     if "blue" in english_colours:
#         blue += 1
#     print(f"Blue:  {blue}")
#     if "yellow" in english_colours:
#         yellow += 1
#     print(f"Yellow:  {yellow}")

# Attempt 1 - Cannot use count function for yellow because some strings CONTAIN 'yellow', but are not 'yellow'.
# count_red = english_colours.count("Red")
# print(f"Red: {count_red}")
# count_green = english_colours.count("Green")
# print(f"Green: {count_green}")
# count_blue = english_colours.count("Blue")
# print(f"Blue: {count_blue}")
# count_yellow = english_colours.count("Yellow")
# print(f"Yellow: {count_yellow}")

# b) Using colours_123.cvs, write a program that outputs the number of times each of the following colours appear in the English Name:
# Red
# Green
# Blue
# Yellow

# Method 1: Success!
# colour = []
# colour_counts = [  # Create a list of each colour count within a list. First column is colour, second is count.
#     ["Red", 0],
#     ["Green", 0],
#     ["Blue", 0],
#     ["Yellow", 0]
# ]
# with open("csv_files/colours_213.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colour.append(line[4])
#     for item in colour:  # Having this for loop eliminates the need to split the strings.
#         if "red" in item:
#             colour_counts[0][1] += 1
#         if "green" in item:
#             colour_counts[1][1] += 1
#         if "blue" in item:
#             colour_counts[2][1] += 1
#         if "yellow" in item:
#             colour_counts[3][1] += 1
#     for colour, count in colour_counts:
#         print(f"{colour}: {count}")

# Q5 Galaxies.py contains data about 82 different galaxies and
# their velocities (km/sec). Using the data, output the galaxy
# with the slowest velocity, and the galaxy with the highest
# velocity.
# INDEX / POSITION

# Method 2
# galaxy_velocities = []

# with open("csv_files/galaxies.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader)
#     for line in reader:
#         galaxy_velocities.append(line)

# min_vel = int(galaxy_velocities[0][1])
# min_gal = galaxy_velocities[0][0]
# max_vel = int(galaxy_velocities[0][1])
# max_gal = galaxy_velocities[0][0]

# for row in range(len(galaxy_velocities)):
#     if int(galaxy_velocities[row][1]) <= min_vel:
#         min_vel = int(galaxy_velocities[row][1])
#         min_gal = galaxy_velocities[row][0]
#     if int(galaxy_velocities[row][1]) >= max_vel:
#         max_vel = int(galaxy_velocities[row][1])
#         max_gal = galaxy_velocities[row][0]

# print(f"Galaxy {min_gal} has the min velocity of {min_vel}km/sec.\nGalaxy {max_gal} has the max velocity of {max_vel}km/sec.")

# Method 1.

galaxy_velocities = []

with open("galaxies.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for line in reader:
        galaxy_velocities.append(line)

min_vel = int(galaxy_velocities[0][1])
min_gal = galaxy_velocities[0][0]
max_vel = int(galaxy_velocities[0][1])
max_gal = galaxy_velocities[0][0]

for row in galaxy_velocities:
    if int(galaxy_velocities[row][1]) <= min_vel:
        min_vel = int(galaxy_velocities[row][1])
        min_gal = galaxy_velocities[row][0]
    if int(galaxy_velocities[row][1]) >= max_vel:
        max_vel = int(galaxy_velocities[row][1])
        max_gal = galaxy_velocities[row][0]

print(f"Galaxy {min_gal} has the min velocity of {min_vel}km/sec.\nGalaxy {max_gal} has the max velocity of {max_vel}km/sec.")

# Attempt 3 - Use of keys.


# def ret_2nd_ele(tuple_1):
#     return tuple_1[1]


# Attempt 2 - importing itemgetter and using it as a key in the min/max inbuilt functions.

# from operator import itemgetter
# galaxy_velocities = []

# with open("csv_files/galaxies.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader)
#     for line in reader:
#         galaxy_velocities.append(line)

# min_tuple = min(galaxy_velocities,
#                 key=itemgetter(1))[0]
# max_tuple = max(galaxy_velocities,
#                 key=itemgetter(1))[0]
# print(min_tuple)
# print(max_tuple)

# Attempt 1 - Unsuccessful. Using lambda key to sort tuples.
#     min_tuple = min(galaxy_velocities, key=lambda tup: tup[1])
#      = max(galaxy_velocities, key=lambda tup: tup[1])

# print(min_tuple)
# print()
