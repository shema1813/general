def test(lst):
    result= {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1,'jean castro','V'],[2,'Lula powell','V'],[3,'Brian','VI'],[4,'Lynne Foster','VI'],[5,'Zachary simon','VII'],]

print("\nOriginal list of lists:")
print(students)
print("\nConverted list to a dictionary:")
print(test(students))