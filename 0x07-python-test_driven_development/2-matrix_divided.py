#!/usr/bin/python3
"""Module for dividing numbers in a matrix

"""


def matrix_divided(matrix, div):
    """Function to divide numbers in matrix by div

    """
    errormsg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    errormsg_2 = "Each row of the matrix must have the same size"
    diverrormsg = "div must be a number"
# check if div is not None
    if div is None:
        raise TypeError(diverrormsg)

## check if matrix is a list
    if type(matrix) is not list:
        raise TypeError(errormsg_1)

## check if length of each row is same
## check if every number in the matrix is an int
## check if each row is a list

    for row in matrix:
        if type(row) is not list:
            raise TypeError(errormsg_1)
        if len(matrix[0]) is not len(row):
            raise TypeError(errormsg_2)
        for number in row:
            if type(number) is not int and type(number) is not float:
                raise TypeError(errormsg_1)

# check if div type is int or float
    if type(div) is not int and type(div) is not float:
        raise TypeError(diverrormsg)

# check if div == 0
    if div is 0:
        raise ZeroDivisionError("division by zero")

# divide elements in matrix by div
    new_matrix = matrix[:]
    for row in range(len(matrix)):
        new_matrix[row] = list(map(lambda x: round(x / div, 2), matrix[row]))

    return new_matrix
