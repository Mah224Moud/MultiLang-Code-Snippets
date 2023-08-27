import re


def hms_to_seconds(time: str) -> int:
    """
    Converts a time in hours, minutes, and seconds format to the total number of seconds.

    Args:
        time (str): The time in hours, minutes, and seconds format. The format should be "HH:MM:SS".

    Returns:
        int: The total number of seconds.

    Example:
        >>> hms_to_seconds("01:30:45")
        5445
    """
    splitted_time = time.split(":")
    hours = int(splitted_time[0]) * 3600
    minutes = int(splitted_time[1]) * 60
    sec = int(splitted_time[2])

    return hours + minutes + sec


def main():
    time = input("Enter time in format HH:MM:SS: ")

    while not re.match(r"^\d{2}:\d{2}:\d{2}$", time):
        time = input("Enter time in format HH:MM:SS: ")

    splitted_time = time.split(":")
    hours = int(splitted_time[0])
    minutes = int(splitted_time[1])
    sec = int(splitted_time[2])
    print(f"{hours}h{minutes}m{sec}s is {hms_to_seconds(time)}seconds")


if __name__ == "__main__":
    main()
