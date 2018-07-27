flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Chi and these are my sheep sizes:", flock)
print()

for k in range(1, 4):
    current_biggest = max(flock)
    print("Now my biggest sheep has size ", current_biggest , " let's shear it")

    for i in range(len(flock)):
        if flock[i] == current_biggest:
            flock[i] = 8
    print("After shearing, here is my flock", flock)
    print()

    for j in range(len(flock)):
        flock[j] += 50
    print("Month", k)
    print("One month has passed, now here is my flock", flock)

total_price = sum(flock) *2
print("My flock has size in total: ", sum(flock))
print("I would get", sum(flock), " *2$ = ", total_price, "$")