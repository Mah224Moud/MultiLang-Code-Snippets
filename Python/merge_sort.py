def merge_sort(numbers: list) -> list:
    """
    Perform a merge sort on the given list of numbers.

    Parameters:
    - numbers: a list of numbers to be sorted

    Returns:
    - a list of sorted numbers
    """
    length = len(numbers)
    if(length > 1):
        middle = length // 2
        left = merge_sort(numbers[:middle])
        right = merge_sort(numbers[middle:])
        numbers = merge(left, right)
    return numbers

def merge(first: list, second: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
        first (list): The first sorted list.
        second (list): The second sorted list.

    Returns:
        list: A new sorted list containing all elements from the input lists.
    """
    newList = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            newList.append(first[i])
            i += 1
        else:
            newList.append(second[j])
            j += 1
    while i < len(first):
        newList.append(first[i])
        i += 1
    while j < len(second):
        newList.append(second[j])
        j += 1

    return newList

def main():
    numbers = [10,16,8,9,12,15,7,8,11]
    print(f"Here are the list: {numbers}")
    numbers = merge_sort(numbers)
    print(f"Here are the sorted list: {numbers}")

if __name__ == "__main__":
    main() 

