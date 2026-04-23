num = int(input("Enter a number: "))

num_str = str(num)
num_digits = len(num_str)

total = 0
for digit in num_str:
    total += int(digit) ** num_digits

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")