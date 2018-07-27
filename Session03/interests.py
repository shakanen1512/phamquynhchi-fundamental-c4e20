print("Hi there, your favorite things so far")
interest = ["Economics", "History", "Japanese"]
print(*interest, sep=", ")
new = input("Name one thing you want to add? ")
interest.append(new)
print(*interest, sep=", ")