def find_one_odd_number(numbers):
    result = 0

    for number in numbers:
        result ^= number

    return result


def find_two_odd_numbers(numbers):
    xor_all = 0

    for number in numbers:
        xor_all ^= number

    rightmost_set_bit = xor_all & -xor_all

    number1 = 0
    number2 = 0

    for number in numbers:
        if number & rightmost_set_bit:
            number1 ^= number
        else:
            number2 ^= number

    return number1, number2


def display_binary(numbers):
    print("\nBinary values:")
    for number in numbers:
        print(f"{number:>5} = {number:08b}")


def main():
    print("=" * 50)
    print("       BINARY CLUE INVESTIGATOR")
    print("=" * 50)

    while True:
        print("\nChoose an investigation:")
        print("1. Find ONE number occurring an odd number of times")
        print("2. Find TWO numbers occurring an odd number of times")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            numbers = list(map(int, input(
                "\nEnter the numbers separated by spaces: "
            ).split()))

            display_binary(numbers)

            answer = find_one_odd_number(numbers)

            print("\nInvestigation Result")
            print("-" * 30)
            print(f"Odd-occurring number: {answer}")
            print(f"Binary: {answer:08b}")

        elif choice == "2":
            numbers = list(map(int, input(
                "\nEnter the numbers separated by spaces: "
            ).split()))

            display_binary(numbers)

            answer1, answer2 = find_two_odd_numbers(numbers)

            print("\nInvestigation Result")
            print("-" * 30)
            print(f"First odd-occurring number:  {answer1}")
            print(f"Binary: {answer1:08b}")
            print(f"Second odd-occurring number: {answer2}")
            print(f"Binary: {answer2:08b}")

        elif choice == "3":
            print("\nInvestigation complete. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
