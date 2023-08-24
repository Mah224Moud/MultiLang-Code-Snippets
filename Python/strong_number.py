def factorial(number: int) -> int:
    """
    Calculate the factorial of a given number.

    Parameters:
        number (int): The number for which the factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.

    Examples:
        >>> factorial(5) -> 120
        >>> factorial(0) -> 1
    """
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def is_strong_number(number: int) -> bool:
    """
    Check if a number is a strong number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a strong number, False otherwise.

    Examples:
        >>> is_strong_number(145) -> True
        >>> is_strong_number(40585) -> True
        >>> is_strong_number(123) -> False
    """
    list_of_numbers = map(int, list(str(number)))
    result = 0
    for i in list_of_numbers:
        result += factorial(i)
    return result == number


def main():
    number = int(input("Enter a number: "))
    if (is_strong_number(number)):
        print(f"{number} is a strong number")
    else:
        print(f"{number} is not a strong number")


if __name__ == "__main__":
    main()
