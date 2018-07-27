from random import *
numb = randint(0,100)
count = 0
loop = True

while loop:
    guess = int(input("Guess my number (0-100): "))
    if guess < numb:
        print("Too small")
    elif guess > numb:
        print("Too large")
    else:
        print("Bingo")
        break
    count += 1
    if count == 7:
        print("You lose")
        loop = False
    
