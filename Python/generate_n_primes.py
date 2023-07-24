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


def generate_n_primes(limit: int) -> list:
    """
    Generate a list of the first n prime numbers.

    Parameters:
    limit (int): The maximum number of prime numbers to generate.

    Returns:
    list: A list of the first n prime numbers.
    """

    start = 2
    list = []
    while limit > 0:
        if (is_prime(start)):
            list.append(start)
            limit -= 1
        start += 1
    return list


def main():

    limit = input("Type a limit: ")
    print("Here are the first", limit, "primes:", generate_n_primes(int(limit)))


if __name__ == "__main__":
    main()
