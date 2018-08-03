numbers = [1, 6, 8, 1, 2, 1, 5, 6]
print("numbers = [1, 6, 8, 1, 2, 1, 5, 6]")

n = int(input("Enter a number: "))
count = 0
for i in range(len(numbers)):
    if numbers[i] == n:
        count += 1

print(n, " appears ", count, " times in my list")