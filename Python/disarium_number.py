def is_disarium_number(number: int) -> bool:
    """
    Determines if a given number is a disarium number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a disarium number, False otherwise.

    Examples:
        >>> is_disarium_number(89)
        True
        >>> is_disarium_number(190)
        False
    """
    total = 0
    for i, digit in enumerate(str(number)):
        total += int(digit) ** (i+1)
    return total == number


def main():
    number = int(input("Enter a number: "))
    if is_disarium_number(number):
        print(f"{number} is a disarium number")
    else:
        print(f"{number} is not a disarium number")


if __name__ == "__main__":
    main()
