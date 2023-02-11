day = "saturday"
date = "31st October"
print(type(day))

message = f"Today is {day} {date}!"
print(message)

name = "Karen"
message = f"{name} the Carrot"
print(message)

# integers
# Run distance in m
run1_dist = 1400
run2_dist = 1800

# Addition
subtotal_distance_1 = run1_dist + run2_dist

# Floats
# Run distance in km
run3_dist = 1.7
run4_dist = 1.35

# Addition
subtotal_distance_2 = run3_dist + run4_dist

# Division and Multiplication Example
#print(run1_dist / 1000)
#print(run4_dist * 1000)

total_distance_m = subtotal_distance_1 + (subtotal_distance_2 * 1000)
print(total_distance_m)

total_distance_km = total_distance_m / 1000
print(total_distance_km)

goal_distance_km = 7
distance_to_goal_km = goal_distance_km - total_distance_km
print(distance_to_goal_km)

distance_to_goal_m = distance_to_goal_km * 1000
print(distance_to_goal_m)

average_distance_km = total_distance_km / 4
print(average_distance_km)

average_distance_m = average_distance_km * 1000
print(average_distance_m)

run5_dist = "5000"
# cannot concatonate an integer and a string
#print(run5_dist + 3)

# cannot convert an integer into a string to make it concatonate
# print(run5_dist + "3")

# Multiplying an integer with a string will result in the string repeated 3x only, not multiplied.
# print(run5_dist * 3)

# multiplying an integer with a float does not concatonate or work.
# print(run5_dist * 3.0)

# Typecasting
print(int(run5_dist) + 3)
print(str(3))
