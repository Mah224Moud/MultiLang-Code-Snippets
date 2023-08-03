import random


def shuffle(word: str) -> str:
    """
    Generate a shuffled version of the input word.

    Args:
        word (str): The word to be shuffled.

    Returns:
        str: The shuffled word.
    """
    return ''.join(random.sample(word, len(word)))


def main():
    word = input("Type the world you want to shuffle: ")
    print(f"The shuffle of the word '{word}' is '{shuffle(word)}'")


if __name__ == "__main__":
    main()
