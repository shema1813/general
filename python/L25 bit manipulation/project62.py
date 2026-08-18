secret = 10
key = 6

def bits(n):
    return format(n & 255, "08b")

def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print("=== Secret Code Bit Scanner ===")
print("Secret Code:", secret, "->", bits(secret))
print("Access Key: ", key, "->", bits(key))
print()

print("AND:", secret & key, "->", bits(secret & key))
print("XOR:", secret ^ key, "->", bits(secret ^ key))
print()

flipped = (~secret) & 255
print("Flipped Secret:", flipped, "->", bits(flipped))

print("Shift Left:", secret << 1, "->", bits(secret << 1))
print("Shift Right:", secret >> 1, "->", bits(secret >> 1))
print()

print("Secret 1-bits:", count_bits(secret))
print("Key 1-bits:", count_bits(key))

if secret == key:
    print("Access Granted!")
else:
    print("Access Denied!")

