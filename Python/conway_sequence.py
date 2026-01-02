def read_and_say(sequence: str) -> str:
    """
    Generate the next term in Conway's Look-and-Say sequence.

    Args:
        sequence (str): The current term in the sequence.

    Returns:
        str: The next term in the sequence.
 
    Examples:
        >>> read_and_say("1")
        '11'
        >>> read_and_say("11")
        '21'
        >>> read_and_say("1211")
        '111221'
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

def conway_term(n: int) -> str:
    """
    Recursively compute the nth term of Conway's Look-and-Say sequence.

    Args:
        n (int): The term number to compute (1-based index).

    Returns:
        str: The nth term of the sequence.

    Examples:
        >>> conway_term(1)
        '1'
        >>> conway_term(4)
        '1211'
        >>> conway_term(5)
        '111221'
    """
    if n == 1:
        return "1"
    else:
        return read_and_say(conway_term(n - 1))