import csv

colour = []
colour_counts = [
    ["Red", 0],
    ["Green", 0],
    ["Blue", 0],
    ["Yellow", 0]
]
with open("csv_files/colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colour.append(line[4])
# print(colour)

for item in colour:
    for colour in colour_counts:
        print(item, colour)
        # if colour[0] in item:
        # colour[1] += 1
