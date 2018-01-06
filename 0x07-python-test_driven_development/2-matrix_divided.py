#!/usr/bin/python3
def matrix_divided(matrix, div):
    errormsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(errormsg)
