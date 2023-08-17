def is_duplicated(values: list) -> bool:
    """
    Check if there are any duplicated values in the given list.

    Parameters:
    - `values` (list): The list of values to check for duplicates.

    Returns:
    - `bool`: True if there are duplicates, False otherwise.
    """
    for i in values:
        if values.count(i) > 1:
            return True
    return False


def has_all_digits(values: list) -> bool:
    """
    Check if a list of values contains all the digits from 1 to 9.

    Args:
        values (list): A list of values.

    Returns:
        bool: True if the list contains all the digits from 1 to 9, False otherwise.
    """
    return sorted(values) == list("123456789")


def is_fascinating_number(number: int) -> bool:
    """
    Check if a number is a fascinating number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a fascinating number, False otherwise.

    Example:
        >>> is_fascinating_number(192)
        True
        >>> is_fascinating_number(257)
        False
    """
    result = str(number) + str(number * 3) + str(number * 2)

    return not is_duplicated(list(result)) and has_all_digits(result)


def main():
    number = int(input("Enter a number: "))
    if (is_fascinating_number(number)):
        print(f"{number} is a fascinating number")
    else:
        print(f"{number} is not a fascinating number")


if __name__ == "__main__":
    main()
