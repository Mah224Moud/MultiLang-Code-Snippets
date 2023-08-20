def seconds_to_hms(seconds: int) -> str:
    """
    Converts seconds to hours, minutes, and seconds.

    Parameters:
        seconds (int): The number of seconds to convert.

    Returns:
        str: The converted time in the format "hours:minutes:seconds".

    Examples:
        >>> seconds_to_hms(3600)
        '1h:0m:0s'
        >>> seconds_to_hms(54780)
        '15h:13m:0s'
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = ((seconds % 3600) % 60)

    return f"{hours}h:{minutes}m:{sec}s"


def main():
    seconds = int(input("Enter seconds: "))
    print(f"{seconds} seconds is {seconds_to_hms(seconds)}")


if __name__ == "__main__":
    main()
