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

def display_conway(n: int) -> None:
    """
    Recursively print the first n terms of Conway's Look-and-Say sequence.

    Args:
        n (int): The number of terms to print.

    Returns:
        None

    Examples:
        >>> display_conway(1)
        1
        >>> display_conway(3)
        1
        11
        21
        
    """
    if n == 1:
        print("1")
    else:
        display_conway(n - 1)
        print(conway_term(n))

def main() -> None:
    """
    Main function to execute the program.

    Prompts the user to enter the number of terms to display
    and prints the Conway sequence up to that term.

    Returns:
        None

    Examples:
        >>> # user inputs 2
        Enter the number of terms to display: 2
        1
        11
        >>> # user inputs 4
        Enter the number of terms to display: 4
        1
        11
        21
        1211
        
    """
    n = int(input("Enter the number of terms to display: "))
    display_conway(n)


if __name__ == "__main__":
    main()