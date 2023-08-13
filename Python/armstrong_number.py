def is_armstrong_number(number: int) -> bool:
    """
    Check if a given number is an Armstrong number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    list_of_numbers = map(int, list(str(number)))
    result = 0
    for i in list_of_numbers:
        result += i ** len(str(number))
    return result == number


def main():
    number = int(input("Enter a number: "))
    if (is_armstrong_number(number)):
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")


if __name__ == "__main__":
    main()
