def power2(n):
    return n > 0 and (n & (n - 1)) == 0

def power4(n):
    return power2(n) and (n & 0x55555555) != 0

def power8(n):
    return n > 0 and power2(n) and n.bit_length() % 3 == 1

def fast_power(a, n):
    r = 1
    while n:
        if n & 1:
            r *= a
        a *= a
        n >>= 1
    return r

n = int(input("Enter a number: "))

print("Binary:", bin(n)[2:])
print("Power of 2:", power2(n))
print("Power of 4:", power4(n))
print("Power of 8:", power8(n))
print("Without rightmost set bit:", n & (n - 1))

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
print("Result:", fast_power(a, b))
