def kth_factor(number: int, k: int) -> int:
    """
        Calculates the kth factor of a given number.

        Args:
            number (int): The number to find the kth factor of.
            k (int): The index of the factor to retrieve.

        Returns:
            int: The kth factor of the given number. If k is greater than the number of factors or less than 1, -1 is returned.
    """
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return -1 if k > len(factors) or k < 1 else factors[k - 1]


def main():
    number = 12
    k = 3
    print(f"The {k}th factor of {number} is {kth_factor(number, k)}")


if __name__ == "__main__":
    main()
