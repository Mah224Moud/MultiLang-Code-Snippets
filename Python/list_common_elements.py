def common(firstList: list, secondList: list) -> list:
    """
        Find the common elements between two lists.

        Args:
            firstList (list): The first list.
            secondList (list): The second list.

        Returns:
            list: A list containing the common elements between the two input lists.

        Example:
            >>> common([1, 2, 3], [2, 3, 4])
            [2, 3]
    """
    uniqueFirst = set(firstList)
    uniqueSecond = set(secondList)

    return list(uniqueFirst.intersection(uniqueSecond))


def main():
    firstList = [1, 2, 3, 4, 5]
    secondList = [5, 3, 6, 8, 9]
    print(
        f"The common elements between {firstList} and {secondList} are {common(firstList, secondList)}")


if __name__ == "__main__":
    main()
