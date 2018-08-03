prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

stocks = {
    "banana" : 6,
    "apple" : 0, 
    "orange" : 32,
    "pear" : 15
}

for a, b in prices.items():
    for c, d in stocks.items():
        if a == c:
            print(a)
            print("price: ", b)
            print("stock: ", d)
            print()

total = 0
for a, b in prices.items():
    for c, d in stocks.items():
        if a == c:
            subtotal = b * d
            total += subtotal
print("Total money will be", total)