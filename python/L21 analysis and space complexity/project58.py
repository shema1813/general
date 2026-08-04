def iterative_binary_search(seats, target):
    left = 0
    right = len(seats) - 1

    while left <= right:
        mid = (left + right) // 2

        if seats[mid] == target:
            return mid
        elif seats[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def recursive_binary_search(seats, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if seats[mid] == target:
        return mid
    elif seats[mid] < target:
        return recursive_binary_search(seats, target, mid + 1, right)
    else:
        return recursive_binary_search(seats, target, left, mid - 1)

seat_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

target = int(input("Enter the seat number to find: "))
index = iterative_binary_search(seat_numbers, target)

if index != -1:
    print(f"Iterative Search: Seat {target} found at index {index}.")
else:
    print("Iterative Search: Seat not found.")

index = recursive_binary_search(seat_numbers, target, 0, len(seat_numbers) - 1)

if index != -1:
    print(f"Recursive Search: Seat {target} found at index {index}.")
else:
    print("Recursive Search: Seat not found.")