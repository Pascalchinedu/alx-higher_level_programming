#!/usr/bin/python3

# a function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    column = len(matrix[0])

    for row in matrix:
        for column in row:
            print(column, end=' ')
        print()


# example usage
matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 8],
    [7, 8, 9, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()