def binary_to_decimal(number: int) -> int:
    """
    Convert a binary number to decimal.

    Args:
        number (int): The binary number to be converted.

    Returns:
        int: The decimal representation of the binary number.
    """
    values = list(str(number))
    result = 0
    pow_index = len(values) - 1
    for i in values:
        if i == "1":
            result += pow(2, pow_index)
        pow_index -= 1
    return result


def main():
    number = int(input("Enter the binary number you want to convert: "))

    print("\n\n*********************************************")
    print("****************** Result *******************")
    print("*********************************************")
    print(f"The decimal number of {number} is {binary_to_decimal(number)}")


if __name__ == "__main__":
    main()
