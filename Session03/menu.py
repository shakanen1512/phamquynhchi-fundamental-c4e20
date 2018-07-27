menu = ["Com", "Ca", "Thit bo", "Ga", "Pizza"]
#print(*menu, sep=", ")
menu.append("Ghe")
#print(*menu, sep=", ")

menu[4] = "Sushi"

#size = len(menu)
#print(size)

#for i in range(len(menu)):
    #print(menu[i])

for index, item in enumerate(menu):
    #print(index + 1, item, sep="")
    print("{}. {}".format(index + 1,item))

#for item in menu:
    #print(item)