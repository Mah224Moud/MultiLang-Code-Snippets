import math


def is_prime(number: int) -> bool:
    """
    Check if a given number is prime.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if (number <= 1):
        return False

    number_sqrt = int(math.sqrt(number)) + 1
    for i in range(2, number_sqrt):
        if ((number % i) == 0):
            return False
    return True


def is_sophie_germain_prime(number: int) -> bool:
    """
    Check if a number is a Sophie Germain prime.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a Sophie Germain prime, False otherwise.

    Examples:
        >>> is_sophie_germain_prime(3)
        True
        >>> is_sophie_germain_prime(7)
        False
    """
    return is_prime(number) and is_prime((2 * number) + 1)


def main():
    number = int(input("Type a number: "))
    if (is_sophie_germain_prime(number)):
        print(f"{number} is Sophie Germain prime")
    else:
        print(f"{number} is not Sophie Germain prime")


if __name__ == "__main__":
    main()
