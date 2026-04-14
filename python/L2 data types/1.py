# activity 1
name = "Penguin"
age = 15
is_student = True
weight = 38.5

print("Name:", name, "|Type:", type(name))
print("Age:", age, "|Type:", type(age))
print("is_student:", is_student, "|Type:", type(is_student))
print("Weight:", weight, "|Type:", type(weight))

print("\nAfter type casting...")
age = str(age)
weight = int(weight)

print("age:", age, "|Type:", type(age))
print("weight:", weight, "|Type:", type(weight))

# Activity 2
num1 = 45
num2 = 3

print("Number 1:", num1)
print("Number 2:", num2)
print("Addition:", num1 + num2)
print("difference:", num1 - num2)
print("product:", num1 * num2)
print("Division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Modulus:", num1 % num2)
print("square:", num2 ** 2)
print("square root:", num1 ** 0.5)

print("Equal?:", num1 == num2)
print("Number 1 greater?:", num1 > num2)
print("Number 2 greater?:", num1 < num2)
print("Not equal?:", num1 != num2)

result = num1 / 2 + num2 ** 2 + 10
print("result:", result)