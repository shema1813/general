with open("notes.txt", "w") as file:
    file.write("Buy groceries\n")
    file.write("IMPORTANT: Submit assignment\n")
    file.write("Python file handling practice\n")
    file.write("IMPORTANT: Study for exam\n")
    file.write("Go for a walk\n")

with open("notes.txt", "r") as file:
    preview = file.read(30)
    print("Preview (30 characters):")
    print(preview)

with open("notes.txt", "r") as file:
    lines = file.readlines()

print("\nAll Lines:")
print(lines)

important_notes = []

print("\nImportant Notes:")
for line in lines:
    if "IMPORTANT" in line:
        print(line.strip())
        important_notes.append(line)

with open("important_notes.txt", "w") as file:
    file.writelines(important_notes)

print("\nImportant notes have been copied to 'important_notes.txt'.")