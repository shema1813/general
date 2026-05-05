my_set = {1,2,2,3,4,4,4}
print("Set :", my_set)

#ADD element
my_set.add(5)
print("After adding 5:", my_set)

#second set
set2 = {2,4,6}
print("\nSecond set:", set2)

#set operations
print("\nDifference:", my_set.difference(set2))
print("Symmetric Difference:", my_set.symmetric_difference(set2))
print("Union:", my_set.union(set2))
print("Intersevtion:", my_set.intersection(set2))