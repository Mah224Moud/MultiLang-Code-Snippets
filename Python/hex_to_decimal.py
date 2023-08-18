def hex_to_decimal(number: str) -> int:
    """
    Convert a hexadecimal number to its decimal representation.

    Parameters:
        number (str): The hexadecimal number to be converted.

    Returns:
        int: The decimal representation of the input hexadecimal number.

    Examples:
        >>> hex_to_decimal("A")
        10
        >>> hex_to_decimal("FF")
        255
    """
    number = number.upper()
    values = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    decimal = 0
    for i, key in enumerate(number[::-1]):
        decimal += values[key] * (16 ** i)

    return decimal


def main():
    number = input("Enter a hex number: ")
    print(f"The decimal number of {number} is {hex_to_decimal(number)}")


if __name__ == "__main__":
    main()
