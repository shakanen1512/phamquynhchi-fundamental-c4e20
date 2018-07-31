from random import choice
words = ["champion", "dungeon", "vodka"]
word = choice(words)
list = list(word)

from random import shuffle
for i in range(len(list)):
    shuffle(list)
print(*list, sep=" ")

loop = True
count = 0

while loop:
    guess = input("Enter your guess: ")
    if guess == word:
        print("Yeah you win!")
        break
    else:
        print("Wrong, try again")
    count += 1
    if count == 5:
        print("Actually, game over!")
        loop = False