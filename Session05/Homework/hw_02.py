inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

#add new key "pocket" and its value
inventory["pocket"] = ["seashell", "strange berry", "lint"]

#delete value "dagger" from key "backpack"
n = inventory["backpack"].index("dagger")
del inventory["backpack"][n]

#add 50 to the number stored under key "gold"
inventory["gold"] += 50

#change value of key "gold" to a list of of 500 & 50
inventory["gold"] = [500]
inventory["gold"].append(50)