def super_digit(number: int) -> int:
    """
    Calculate the super digit of a given number.

    Parameters:
        number (int): The number to calculate the super digit for.

    Returns:
        int: The super digit of the given number.

    Example:
        >>> super_digit(123)
        6
        >>> super_digit(845)
        8
    """
    while number >= 10:
        total = 0
        for digit in list(str(number)):
            total += int(digit)
        number = total
    return number


def main():
    number = int(input("Enter a number: "))
    print(f"The super digit of {number} is {super_digit(number)}")


if __name__ == "__main__":
    main()
