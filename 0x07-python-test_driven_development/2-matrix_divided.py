#!/usr/bin/python3

"""
matrix_divided - divides all elements of 2d array by number
@matrix: list of lists of numbers to be divided
@div: number to divide numbers of matrix by
Return: new matrix containing results of division
"""


def matrix_divided(matrix, div):
    """ Divides contents of matrix by div """

    # tests matrix and elements in matrix
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for elements in matrix:
        if type(elements) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # test div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # return matrix divided by div as seen in 100-
    new_matrix = list(map(lambda num: list(map(lambda num: round(num / div, 2), num)), matrix))
    return new_matrix
