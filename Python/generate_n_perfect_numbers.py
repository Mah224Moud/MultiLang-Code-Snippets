def is_perfect_number(number: int) -> bool:
    """
    Checks if a given number is a perfect number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a perfect number, False otherwise.
    """
    list_of_divisors = []
    for i in range(1, number):
        if number % i == 0:
            list_of_divisors.append(i)
    return sum(list_of_divisors) == number


def generate_n_perfect_numbers(limit: int) -> list:
    """
    Generate a list of n perfect numbers up to a given limit.

    Parameters:
        limit (int): The upper limit to generate perfect numbers up to.

    Returns:
        list: A list of n perfect numbers.

    """
    perfect_numbers = []
    start = 1
    while limit > 0:
        if (is_perfect_number(start)):
            perfect_numbers.append(start)
            limit -= 1
        start += 1
    return perfect_numbers


def main():
    print(generate_n_perfect_numbers(4))


if __name__ == "__main__":
    main()
