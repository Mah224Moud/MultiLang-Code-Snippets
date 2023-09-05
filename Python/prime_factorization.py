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


def prime_factorization(number: int) -> list:
    """
    Generate the prime factorization of a given number.

    Parameters:
        number (int): The number to be factorized.

    Returns:
        list: A list of prime factors of the given number.

    Example:
        >>> prime_factorization(12)
        [2, 2, 3]
    """
    multiple = []
    start = 2
    while number > 1:
        if is_prime(start):
            if (number % start) == 0:
                number //= start
                multiple.append(start)
            else:
                start += 1
        else:
            start += 1

    return multiple


# The following code is the same as the above only with a different return type and exposes the exponents.
"""
def prime_factorization(number: int) -> dict:
    Calculates the prime factorization of a given number.

    Parameters:
        number (int): The number to be factorized.

    Returns:
        dict: A dictionary representing the prime factorization of the number. The keys are the prime factors and the values are the corresponding exponents.
    Example:
        >>> prime_factorization(12)
        {2: 2, 3: 1}
    
    multiple = {}
    start = 2
    while number > 1:
        if is_prime(start):
            if (number % start) == 0:
                number //= start
                if str(start) in multiple.keys():
                    multiple[str(start)] += 1
                else:
                    multiple.__setitem__(str(start), 1)
            else:
                start += 1
        else:
            start += 1
    return multiple
"""


def main():
    number = int(input("Type a number: "))
    print(
        f"The prime factorization of {number} is: {prime_factorization(number)}")


if __name__ == "__main__":
    main()
