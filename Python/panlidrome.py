def is_palindrome(word: str) -> bool:
    """
    Check if a given word is a palindrome.

    Args:
        word (str): The word to be checked.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("house"))
