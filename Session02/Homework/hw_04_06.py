n = int(input("Enter a number: "))
for row in range(1, n+1):
    s = ""
    for col in range(1,n+1):
        s += '{:3}'.format(row*col)
    print(s)