def series(first_resistance: float, second_resistance: float, third_resistance: float) -> float:
    """
    Calculate the total resistance of a series circuit.

    Parameters:
        first_resistance (float): The resistance of the first component in the series circuit.
        second_resistance (float): The resistance of the second component in the series circuit.
        third_resistance (float): The resistance of the third component in the series circuit.

    Returns:
        float: The total resistance of the series circuit.
    """
    return first_resistance + second_resistance + third_resistance


def parallel(first_resistance: float, second_resistance: float, third_resistance: float) -> float:
    """
    Calculate the equivalent resistance of three resistors connected in parallel.

    Args:
        first_resistance (float): The resistance value of the first resistor.
        second_resistance (float): The resistance value of the second resistor.
        third_resistance (float): The resistance value of the third resistor.

    Returns:
        float: The equivalent resistance of the three resistors connected in parallel.
    """
    return (first_resistance * second_resistance * third_resistance) / ((first_resistance * second_resistance) + (second_resistance * third_resistance) + (third_resistance * first_resistance))


def main():
    print("This program calculates the total resistance of a series and equivalent resistance of three resistors connected in parallel in a circuit. \n")

    first = float(input("Type your first resistance: "))
    second = float(input("Type your second resistance: "))
    third = float(input("Type your third resistance: "))
    print(
        f"\n\nThe total resistance of the series circuit is {series(first, second, third)}")
    print(
        f"The equivalent resistance of the three resistors connected in parallel is {parallel(first, second, third)}")


if __name__ == "__main__":
    main()
