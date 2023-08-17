def binary_to_complement(binary: int) -> dict:
    """
    Convert a binary number to its complement.

    Args:
        binary (int): The binary number to be converted.

    Returns:
        dict: A dictionary containing the original binary number and its complement.

    Example:
        >>> binary_to_complement(101)
        {'original': '101', 'complement': '010'}
    """
    converted = list(str(binary))
    complement = []
    for i in converted:
        if i == "0":
            complement.append("1")
        else:
            complement.append("0")
    return {
        "original": converted,
        'complement': complement
    }


def mai():
    binary = int(input("Enter a binary number: "))
    result = binary_to_complement(binary)
    print(f"\n\nOriginal binary:   {''.join(result['original'])}")
    print(f"Complement binary: {''.join(result['complement'])}")


if __name__ == "__main__":
    mai()
