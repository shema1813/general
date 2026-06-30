# PART 1
n = int(input("How many characters to preview?"))
file = open("python/L14 operations on a file/Class-notes.txt", "r")
print(file.read(n))
file.close()
print()

# PART 2
file = open("python/L14 operations on a file/Class-notes.txt", "r")
lines = file.readlines()
file.close
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

# PART 3
word = input("Skip lines starting with:")
file = open("python/L14 operations on a file/Class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Seep ->", line.strip())
    else:
        print("Keep ->", line.strip())
file.close
print()

# PART 4
file = open("python/L14 operations on a file/Class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("python/L14 operations on a file/odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close
print("Odd lines saved to odd-lines.txt")
