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


def main():
    number = int(input("Type a number: "))
    print(f" The divisors of {number} are: {divisors(number)}")


if __name__ == "__main__":
    main()
