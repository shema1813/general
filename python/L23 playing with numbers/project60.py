a = int(input("Enter a number"))
b = int(input("Enter a number"))

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break