def swap(tab: list, first_index: int, second_index: int) -> None:
    """
    Swaps two elements in a given list.

    Args:
        tab (list): The list in which to perform the swap.
        first_index (int): The index of the first element to swap.
        second_index (int): The index of the second element to swap.

    Returns:
        None: This function does not return anything.
    """
    tmp = tab[first_index]
    tab[first_index] = tab[second_index]
    tab[second_index] = tmp


def selection_sort(tab: list) -> None:
    """
    Sorts a list of elements using the selection sort algorithm.

    Parameters:
        tab (list): The list of elements to be sorted.

    Returns:
        None: This function does not return anything.
    """
    length = len(tab)
    for i in range(length - 1):
        minimum = i
        for j in range(i+1, length):
            if tab[j] < tab[minimum]:
                minimum = j
        if minimum != i:
            swap(tab, i, minimum)


def main():
    numbers = [33, -50, 25, 10, 1, -4, 7.8]
    print(f"Here are the list: {numbers}")
    selection_sort(numbers)
    print(f"Here are the sorted list: {numbers}")


if __name__ == "__main__":
    main()
