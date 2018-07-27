count = 0
loop = True
list = ["T-Shirt", "Sweater"]

while loop:
    choice = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if choice == "R":
        print("Our items: ", end ="")
        print(*list, sep=", ")
    elif choice == "C":
        new_item_C = input("Enter new item: ")
        list.append(new_item_C)
        print("Our items: ", end ="")
        print(*list, sep=", ")
    elif choice == "U":
        new_numb = int(input("Update position? "))
        new_item_U = input("New item? ")
        list[new_numb - 1] = new_item_U
        print("Our items: ", end ="")
        print(*list, sep=", ")
    elif choice == "D":
        delete_choice = int(input("Delete position? "))
        del list[delete_choice - 1]
        print("Our items: ", end ="")
        print(*list, sep=", ")
    count += 1
    if count == 4:
        loop = False