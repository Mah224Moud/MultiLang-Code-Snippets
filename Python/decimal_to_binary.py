def decimal_to_binary(number: int) -> int:
    """
    Convert a decimal number to its binary representation.

    Parameters:
        number (int): The decimal number to be converted.

    Returns:
        int: The binary representation of the decimal number.
    """
    binary = ""
    while (number > 0):
        binary += f"{number%2}"
        number = number // 2
    return int(binary[::-1])


def main():
    number = int(input("Type a number : "))
    print(
        f"The binary representation of {number} is {decimal_to_binary(number)}")


if __name__ == "__main__":
    main()
