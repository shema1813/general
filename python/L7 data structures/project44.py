import random

user_number = int(input("Pick a number between 1 and 10: "))

numbers = list(range(1, 11))

computer_number = random.choice(numbers)

print(f"Computer picked: {computer_number}")

if user_number == computer_number:
    print("You won!")
else:
    print("You lost!")