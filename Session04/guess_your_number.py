input("Please think about a number between 1 and 100 then press Enter")
list = range(1,100)

print("""
"c" if my guess is correct
"s" if my guess is smaller
"l" if my guess is larger
""")

loop = True
count = 0

#while loop:
    #for i in range(len(list)):
        #n = (list[0] + list[len(list)-1])/2
        #guess = int(input("Is {} your number?".format(n)))
        #if guess == "s":
            #del list[0:i/2]
        #elif guess == "l":
            #del list[i/2: i]
        #elif guess == "c":
            #print("Congrats")
            #break
        #count += 1

low = 0
high = 100

while loop:
    mid = (low + high) // 2
    guess = input("Is {} your number? ".format(mid))

    if guess == "c":
        print("Correct")
        break
    elif guess == "s":
        low = mid
    elif guess == "l":
        high = mid
