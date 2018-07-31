import re
your_name = input("Your full name: ")
up_name = your_name.split()
up_name = [chara.lower() for chara in up_name];up_name
for i in range(len(up_name)):
    up_name[i] = up_name[i].title()
print("Updated: ",*up_name, sep=" ")
