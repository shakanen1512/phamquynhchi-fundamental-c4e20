flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Chi and these are my sheep sizes:", flock)

current_biggest = max(flock)
print("Now my biggest sheep has size ", current_biggest , " let's shear it")

for i in range(len(flock)):
    if flock[i] == current_biggest:
        flock[i] = 8

print("After shearing, here is my flock", flock)