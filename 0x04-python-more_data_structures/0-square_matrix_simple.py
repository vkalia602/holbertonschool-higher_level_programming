#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = matrix[:]
        expo = lambda x: x ** 2
        for i in range(len(matrix)):
            new_matrix[i] = list(map(expo, matrix[i]))
        return new_matrix
