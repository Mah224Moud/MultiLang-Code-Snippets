def united_keys(firstDictionary: dict, secondDictionary: dict) -> list:
    """
    Generates a list of unique keys by combining the keys from two dictionaries.

    Args:
        firstDictionary (dict): The first dictionary.
        secondDictionary (dict): The second dictionary.

    Returns:
        list: A list of unique keys from both dictionaries.

    Example:
        >>> united_keys({'a': 1, 'b': 2}, {'b': 2, 'c': 3})
        ['b', 'c', 'a']
    """

    uniqueFirst = set(firstDictionary.keys())
    uniqueSecond = set(secondDictionary.keys())

    return list(uniqueFirst | uniqueSecond)


def main():
    firstDictionary = {'a': 1, 'b': 2}
    secondDictionary = {'b': 2, 'c': 3}
    print(
        f"The united keys are: {united_keys(firstDictionary, secondDictionary)}")


if __name__ == "__main__":
    main()
