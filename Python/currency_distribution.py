def calculate_currency_distribution(amount: float) -> dict:
    """
    Calculate the distribution of currency denominations for a given amount.

    Parameters:
        amount (float): The amount for which the currency distribution needs to be calculated.

    Returns:
        dict: A dictionary containing the distribution of currency denominations. The keys are the denomination names, and the values are lists containing the category (bills or coins) and the count of that denomination.

    Example:
        calculate_currency_distribution(123.45)
        Output: 
        {
            "Hundred": ["bills", 1],
            "Fifty": ["bills", 0],
            "Twenty": ["bills", 1],
            "Ten": ["bills", 0],
            "Five": ["bills", 0],
            "Two": ["coins", 1],
            "One": ["coins", 1],
            "Fifty cents": ["coins", 0],
            "Twenty cents": ["coins", 2],
            "Ten cents": ["coins", 0],
            "Five cents": ["coins", 1],
            "Two cents": ["coins", 0],
            "One cent": ["coins", 0]
        }
    """
    denominations = [
        ("Hundred", 100, "bills"),
        ("Fifty", 50, "bills"),
        ("Twenty", 20, "bills"),
        ("Ten", 10, "bills"),
        ("Five", 5, "bills"),
        ("Two", 2, "coins"),
        ("One", 1, "coins"),
        ("Fifty cents", 0.5, "coins"),
        ("Twenty cents", 0.2, "coins"),
        ("Ten cents", 0.1, "coins"),
        ("Five cents", 0.05, "coins"),
        ("Two cents", 0.02, "coins"),
        ("One cent", 0.01, "coins")
    ]

    distribution = {}
    remaining_amount = amount

    for denomination_name, value, category in denominations:
        if value >= 1:
            count = int(remaining_amount // value)
        else:
            # Added a small value to account for floating-point precision
            count = int(remaining_amount / value + 0.001)
        distribution[denomination_name] = [category, count]
        remaining_amount -= count * value

    return distribution


def main():
    print("\n*******************************************************************************************")
    print("*************************************** WELCOME *******************************************")
    print("*******************************************************************************************\n\n")

    amount = float(input("Enter amount: "))
    currency_distribution = calculate_currency_distribution(amount)

    print(f"Here is {amount} currency distribution:\n")
    for denomination_name, currency_count in currency_distribution.items():
        if currency_count[1] > 0:
            print(
                f"{currency_count[1]} {denomination_name} {currency_count[0]}")


if __name__ == "__main__":
    main()
