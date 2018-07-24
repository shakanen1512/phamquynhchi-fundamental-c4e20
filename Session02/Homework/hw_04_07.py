for row in range(1, 10):
    s = ""
    for col in range(1,10):
        if (row + col) % 2 == 0:
            s += '{:3}'.format(1)
        else:
            s += '{:3}'.format(0)
    print(s)