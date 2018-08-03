alreadyknown = {0: 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        t = fib(n-1) + fib(n-2)
        alreadyknown[n] = t
    return alreadyknown[n]

for i in range(5):
    total = fib(i+2)
    print("Month {}: {} pair(s) of rabbit".format(i, total))