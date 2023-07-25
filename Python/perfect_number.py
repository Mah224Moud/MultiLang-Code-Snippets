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


def main():
    number = int(input("Type a number : "))
    if (is_perfect_number(number)):
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")


if __name__ == "__main__":
    main()
