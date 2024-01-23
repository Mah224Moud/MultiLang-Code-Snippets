def swap(numbers: list, first_index: int, second_index: int) -> None:
    """
    Swaps the elements at the specified first and second indices in the given list of numbers.
    
    Parameters:
    - numbers: list, the list of numbers
    - first_index: int, the index of the first element to be swapped
    - second_index: int, the index of the second element to be swapped
    
    Returns:
    None
    """
    temp = numbers[first_index]
    numbers[first_index] = numbers[second_index]
    numbers[second_index] = temp


def insertion_sort(numbers: list) -> None:
    """
    Sorts the input list of numbers in place using the insertion sort algorithm.

    Args:
        numbers (list): The list of numbers to be sorted.

    Returns:
        None
    """
    tab_lenght = len(numbers)
    
    for i in range (1, tab_lenght):
        temp = numbers[i]
        temp_indice = i
        
        for j in reversed(range(i)):
            if(numbers[j] > temp ):
                swap(numbers, temp_indice, j)
                temp_indice= j


def main():
    numbers = [33, -50, 25, 10, 1, -4, 7]
    print(f"Here are the list: {numbers}")
    insertion_sort(numbers)
    print(f"Here are the sorted list: {numbers}")


if __name__ == "__main__":
    main()