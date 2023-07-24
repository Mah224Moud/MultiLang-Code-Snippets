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


def main():
    number = int(input("Type a number: "))
    if (is_prime(number)):
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")


if __name__ == "__main__":
    main()
