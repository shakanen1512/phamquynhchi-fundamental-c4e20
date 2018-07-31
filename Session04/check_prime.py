numb = int(input("Enter a number: "))
is_prime = True
i = 2

while i < (numb**2): 
    if numb % i == 0:
        is_prime = False
    i += 1

if is_prime:
    print("{} is a prime number".format(numb))
else:
    print("{} is not a prime number".format(numb))