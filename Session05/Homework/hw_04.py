initial_bacteria = int(input("How many B bacteria are there? "))
time = int(input("How much time in minutes will we wait? "))

if time % 2 == 0: 
    time_1 = time
else:
    time_1 = time - 1

total_bacteria = int(initial_bacteria*2**(time_1/2))
print("After {} minutes, we would have {} bacteria".format(time, total_bacteria))