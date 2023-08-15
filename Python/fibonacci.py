def fibonacci(limit: int):
    """
    Generate a list of Fibonacci numbers up to the given limit.

    Parameters:
        limit (int): The maximum number of Fibonacci numbers to generate.

    Returns:
        list: A list of Fibonacci numbers.
    """
    if limit <= 0:
        return []
    elif limit == 1:
        return [0]
    elif limit == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence


def main():
    limit = int(input("Enter the limit of the Fibonacci sequence: "))
    fib_sequence = fibonacci(limit)
    print(f"The Fibonacci sequence up to {limit} terms is: {fib_sequence}")


if __name__ == "__main__":
    main()
