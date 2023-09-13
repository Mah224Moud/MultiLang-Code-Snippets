import random


def dices(number: int) -> dict:
    """
    Generates a dictionary representation of different dice patterns based on the given number.

    Parameters:
        number (int): The number representing the dice pattern to be generated.

    Returns:
        dict: A dictionary containing the dice pattern corresponding to the given number.
    """
    DICES = {
        1: (
            "┌───────┐",
            "│       │",
            "│   ●   │",
            "│       │",
            "└───────┘"
        ),
        2: (
            "┌───────┐",
            "│ ●     │",
            "│       │",
            "│    ●  │",
            "└───────┘"
        ),
        3: (
            "┌───────┐",
            "│ ●     │",
            "│   ●   │",
            "│     ● │",
            "└───────┘"
        ),
        4: (
            "┌───────┐",
            "│ ●   ● │",
            "│       │",
            "│ ●   ● │",
            "└───────┘"
        ),
        5: (
            "┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ●   ● │",
            "└───────┘"
        ),
        6: (
            "┌───────┐",
            "│ ●   ● │",
            "│ ●   ● │",
            "│ ●   ● │",
            "└───────┘"
        )
    }

    return DICES[number]


def roll():
    """
    Rolls a dice and prints the result.

    This function generates a random number between 1 and 6 using the `random.randint()` function. 
    The generated number is then used as an argument to the `dices()` function, which returns a list 
    of dice faces corresponding to the random number. Finally, the function iterates over the dice 
    faces using a for loop and prints each face.

    Parameters:
        None

    Returns:
        None
    """
    rand_number = random.randint(1, 6)

    dice = dices(rand_number)
    for i in dice:
        print(i)


def main():
    print("*************************************************************")
    print("*********************** WELCOME *****************************")
    print("*************************************************************")

    print("\nMake your choice: ")
    print("1: Rolling the dices...")
    print("2: Exit")
    while True:
        choice = int(input("\nYour choice: "))

        if choice == 1:
            roll()
        elif choice == 2:
            print("Exiting...\nThank you!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
