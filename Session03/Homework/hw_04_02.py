flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Chi and these are my sheep sizes:", flock)

# shorter answer (to be used in next assignment)
# print("Now my biggest sheep has size ", max(flock), " let's shear it")

i = 0
n = flock[0]
while i < (len(flock)):
    if flock[i] > n:
        n = flock[i]
    i += 1

print("Now my biggest sheep has size ", n, " let's shear it")