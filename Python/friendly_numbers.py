def divisor(number: float) -> float:
    """
    Calculate the sum of all the divisors of a given number except for 1 and the number.

    Args:
        number (float): The number for which to calculate the sum of divisors.

    Returns:
        float: The sum of all the divisors of the given number except for 1 and the number.
    """
    divisor_list = []
    for i in range(2, int(number)):
        if number % i == 0:
            divisor_list.append(i)
    return sum(divisor_list)


def is_friendly_numbers(first_number: float, second_number: float) -> bool:
    """
    Check if two numbers are friendly numbers.

    Args:
        first_number (float): The first number.
        second_number (float): The second number.

    Returns:
        bool: True if the numbers are friendly, False otherwise.
    """
    return divisor(first_number) == second_number and divisor(second_number) == first_number


def main():
    first_number = float(input("Type the first number: "))
    second_number = float(input("Type the second number: "))

    if is_friendly_numbers(first_number, second_number):
        print(f"{first_number} and {second_number} are friendly numbers.")
    else:
        print(f"{first_number} and {second_number} are not friendly numbers.")


if __name__ == "__main__":
    main()
