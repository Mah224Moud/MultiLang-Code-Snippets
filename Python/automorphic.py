def is_automorphic(number: int):
    """
    Check if a given number is an automorphic number.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is an automorphic number, False otherwise.
    """
    number_length = len(str(number))
    result = list(str(number ** 2))

    return list(str(number)) == result[-number_length:]


def main():
    number = int(input("Enter a number: "))
    if (is_automorphic(number)):
        print(f"{number} is an automorphic number")
    else:
        print(f"{number} is not an automorphic number")


if __name__ == "__main__":
    main()
