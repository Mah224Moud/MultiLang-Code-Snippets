import random


def swap(tab: list, pivot_index: int, last_index: int) -> None:
    """
    Swaps the elements in a list.

    Args:
        tab (list): The list containing the elements to be swapped.
        pivot_index (int): The index of the first element to be swapped.
        last_index (int): The index of the second element to be swapped.

    Returns:
        None: This function does not return anything.
    """
    tmp = tab[pivot_index]
    tab[pivot_index] = tab[last_index]
    tab[last_index] = tmp


def partition(tab: list, first_index: int, last_index: int, pivot) -> int:
    """
    Partition the given list `tab` based on the pivot element.

    Args:
        tab (list): The list to be partitioned.
        first_index (int): The index of the first element in the range to be partitioned.
        last_index (int): The index of the last element in the range to be partitioned.
        pivot: The pivot element used for partitioning.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    swap(tab, pivot, last_index)
    j = first_index

    for i in range(first_index, last_index):
        if tab[i] <= tab[last_index]:
            swap(tab, i, j)
            j += 1
    swap(tab, last_index, j)
    return j


def pivot_choice(tab: list, first_index: int, last_index: int):
    """
    Generate a random pivot choice for quicksort.

    Parameters:
        tab (list): The list to choose a pivot from.
        first_index (int): The index of the first element in the range.
        last_index (int): The index of the last element in the range.

    Returns:
        int: The randomly chosen pivot value.

    """
    return random.randint(first_index, last_index)


def quick_sort(tab: list, first_index: int, last_index: int):
    """
    Sorts a list using the quicksort algorithm.

    Parameters:
    - tab (list): The list to be sorted.
    - first_index (int): The index of the first element to be considered in the sorting.
    - last_index (int): The index of the last element to be considered in the sorting.

    Returns:
    - None

    Algorithm:
    - Choose a pivot element from the list.
    - Partition the list so that all elements smaller than the pivot are on its left, and all elements greater than the pivot are on its right.
    - Recursively apply the quicksort algorithm to the left and right partitions of the list.
    """
    if first_index < last_index:
        pivot = pivot_choice(tab, first_index, last_index)
        pivot = partition(tab, first_index, last_index, pivot)
        quick_sort(tab, first_index, pivot-1)
        quick_sort(tab, pivot+1, last_index)


def main():

    numbers = [-50, 25, 10, 1, -4, 7.8]
    print(f"Here are the list: {numbers}")
    quick_sort(numbers, 0, len(numbers)-1)
    print(f"Here are the sorted list: {numbers}")


if __name__ == "__main__":
    main()
