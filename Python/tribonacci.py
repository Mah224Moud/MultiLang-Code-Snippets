def tribonacci(limit: int) -> list:
    """
    Generate a list of Tribonacci numbers up to the given limit.

    Parameters:
        limit (int): The maximum number of Tribonacci numbers to generate.

    Returns:
        list: A list of Tribonacci numbers.

    Examples:
        >>> tribonacci(10)
        [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    """
    if limit <= 0:
        return []
    elif limit == 1:
        return [0]
    elif limit == 2:
        return [0, 1]
    elif limit == 3:
        return [0, 1, 1]

    trib_sequence = [0, 1, 1]
    while len(trib_sequence) < limit:
        trib_sequence.append(
            trib_sequence[-1] + trib_sequence[-2] + trib_sequence[-3])

    return trib_sequence


def main():
    limit = int(input("Enter the limit of the Tribonacci sequence: "))
    trib_sequence = tribonacci(limit)
    print(f"The Tribonacci sequence up to {limit} terms is: {trib_sequence}")


if __name__ == "__main__":
    main()
