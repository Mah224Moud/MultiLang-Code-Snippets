def permute(tab: list, index):
    """
    Generates a new list by swapping two elements in the given list.

    Parameters:
        tab (list): The input list.
        index (int): The index of the first element to be swapped.

    Returns:
        list: The modified list with the elements at the specified indices swapped.
    """
    tmp = tab[index]
    tab[index] = tab[index+1]
    tab[index+1] = tmp
    return tab


def bubble_sort(tab: list) -> list:
    """
    Sorts a given list of numbers in ascending order using the bubble sort algorithm.

    Parameters:
    - tab (list): The list of numbers to be sorted.

    Returns:
    - list: The sorted list of numbers.
    """
    i = 0
    tab_length = len(tab)
    while i < tab_length:
        if i+1 != tab_length and tab[i] > tab[i+1]:
            tab = permute(tab, i)
            i = -1
        i += 1
    return tab


def main():
    numbers = [12, 4, 120, 8, 45, 7, -1, 44]
    print(f"Here are the list: {numbers}")
    print(f"Here are the sorted list: {bubble_sort(numbers)}")


if __name__ == "__main__":
    main()
