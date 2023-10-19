def squared_binomial(a: int, b: int) -> int:
    """
    Calculate the square of a binomial expression using the formula a² + 2*a*b + b².

    Args:
        a (int): The first term of the binomial expression.
        b (int): The second term of the binomial expression.

    Returns:
        int: The result of squaring the binomial expression.
    """
    return (a**2) + (2*a*b) + (b**2)
    
def squared_binomial_with_subtraction(a: int, b: int) -> int:
    """
    Calculate the square of a binomial using the formula a² - 2*a*b + b².

    Parameters:
        a (int): The first integer value.
        b (int): The second integer value.

    Returns:
        int: The result of the squared binomial calculation.
    """
    return (a**2) - (2*a*b) + (b**2)
    
def sum_of_quares(a: int, b: int) -> int:
    """
    Calculate the sum of squares of two integers using the formula (a² + 2*a*b + b²) - 2*a*b.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The difference between the squared binomial of a and b and 2 times a times b.
    """
    return squared_binomial(a, b) - (2*a*b)
    
def difference_of_squares(a: int, b: int) -> int:
    """
    Calculates the difference of squares of two integers using the formula (a-b) * (a+b).

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The difference of the squares of the two integers.
    """
    return (a-b) * (a+b)

def main():

    print("Binomial Identity\n")

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(f"({a} + {b})² = {a}² + 2*{a}*{b} + {b}² = {a**2} + {2*a*b} + {b**2} = {squared_binomial(a, b)}")
    print(f"({a} - {b})² = {a}² - 2*{a}*{b} + {b}² = {a**2} - {2*a*b} + {b**2} = {squared_binomial_with_subtraction(a, b)}")
    print(f"{a}² + {b}² = ({a} + {b})² - 2*{a}*{b} = {a**2} + {2*a*b} - {b**2} = {sum_of_quares(a, b)}")
    print(f"{a}² - {b}² = ({a} - {b}) * ({a} + {b}) = {a-b} * {a+b} = {difference_of_squares(a, b)}")

if __name__ == "__main__":
    main()