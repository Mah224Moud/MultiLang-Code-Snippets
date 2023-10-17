import math


def divisors(number: int) -> list:
    """
    Determine a list of all the divisors of the given number.

    Parameters:
        number (int): The number for which to find the divisors.

    Returns:
        list: A list containing all the divisors of the given number.
    """
    divisors_list = []
    for i in range(1, number + 1):
        if (number % i) == 0:
            divisors_list.append(i)
    return divisors_list

def is_prime(number: int) -> bool:
    """
    Check if a given number is prime.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if (number <= 1):
        return False

    number_sqrt = int(math.sqrt(number)) + 1
    for i in range(2, number_sqrt):
        if ((number % i) == 0):
            return False
    return True


def prime_divisors(divisors: list) -> list:
    prime_divisors_list = []

    for i in divisors:
        if(is_prime(i)):
            prime_divisors_list.append(i)
    return prime_divisors_list

def main():
    number = int(input("Type a number: "))
    divisors_list = divisors(number)
    print(f"\n\nThe divisors of {number} are: {divisors_list}")
    
    print(f"The prime divisors of {number} are: {prime_divisors(divisors_list)}")

if __name__ == "__main__":
    main()