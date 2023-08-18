def decimal_to_hex(number: int) -> str:
    """
    Converts a decimal number to its hexadecimal representation.

    Parameters:
        number (int): The decimal number to be converted.

    Returns:
        str: The hexadecimal representation of the decimal number.

    Examples:
        >>> decimal_to_hex(10)
        'A'
        >>> decimal_to_hex(16)
        '10'
        >>> decimal_to_hex(255)
        'FF'
    """

    values = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F"
    }

    hex_values = ""
    while number > 0:
        rest = f"{number % 16}"
        hex_values += values[rest]
        number //= 16
    return hex_values[::-1]


def main():
    number = int(input("Type a number : "))
    print(
        f"The hexadecimal representation of {number} is {decimal_to_hex(number)}")


if __name__ == "__main__":
    main()
