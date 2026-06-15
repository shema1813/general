file = open("shopping-list.txt", "w")
file.write("1. Milk\n")
file.write("2. Bread\n")
file.write("3. Eggs\n")
file.close()
print("Shopping list saved to shopping-list.txt!")

file = open("shopping-list.txt", "r")
content = file.read()
print("\n=== My Shopping List ===")
print(content)
file.close()

file = open("shopping-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} items on your shopping list")
file.close()

file = open("shopping-list.txt", "a")
file.write("4. Apples\n")
file.write("5. Rice\n")
file.close()
print("\n2 more items added!")

file = open("shopping-list.txt", "r")
print("\n=== Updated Shopping List ===")
for line in file:
    print(line.strip())
file.close()