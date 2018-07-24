for row in range(1, 10):
    s = ""
    for col in range(1,10):
        s += '{:3}'.format(row*col)
    print(s)