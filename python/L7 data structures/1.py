lst = ['apple','Guava','Mango','bannan','kiwi']

print("Length of list:", len(lst))
print("first element:", lst[0])
print("Length of list:", lst[-1])

lst.append('papaya')
print("Updated list:", lst)

lst.remove('Guava')
print("Updated list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop(1)
print("Updated list:", lst)

lst.reverse()
print("reversed:", lst)

print("Multiplication on List:", lst*2)

lst = lst[:4]
print("sliced lsit:", lst)

lst.clear()
print("updated list:", lst)