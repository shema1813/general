#part1
names = ["Aarav", "Priya", "Dev", "Meera", "Kabir"]
scores = [90, 75, 88, 62, 95]
n = len(scores)
print("=== Score Tracker (n=", n, "players) ===")
for i in range(n):
    print(i + 1, ". ", names[i], " : ", scores[i], sep="")
print()

#part2
steps = 1
print("score at index 0 :", scores[0], "| steps=", steps, "| Theta(1) - tight bound\n")
print()

#part3
target = "Aarav"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for", target, "| steps =", steps, "| Omega(1) - best case lower bound")

target = "Kabir"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for", target, "| steps =", steps, "| O(n) =", n, "- worst case upper bound")

steps = 0
target_sum = 150
print("Pairs wuth total score =", target_sum, ":")
for i in range(n):
    for j in range(i + 1, n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(" ", names[i], "+", names[j], "=", scores[i] + scores[j])
print("Total comparisons :", steps, "| O(n^2) - drop constants, keep n^2")
print()

#part5
print("=== Asymptotic summary ===")
print("Theta(1) : index access - always 1 step, tight bound")
print("Omega(1) : best case - found in 1 step, lower bound")
print("O(n) : worst case - found after n =", n, "steps, upper bound")
print("O(n^2) : pair check - n*(n-1)/2 =", n * (n-1) // 2, "comparisons")
print()
print("Drop constants, Keep the dominant term. That us asymptotic analysis")
