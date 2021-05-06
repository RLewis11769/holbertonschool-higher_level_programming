#!/usr/bin/python3

"""
matrix_divided - divides all elements of 2d array by number
@matrix: list of lists of numbers to be divided
@div: number to divide numbers of matrix by
Return: new matrix containing results of division
"""


def matrix_divided(matrix, div):
    """ Divides contents of matrix by div """

    """ Tests matrix and elements in matrix """
    if not isinstance(matrix, list):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError
            ("matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")

    """ Tests length of matrix """
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    """ Tests div is proper number """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ return matrix divided by div as seen in 0x04-101 """
    new_matrix = list(map(lambda num:
                          list(map(lambda num:
                                   round(num / div, 2), num)), matrix))
    return new_matrix
