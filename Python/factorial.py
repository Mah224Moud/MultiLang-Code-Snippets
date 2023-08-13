def factorial(number: int) -> int:
    """
    Calculate the factorial of a given number.

    Args:
        number (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the given number.
    """
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    number = int(input("Type a number: "))
    print(f"{number}! is {factorial(number)}")


if __name__ == "__main__":
    main()
