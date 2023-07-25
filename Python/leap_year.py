def is_leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    print(is_leap_year(2400))
    print(is_leap_year(2000))
    print(is_leap_year(2020))
    print(is_leap_year(2021))


if __name__ == "__main__":
    main()
