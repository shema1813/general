def build_subset(items, mask):
    """Build one subset using a binary mask."""
    subset = []

    for i in range(len(items)):
        # Check if bit i is turned on
        if (mask >> i) & 1:
            subset.append(items[i])

    return subset

def power_set(items):
    """Generate every possible subset of the list."""
    subsets = []

    # There are 2^n possible subsets
    total = 2 ** len(items)

    for mask in range(total):
        subset = build_subset(items, mask)
        subsets.append(subset)

    return subsets

def bit_difference(a, b):
    """Return the bits that are different between two numbers."""
    return a ^ b


items = ["A", "B", "C"]

print("Items:", items)
print()
print("Power Set:")

subsets = power_set(items)

for subset in subsets:
    print(subset)


print()
print("Bit Probe:")

mask = 5 

for i in range(len(items)):
    bit = (mask >> i) & 1
    print("Bit", i, "=", bit)

print("Mask 5 selects:", build_subset(items, mask))

print()
print("Bit Difference:")
a = 5       
b = 3     
difference = bit_difference(a, b)

print("a =", a, "binary:", bin(a))
print("b =", b, "binary:", bin(b))
print("a XOR b =", difference, "binary:", bin(difference))

