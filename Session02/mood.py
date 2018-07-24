from random import randint
random_number = randint(1,100)

print("How is your mood?")
if random_number < 30:
    print ("Melancholy")
elif random_number < 60:
    print ("Serendipity")
else:
    print ("Euphoria")