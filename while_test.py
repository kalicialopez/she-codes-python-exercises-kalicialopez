num_list = []

while True:
    num = input("Enter a number")
    if num == " ":
        print(sum(num_list))
        break
    else:
        num_list.append(int(num))
