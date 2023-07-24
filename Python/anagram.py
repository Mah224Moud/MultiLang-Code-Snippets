def is_same_strings(first: str, second: str) -> bool:
    """
    Check if two strings are the same.

    Args:
        first (str): The first string.
        second (str): The second string.

    Returns:
        bool: True if the two strings are the same, False otherwise.
    """
    return first == second


def convert_string_to_sorted_list(word: str) -> list:
    """
    Converts a string to a sorted list.

    Args:
        word (str): The string to be converted.

    Returns:
        list: A sorted list of characters from the input string.
    """
    return sorted(word)


def is_anagram(firstList: list, secondList: list) -> bool:
    """
    Check if two lists are anagrams of each other.

    Args:
        firstList (list): The first list.
        secondList (list): The second list.

    Returns:
        bool: True if the lists are anagrams, False otherwise.
    """
    if (len(firstList) != len(secondList)):
        return False
    else:
        for i, j in zip(firstList, secondList):
            if i != j:
                return False
        return True


def main():
    firstInput = input("Type a word: ")
    secondInput = input("Type another word: ")

    firstWord = firstInput.strip()
    secondWord = secondInput.strip()

    firstList = convert_string_to_sorted_list(firstWord)
    secondList = convert_string_to_sorted_list(secondWord)

    if (is_same_strings(firstWord, secondWord)):
        print("The words are not anagrams")
    else:
        if (is_anagram(firstList, secondList)):
            print("The words are anagrams")
        else:
            print("The words are not anagrams")


if __name__ == "__main__":
    main()
