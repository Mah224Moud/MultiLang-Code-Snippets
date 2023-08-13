def is_spy_number(number: int) -> bool:
    """
    Check if a number is a spy number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a spy number, False otherwise.
    """
    values = list(str(number))
    total_product = 1
    total_sum = 0
    for i in values:
        total_product *= int(i)
        total_sum += int(i)

    return total_sum == total_product


def main():
    number = int(input("Enter a number: "))
    if (is_spy_number(number)):
        print(f"{number} is a spy number")
    else:
        print(f"{number} is not a spy number")


if __name__ == "__main__":
    main()
