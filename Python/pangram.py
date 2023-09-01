def is_pangram(word: str) -> bool:
    """
    Check if the given word is a pangram.

    Args:
        word (str): The word to be checked.

    Returns:
        bool: True if the word is a pangram, False otherwise.

    Examples:
        >>> is_pangram("The quick brown fox jumps over the lazy dog.")
        True
        >>> is_pangram("The quick brown fox jumps over the lazy cat.")
        False
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(word.lower()) >= alphabet


def main():
    word = input("Type a word: ")
    if is_pangram(word):
        print(f"The word '{word}' is a pangram")
    else:
        print(f"The word '{word}' is not a pangram")


if __name__ == "__main__":
    main()
