# Method 1: Formula
# START
# Get number of laps
# Get points per lap
# Multiply laps by points per lap
# Display total points
# END

# Method 2: Loop
# START
# Get number of laps
# Get points per lap
# Set total points to 0
# Repeat for each lap:
#     Add points per lap to total points
# Display total points
# END

# Method 3: Nested Loop
# START
# Get number of laps
# Get points per lap
# Set total points to 0
# Repeat for each lap:
#     Repeat points per lap times:
#         Add 1 to total points
# Display total points
# END

laps = int(input("Enter the number of laps completed: "))
points_per_lap = int(input("Enter the points earned per lap: "))

formula_points = laps * points_per_lap
print("\nMethod 1: Formula")
print("Total Points =", formula_points)

loop_points = 0

for i in range(laps):
    loop_points += points_per_lap

print("\nMethod 2: Loop")
print("Total Points =", loop_points)

nested_points = 0

for i in range(laps):
    for j in range(points_per_lap):
        nested_points += 1

print("\nMethod 3: Nested Loop")
print("Total Points =", nested_points)

print("\nComplexity Comparison")
print("Formula:      Time = O(1), Space = O(1)")
print("Loop:         Time = O(n), Space = O(1)")
print("Nested Loop:  Time = O(n²), Space = O(1)")

print("\nMost Efficient: Formula (O(1))")
