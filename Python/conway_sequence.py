def read_and_say(sequence: str) -> str:
    """
    Generate the next term in Conway's Look-and-Say sequence.

    Args:
        sequence (str): The current term in the sequence.

    Returns:
        str: The next term in the sequence.
    """
    result = ""
    count = 1

    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            count += 1
        else:
            result += str(count) + sequence[i]
            count = 1

    result += str(count) + sequence[-1]
    return result

""" 
Examples:
        >>> read_and_say("1")
        '11'
        >>> read_and_say("11")
        '21'
        >>> read_and_say("1211")
        '111221'
"""
