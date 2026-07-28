# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def average(numbers):
    if not numbers:
        return 0
    return sum_numbers(numbers) / len(numbers)


def max_number(numbers):
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum


def min_number(numbers):
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum


def format_value(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def main():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid integer for the count.")
        return

    if count <= 0:
        print("Error: Number of values must be a positive integer.")
        return

    numbers = []
    for i in range(1, count + 1):
        try:
            value = float(input(f"Enter number {i}: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        numbers.append(value)

    total = sum_numbers(numbers)
    avg = average(numbers)
    maximum = max_number(numbers)
    minimum = min_number(numbers)

    print("\nResults:")
    print(f"Sum:     {format_value(total)}")
    print(f"Average: {format_value(avg)}")
    print(f"Maximum: {format_value(maximum)}")
    print(f"Minimum: {format_value(minimum)}")


if __name__ == "__main__":
    main()

