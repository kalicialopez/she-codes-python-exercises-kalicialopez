# Q1 Kate's cat, Roary, loves catching moths. Write a program that determines whether or not it is time for Roary to catch moths.
#moths_in_house = True
# if moths_in_house:
#    print("Get the moths!")
# else:
#    print("No threats detected")

# Q2 But Roary can't actually get moths by herself! Amend the previous program to determine whether ot not it is time for Roary to go moth hunting.
#moths_in_house = True
#mitch_is_home = True

# if moths_in_house and mitch_is_home:
#    print("Hooman! Help me get the moths!")
# elif moths_in_house and not mitch_is_home:
#    print("Meoooooooooow! Hisssss!")
# elif not moths_in_house and mitch_is_home:
#    print("Climb on Mitch.")
# else:
#    print("No threats detected.")

# Q3 Write a program that implements the algorithm for Red Light Cameras.
#light_color = "Red"
#car_detected = True

# if light_color and car_detected:
#    print("Flash!")
# else:
#    print("Do nothing.")

# Q4 Write a program that asks the user for their height, and determines whether or not they are tall enough to ride the rollercoaster, which has a height requirement of 120cms.
#height = input("How tall are you (in cms)?")
# if int(height) >= 120:
#    print("Hop on!")
# else:
#    print("Sorry, not today!")

# Q5 Write a program that asks the user to enter their username and password, and outputs a success message if they're correct, or a failure message if they are incorrect.
#username = input("Username:")
#password = input("Password:")

# if username == "fleur" and password == "password123":
#    print("Correct!")
# else:
#    print("Incorrect!")


# Q6 Write a program that asks the user to enter their email address and checks whether it is valid or not. For the purpose of this exercise, you can make the assumption that a valid email address contains a "@" symbol and a "." symbol.
email = input("Email:")
compulsory_1 = ('@')
compulsory_2 = ('.')

if compulsory_1 and compulsory_2 in email:
    print("Valid email address.")

else:
    print("Invalid email address.")
