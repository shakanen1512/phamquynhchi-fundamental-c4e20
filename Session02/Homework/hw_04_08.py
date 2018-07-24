n = int(input("Enter a number: "))
for row in range(1, n+1):
    s = ""
    for col in range(1,n+1):
        if (row + col) % 2 == 0:
            s += '{:3}'.format(1)
        else:
            s += '{:3}'.format(0)
    print(s)