scores = [85, 92, 78, 90, 88]
target = int(input("Enter the quiz score to search: "))

print("\nDirect Access:")
index = int(input("Enter an index (0-4): "))
if 0 <= index < len(scores):
    print("Score at index", index, "is", scores[index])
else:
    print("Invalid index.")

print("\nLinear Search:")
found = False
for i in range(len(scores)):
    if scores[i] == target:
        print("Score found at index", i)
        found = True
        break

if not found:
    print("Score not found.")

print("\nPair Comparison:")
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        print(scores[i], "compared with", scores[j])