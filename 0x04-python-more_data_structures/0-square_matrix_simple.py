#!/usr/bin/python3

'''
    A function that computes the square value of all
    integers of a matrix
'''
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)


# Example usage
matrix = [
    [12, 2, 3],
    [4, 12, 6],
    [7, 8, 12]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)