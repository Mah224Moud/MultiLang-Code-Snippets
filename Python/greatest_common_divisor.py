def divisors(number: int) -> list:
    """
    Determine a list of all the divisors of the given number.

    Parameters:
        number (int): The number for which to find the divisors.

    Returns:
        list: A list containing all the divisors of the given number.
    """
    divisors_list = []
    for i in range(1, number + 1):
        if (number % i) == 0:
            divisors_list.append(i)
    return divisors_list


def common(firstList: list, secondList: list) -> list:
    """
        Find the common elements between two lists.

        Args:
            firstList (list): The first list.
            secondList (list): The second list.

        Returns:
            list: A list containing the common elements between the two input lists.

        Example:
            >>> common([1, 2, 3], [2, 3, 4])
            [2, 3]
    """
    uniqueFirst = set(firstList)
    uniqueSecond = set(secondList)

    return list(uniqueFirst.intersection(uniqueSecond))


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of `a` and `b`.

    Example:
        >>> gcd(12, 18)
        6
    """
    a_divisors = divisors(a)
    b_divisors = divisors(b)

    common_divisors = common(a_divisors, b_divisors)

    return max(common_divisors)


def main():
    firstNumber = int(input("Type the first number: "))
    secondNumber = int(input("Type the second number: "))

    print(
        f"The greatest common divisor of {firstNumber} and {secondNumber} is {gcd(firstNumber, secondNumber)}")


if __name__ == "__main__":
    main()
