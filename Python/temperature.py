def temperature(temperature: float, temp_type: str) -> None:
    """
    Convert temperature from one unit to another based on the given temperature and temperature type.

    Parameters:
    - temperature (float): The temperature value to be converted.
    - temp_type (str): The type of temperature value provided. Accepted values are "Fahrenheit", "Celsius", and "Kelvin".

    Returns:
    - None

    Example:
    temperature(32, "Fahrenheit")
    Output: 32°F is 0°C and 273.15°K
    """
    if (temp_type == "Fahrenheit"):
        celsius = round(((temperature - 32) * (5/9)), 2)
        kelvin = round(((temperature - 32) * (5/9)) + 273.15, 2)
        print(f"{temperature}°F is {celsius}°C and {kelvin}°K")

    elif (temp_type == "Celsius"):
        fahrenheit = round((temperature * (9/5)) + 32, 2)
        kelvin = round(temperature + 273.15, 2)
        print(f"{temperature}°C is {fahrenheit}°F and {kelvin}°K")

    else:
        celsius = round(temperature - 273.15, 2)
        fahrenheit = round(((temperature - 273.15) * (9/5)) + 32, 2)
        print(f"{temperature}°K is {celsius}°C and {fahrenheit}°F")


def main():
    temperature_types = ["fahrenheit", "celsius", "kelvin"]

    print("\n************************************")
    print("Here are the list of temperatures:")
    print(", ".join(temperature_types))
    print("************************************\n\n")
    temp_type = input("What type of temperature do you want to convert : ")

    while temp_type.lower() not in temperature_types:
        temp_type = input(
            f"This is not a valid option !!!\nTry again using one of the following options [{', '.join(temperature_types)}] : ")

    print(f"\nYou have chosen {temp_type.capitalize()}.\n")
    temperature_input = input("Type a temperature : ")
    temperature(float(temperature_input), temp_type.capitalize())


if __name__ == "__main__":
    main()
