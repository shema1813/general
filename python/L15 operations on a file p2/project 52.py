# Step 1: Create a sample notes file
with open("notes.txt", "w") as file:
    file.write("Buy groceries\n")
    file.write("Finish Python assignment\n")
    file.write("Call Mom\n")
    file.write("Python practice every day\n")
    file.write("Read a book\n")

# Step 2: Preview file content using read(n)
with open("notes.txt", "r") as file:
    preview = file.read(30)  # Read the first 30 characters
    print("Preview of file:")
    print(preview)

# Step 3: Read all lines using readlines()
with open("notes.txt", "r") as file:
    lines = file.readlines()

print("\nAll Notes:")
for line in lines:
    print(line.strip())

# Step 4 & 5: Filter lines containing the word "Python"
filtered_notes = []

with open("notes.txt", "r") as file:
    for line in file:
        if "Python" in line:
            filtered_notes.append(line)

# Step 6: Copy filtered lines into a new file
with open("python_notes.txt", "w") as file:
    file.writelines(filtered_notes)

print("\nFiltered notes saved to 'python_notes.txt'.")

# Display filtered notes
print("\nFiltered Notes:")
for note in filtered_notes:
    print(note.strip())