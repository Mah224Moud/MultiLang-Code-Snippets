def fast_exponentiation(number: int, power: int, modulo: int):
    output = 1
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
