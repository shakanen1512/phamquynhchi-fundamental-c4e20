print("Hi there, your favorite things so far")
interest = ["Economics", "History", "Japanese"]

print("* " * 20)
for index, item in enumerate(interest):
    print("{}. {}".format(index + 1,item))
print("* " * 20)

new_numb = int(input("Name position you want to replace: "))
interest[new_numb - 1] = input("What is your new favorite? ")

print("* " * 20)
for index, item in enumerate(interest):
    print("{}. {}".format(index + 1,item))
print("* " * 20)
