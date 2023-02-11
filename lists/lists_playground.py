chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# indexing
print(len(chilli_wishlist))
# print(chilli_wishlist[4])

# print(chilli_wishlist[0])

# print(chilli_wishlist[1])
# print(chilli_wishlist[-1])
# print(chilli_wishlist[0:2])
# print(chilli_wishlist[1:3])
# chilli_wishlist[1] = 'carrot'
# print(chilli_wishlist)

# List of subitems in position 2 through to 3.
# print(chilli_wishlist[2:4])

# print the item in position -3
# print(chilli_wishlist[-3])

# Change the value of the first item in the list
# chilli_wishlist[0] = 'cow'
# print(chilli_wishlist)

# Challenge: adding item to chilli's wishlist at position number 2
# chilli_wishlist.insert(1, "donkey")
# print(chilli_wishlist)

# chilli_wishlist.append('dig mat')
# chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])
# chilli_wishlist.insert(1, 'peanut butter')
# print(chilli_wishlist)

# chilli_wishlist.pop()
# chilli_wishlist.pop(2)
# print(chilli_wishlist)
# chilli_wishlist.remove('kong')
# print(chilli_wishlist)

# chilli_wishlist.insert(-1, 'bone')
# chilli_wishlist.pop(2)
# print(chilli_wishlist)

# chilli_wishlist.extend(['ham', 'squeaky', 'shoe', 'teddy'])
# chilli_wishlist.remove('igloo')
# print(chilli_wishlist)

# if 'tennis ball' in chilli_wishlist:
#    print('Chilli would like a tennis ball.')
# else:
#    print("Chilli doesn't feel like playing fetch.")

# print(len(chilli_wishlist))
# if len(chilli_wishlist) > 8:
#    print("chilli wants a lot of stuff!")

# use if statement to check if blueberries is in the list and if not, add it.
# if "blueberries" not in chilli_wishlist:
#    chilli_wishlist.append("blueberries")
# print(chilli_wishlist)


# creating sublists
chilli_wishlist = [
    ["igloo"],  # bed
    ["donut toy", "tennis ball", "crocodile toy"],  # toys
    ["chicken", "peanut butter"],  # treats
    ["cardboard box", "kong", "dig mat"]  # activity-based toys
]

print(chilli_wishlist[2])
print(chilli_wishlist[2][1])

# if I want to replace peanut butter in the third list with collar, how would we do that?
# chilli_wishlist[2][1] = "collar"
# print(chilli_wishlist)

# Use indexing to change the third item in the second list
# chilli_wishlist[1][2] = "squeaky"
# print(chilli_wishlist)

# Add another sublist to the list.
# chilli_wishlist.append(['brush', 'clipper', 'bathtub'])
# print(chilli_wishlist)
