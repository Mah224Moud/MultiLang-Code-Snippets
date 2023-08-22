def decimal_to_binary(number: int) -> int:
    """
    Convert a decimal number to its binary representation.

    Parameters:
        number (int): The decimal number to be converted.

    Returns:
        int: The binary representation of the decimal number.

    Examples:
        >>> decimal_to_binary(10)
        1010
        >>> decimal_to_binary(15)
        1111
    """
    binary = ""
    while (number > 0):
        binary += f"{number%2}"
        number = number // 2
    return int(binary[::-1])


def is_evil_number(number: int) -> bool:
    """
    Determine if the given number is an evil number.

    Parameters:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is evil, False otherwise.

    Examples:
        >>> is_evil_number(3)
        False

        >>> is_evil_number(4)
        True
    """

    decimal_to_binary_list = map(int, list(str(decimal_to_binary(number))))
    ones = 0
    for i in decimal_to_binary_list:
        if i == 1:
            ones += 1
    return ones % 2 == 0


def main():
    number = int(input("Enter a number: "))
    if (is_evil_number(number)):
        print(f"{number} is an evil number")
    else:
        print(f"{number} is not an evil number")


if __name__ == "__main__":
    main()
