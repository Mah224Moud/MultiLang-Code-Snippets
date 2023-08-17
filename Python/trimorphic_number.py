def is_trimorphic_number(number: int) -> bool:
    """
    Check if a number is a trimorphic number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a trimorphic number, False otherwise.

    Example:
        >>> is_trimorphic_number(192)
        False
        >>> is_trimorphic_number(25)
        True
    """
    digits_list = list(str(number))
    length = len(digits_list)

    cube = number ** 3
    cube_list = list(str(cube))

    return digits_list == cube_list[-length:]


def main():
    number = int(input("Enter a number: "))
    print(f"Is {number} a trimorphic number? {is_trimorphic_number(number)}")


if __name__ == "__main__":
    main()
