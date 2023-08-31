import requests

API_KEY = "YOUR_RAPIDAPI_KEY_HERE"


def get_surah(surah_number: int, API_KEY: str) -> None:
    """
    Retrieves information about a specific Surah (chapter) of the Quran.

    Args:
        surah_number (int): The number of the Surah to retrieve.
        API_KEY (str): The API key to authenticate the request.

    Returns:
        None: This function does not return anything.
    """

    url = f"https://al-quran1.p.rapidapi.com/{surah_number}"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "al-quran1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    surah_name = data["surah_name"]
    surah_name_ar = data['surah_name_ar']
    surah_type = data['type']
    description = data['description']
    total_verses = data["total_verses"]
    verses = data['verses']

    print(f"\n\n{''.center(70, '*')}")
    print(f"{''.center(70, '*')}")
    print(f"{surah_name_ar.center(70, '*') }")
    print(f"{surah_name.center(70, '*') }")
    print(
        f"***************** Type: {surah_type.capitalize()}, number of verses: {total_verses} *****************")
    print(f"{''.center(70, '*')}")
    print(f"{''.center(70, '*')}")
    print(f"{' Description '.center(70, '*')}")
    print(description)
    print(f"{''.center(70, '*')}")
    print(f"{''.center(70, '*')}\n\n")

    for i in range(1, len(verses)+1):
        print(f"{i}: {verses[str(i)]['content']}")
        print(f"{verses[str(i)]['translation_eng']}\n\n")


def main():
    surah_number = int(input("Enter a surah number between 1 to 114: "))

    while (surah_number > 114 or surah_number < 1):
        surah_number = int(input("Enter a surah number between 1 to 114: "))
    get_surah(surah_number, API_KEY)


if __name__ == "__main__":
    main()
