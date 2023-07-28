import random


def password_generator(length: int, password_type: str) -> None:
    """
    Generates a password of a specified length and type.

    Parameters:
        length (int): The length of the password to be generated.
        password_type (str): The type of password to be generated. Can be one of the following options:
            - "lower": Generates a password with lower and uppercase alphabets.
            - "medium": Generates a password with lower and uppercase alphabets and numbers.
            - "high": Generates a password with lower and uppercase alphabets, numbers, and special characters.

    Returns:
        None

    Example:
        password_generator(10, "medium")
    Output: Your generated password is: 2l93oOXZLd
    """
    lower = "abcdefghijklmnopqrstuwxyz"
    upper = "ABCDEFGHIJKLMNOPSQRSTUVWXYZ"
    numbers = "0123456789"
    special = "&~{([-_\ç@)]=}$*!:;,/"

    if password_type == "lower":
        united = lower + upper
        print("".join(random.sample(united, length)))
    elif password_type == "medium":
        united = lower + upper + numbers
        print("".join(random.sample(united, length)))
    else:
        united = lower + upper + numbers + special
        print("".join(random.sample(united, length)))


def main():
    password_type_list = ["lower", "medium", "strong"]
    password_type = ""
    length = 0

    print("*************************************************************")
    print(
        f"Here are the list of passwords types: {', '.join(password_type_list)}")
    print("*************************************************************\n\n")

    password_type = input("What type of password do you want to generate : ")

    while password_type.lower() not in password_type_list:
        password_type = input(
            f"This is not a valid option !!!\nTry again using one of the following options [{', '.join(password_type_list)}] : ")
    length = int(input("\nType your password length : "))
    while length < 8:
        length = int(
            input("Try again !!!!\nThe password length must be at least 8: "))

    print("\n\nHere's your generated password : ")
    password_generator(length, password_type)


if __name__ == "__main__":
    main()
