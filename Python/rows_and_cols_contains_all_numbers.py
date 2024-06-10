import pprint as pp


def rows_and_cols_contains_all_numbers(matrix: list[list[int]]) -> bool:
    """
        Check if all rows and columns of a matrix contain all numbers from 1 to n, where n is the length of the matrix.

        Args:
            matrix (list[list[int]]): The matrix to check.

        Returns:
            bool: True if all rows and columns contain all numbers from 1 to n, False otherwise.
    """
    length = len(matrix)
    valid = [i for i in range(1, length+1)]
    for i in range(length):
        lines = valid.copy()
        for j in range(length):
            row = matrix[j][i]
            col = matrix[i][j]
            if row not in lines or col not in valid:
                return False
            else:
                lines.remove(row)
    return True


def main():
    matrix = [
        [
            [1, 2, 3],
            [3, 1, 2],
            [2, 3, 1]
        ],
        [
            [1, 2, 3],
            [2, 1, 3],
            [3, 2, 1]
        ],
        [
            [1, 2, 3, 4],
            [4, 1, 2, 3],
            [3, 4, 1, 2],
            [2, 3, 4, 1]
        ],
        [
            [1, 2, 3, 4],
            [4, 1, 2, 3],
            [3, 4, 2, 1],
            [2, 3, 4, 1]
        ],
        [
            [1, 2, 3, 4, 5],
            [5, 1, 2, 3, 4],
            [4, 5, 1, 2, 3],
            [3, 4, 5, 1, 2],
            [2, 3, 4, 5, 1]
        ],
        [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [4, 3, 2, 5, 1],
            [3, 2, 1, 4, 5],
            [2, 1, 5, 3, 4]
        ],
        [
            [1, 2, 3, 4, 5, 6],
            [6, 1, 2, 3, 4, 5],
            [5, 6, 1, 2, 3, 4],
            [4, 5, 6, 1, 2, 3],
            [3, 4, 5, 6, 1, 2],
            [2, 3, 4, 5, 6, 1]
        ],
        [
            [1, 2, 3, 4, 5, 6],
            [6, 1, 2, 3, 4, 5],
            [5, 6, 1, 2, 3, 4],
            [4, 5, 6, 2, 1, 3],
            [3, 4, 5, 6, 1, 2],
            [2, 3, 4, 5, 6, 1]
        ]
    ]

    for i in matrix:
        result = rows_and_cols_contains_all_numbers(i)
        pp.pprint(i)
        if result:
            print(
                f"Contains all numbers from 1 to {len(i)} in rows and columns"
            )
        else:
            print(
                f"Does not contain all numbers from 1 to {len(i)} in rows and columns"
            )
        print("\n")


if __name__ == "__main__":
    main()
