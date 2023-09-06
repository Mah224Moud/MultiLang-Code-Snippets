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


def prime_factorization(number: int) -> dict:
    """
    Calculates the prime factorization of a given number.

    Parameters:
        number (int): The number to be factorized.

    Returns:
        dict: A dictionary representing the prime factorization of the number. The keys are the prime factors and the values are the corresponding exponents.
    Example:
        >>> prime_factorization(12)
        {2: 2, 3: 1}
    """
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


def lcm(a: int, b: int) -> int:
    """
    Calculates the least common multiple (LCM) of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The least common multiple of a and b.

    Examples:
        >>> lcm(18, 12)
        36
        >>> lcm(682, 496)
        5456
    """
    a_multiples = prime_factorization(a)
    b_multiples = prime_factorization(b)

    result = 1

    for key in a_multiples.keys() | b_multiples.keys():
        result *= int(key) ** max(a_multiples.get(key, 0),
                                  b_multiples.get(key, 0))

    return result


def main():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    print(
        f"The least common multiple of {first_number} and {second_number} is {lcm(first_number, second_number)}")


if __name__ == "__main__":
    main()
