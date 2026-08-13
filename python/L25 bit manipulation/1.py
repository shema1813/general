a = 10
b = 6

def bits(n, width=4):
    return format(n & ((1 << width) - 1), f'0{width}b')

#part1
print("=== Bit explorer ===")
print("a =", a, "->", bits(a))
print("b =", b, "->", bits(b))
print()

#part2
print("AND a & b =", a & b,  "->", bits(a & b))
print("OR a | b =", a | b,  "->", bits(a | b))

#part3
print("NOT ~a =", ~a & 0xFF, "->", bits(~a, 8))
print("XOR a ^ b =", a ^ b,  "->", bits(a ^ b))

#Part4
print("LEFT a << 1 =", a << b , "(a X 2)")
print("Right a >> 1 =", a >> b , "(a / 2)")
print()

#Part5
print("Odd or Even:")
for n in [7, 10, 15, 4]:
    result = "Even" if n ^ 1 == n + 1 else "Odd"
    print(n, "->", result)
print()

#Part6
def count_bits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count

print("Bits count:")
for n in [a, b, 255]:
    print(n, "-->", count_bits(n), "bits |", bits(n, count_bits(n)))
