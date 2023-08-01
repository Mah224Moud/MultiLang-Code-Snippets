import requests

API_KEY = "your_rapidapi_key_here"


def get_current_prices(API_KEY: str, from_currency: str) -> dict:
    """
    Retrieves the current exchange rates for a given currency.

    :param API_KEY: The API key for accessing the exchange rate API. Must be a string.
    :param from_currency: The currency for which to retrieve exchange rates. Must be a string.
    :return: A dictionary containing the current exchange rates for the specified currency.
    """
    url = f"https://exchangerate-api.p.rapidapi.com/rapid/latest/{from_currency}"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "exchangerate-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data["rates"]


def get_all_currencies(API_KEY: str) -> list:
    """
    Retrieves a list of all available currencies using the specified API key.

    Args:
        API_KEY (str): The API key used to authenticate the request.

    Returns:
        list: A sorted list of currency codes.
    """
    url = f"https://exchangerate-api.p.rapidapi.com/rapid/latest/USD"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "exchangerate-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return sorted(list(data["rates"].keys()))


def determinate_current_exchange_price(currencies: dict, from_currency: str, to_currency: str, amount: float):
    """
    Calculates and prints the exchange rate for a given amount between two currencies.

    Parameters:
        currencies (dict): A dictionary containing the exchange rates for different currencies.
        from_currency (str): The currency that the amount is in.
        to_currency (str): The currency that the amount will be converted to.
        amount (float): The amount of money to be converted.

    Returns:
        None
    """
    _to = currencies[to_currency]
    formatter_to = "{:,.2f}".format(_to)
    value = round(amount * _to, 2)
    formatted_number = "{:,.2f}".format(value)

    print(f"\n\n{amount} {from_currency} to {to_currency} = {formatted_number}\nAt a rate of 1 {from_currency} = {formatter_to} {to_currency}")


def currency_input(currencies: list, input_type: str) -> str:
    """
    Generates a currency input based on the given list of currencies and input type.

    Args:
        currencies (list): A list of currencies.
        input_type (str): The type of input. Possible values are "from" or any other string.

    Returns:
        str: The user input in uppercase, after validating against the list of currencies.
    """
    if input_type == "from":
        user_input = input("\nEnter your current currency: ")
    else:
        user_input = input("\nEnter the target currency for conversion: ")
    while user_input.upper() not in currencies:
        user_input = input(
            f"\n\nThis is not a valid option !!!\nTry again using one of the following options:\n[ {', '.join(currencies)} ] : ")
    return user_input.upper()


def currency_amount() -> float:
    """
    Function to prompt the user to enter an amount and validate that it is greater than 0.

    Parameters:
    None

    Returns:
    float: The amount entered by the user.
    """
    amount = float(input("\nEnter the amount you wish to convert: "))
    while amount <= 0.0:
        amount = float(input(
            "\n\nThe amount must be greater than 0 !!!\nEnter the amount you wish to convert: "))
    return amount


def main():
    currencies_list = get_all_currencies(API_KEY)

    print("*******************************************************************************************")
    print("*************************************** WELCOME *******************************************")
    print("*******************************************************************************************")

    print(
        f"Here are the {len(currencies_list)} current currencies list:\n{', '.join(currencies_list)}")

    from_currency = currency_input(currencies_list, "from")
    to_currency = currency_input(currencies_list, "to")

    while from_currency == to_currency:
        print("\n\n*******************************************")
        print("The two currencies must be different.")
        print("*******************************************")
        to_currency = currency_input(currencies_list, "to")
    amount = currency_amount()

    current_prices = get_current_prices(API_KEY, from_currency)
    determinate_current_exchange_price(
        current_prices, from_currency, to_currency, amount)


if __name__ == "__main__":
    main()
