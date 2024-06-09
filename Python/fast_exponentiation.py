def fast_exponentiation(number: int, power: int, modulo: int):
    """
        Calculates the result of raising a number to a power and taking the modulo of the result.

        Args:
            number (int): The number to be raised to a power.
            power (int): The power to which the number should be raised.
            modulo (int): The modulo value.

        Returns:
            int: The result of raising the number to the power and taking the modulo of the result.
    """
    while power > 0:
        right = ""
        if (power % 2):
            output = (output * number) % modulo
        number = (number*number) % modulo
        power //= 2
    return output


def main():
    number = 38
    power = 13
    mod = 87

    result = fast_exponentiation(number, power, mod)
    print(f"The result of {number}^{power} mod {mod} = {result} ")


if __name__ == "__main__":
    main()
