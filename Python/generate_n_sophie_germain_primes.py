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
    """
    return is_prime(number) and is_prime((2 * number) + 1)


def generate_n_sophie_germain_primes(limit: int) -> list:
    """
    Generates a list of the first `limit` Sophie Germain primes.

    Parameters:
        limit (int): The number of Sophie Germain primes to generate.

    Returns:
        list: A list of the first `limit` Sophie Germain primes.

    Examples:
        >>> generate_n_sophie_germain_primes(10)
        [2, 3, 5, 11, 23, 29, 41, 53, 83, 89]
    """
    sophie_germain_list = []
    start = 1
    while limit > 0:
        if is_sophie_germain_prime(start):
            sophie_germain_list.append(start)
            limit -= 1
        start += 1
    return sophie_germain_list


def main():
    number = int(input("Type the limit: "))
    print(
        f"Here are the first {number} Sophie Germain primes: {generate_n_sophie_germain_primes(number)}")


if __name__ == "__main__":
    main()
