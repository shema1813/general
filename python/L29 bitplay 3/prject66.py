print("1. Swap without a third variable")
a = 10
b = 20
print("Before swap: a =", a, "b =", b)
a, b = b, a

print("After swap:  a =", a, "b =", b)
print()

print("2. XOR Swap")
a = 15
b = 25

print("Before swap: a =", a, "b =", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swap:  a =", a, "b =", b)
print()

print("3. Double a number using left shift")
number = 12
result = number << 1
print("Number:", number)
print("Doubled:", result)
print()

print("4. Detect different signs using XOR")
a = -10
b = 20
if (a ^ b) < 0:
    print(a, "and", b, "have different signs")
else:
    print(a, "and", b, "have the same sign")
print()


print("5. Divide using right shift")
number = 40
result = number >> 1
print("Number:", number)
print("Result:", result)
