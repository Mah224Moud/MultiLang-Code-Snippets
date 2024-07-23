import random as rand


def generate_random_key(lenght: int) -> str:
    """
    Generates a random key of a specified length.

    Parameters:
        lenght (int): The length of the random key to be generated.

    Returns:
        str: The randomly generated key.
    """
    random_key = ""
    letters = "".join(chr(i) for i in range(97, 123))
    random_key = "".join(rand.SystemRandom().choice(letters)
                         for _ in range(lenght))
    return random_key


def is_aphabet(text: str) -> bool:
    """
    Check if the given text is a valid alphabet character.

    Parameters:
        text (str): The text to be checked.

    Returns:
        bool: True if the text is a valid alphabet character, False otherwise.
    """
    return "A" <= text.upper() <= "Z"


def vernam(text: str, key: str, encode: bool = False) -> str:
    """
    Decodes or encodes a text using the Vernam cipher algorithm for the given text and key.

    Parameters:
        text (str): The text to be encrypted.
        key (str): The key used for encryption.
        encode (bool, optional): Whether to encode or decode the text. Defaults to False.

    Returns:
        str: The decoded text.

    Example usage:
    ```
    text = "DSCWR"
    key = "WORLD"
    decoded_text = vernam(text, key)
    print(decoded_text)  # Output: "HELLO"

    text = "HELLO"
    key = "WORLD"
    encoded_text = vernam(text, key, encode=True)
    print(encoded_text)  # Output: "DSCWR"
    ```
    """
    decalage = 65
    result = ""
    for t, k in zip(text, key):
        tval = ord(t.upper()) - decalage
        kval = ord(k.upper()) - decalage

        if encode:
            calcul = (tval + kval) % 26
        else:
            calcul = (tval - kval) % 26
        if is_aphabet(t):
            if t.isupper():
                result += chr(calcul + decalage).upper()
            else:
                result += chr(calcul + decalage).lower()
        else:
            result += t
    return result


def main():
    text = "HELLO WORLD"
    key = generate_random_key(len(text)).upper()

    encode = vernam(text, key, encode=True)

    print(f"'{text}' encoded with '{key}' using VERNAM cipher = '{encode}'")


if __name__ == "__main__":
    main()
