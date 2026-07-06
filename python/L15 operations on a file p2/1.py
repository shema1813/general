import os

#Part 1
print("=== Science Notes ===")
with open("python/L15 operations on a file p2/science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

#Part2
print("=== Word Count ===")
with open("python/L15 operations on a file p2/math-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

#Part3
print("=== Merging Notes ===")
if os.path.exists("python/L15 operations on a file p2/all-notes.txt"):
    print("all-notes.txt already exists - overwriting")
else:
    print("all-notes.txt not found - creating now")

content = ""
with open("python/L15 operations on a file p2/science-notes.txt", "r") as f:
    content += "--- science-notes.txt ---\n"
    content += f.read() + "\n"

with open("python/L15 operations on a file p2/math-notes.txt", "r") as f:
    content += "--- math-notes.txt ---\n"
    content += f.read() + "\n"

with open("python/L15 operations on a file p2/all-notes.txt", "w") as out:
    out.write(content)
print("Saved to all-notes.txt")
print()

#Part4
if os.path.exists("python/L15 operations on a file p2/all-notes.txt"):
    os.remove("python/L15 operations on a file p2/all-notes.txt")
    print("all-notes.txt deleted.")
else:
    print("all-notes.txt does not exist")

