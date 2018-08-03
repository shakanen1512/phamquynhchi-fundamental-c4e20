#quy = ["Quy", 20, "Vinh Phuc", 2, 3, ["Anime", "ping pong"]]
# dictionary
# key : value

#create
person = {
"name" : "Quy",
"age" : 20,
"university" : "hust",
"ex" : 2,
"favs" : ["Anime", "ping pong"]
}

# person["gender"] = "male"
# print(person)

#read

# key = "ex"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

# for key in person.keys():
#     print(key, end="\t")

# for key, value in person.items():
#     print(key, value)

# for value in person.values():
#     print(value)

#update
# person["ex"] = 20
# print(person)

#delete
del person["age"]
print(person)