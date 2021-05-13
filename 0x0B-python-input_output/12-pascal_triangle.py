#!/usr/bin/python3

"""
pascal_triangle - returns list of list of integers of Pascal's triangle
@n: size of Pascal's triangle
Return: list of lists representing Pascal's triangle

Note: Pascal's triangle sums adjacent elements in preceding rows
    Used google, sorry
Logic: Beginning and end of each row is 1
    In this triangle, sum is diagonal right and directly above
        Aka [down - 1][across - 1] and [down - 1][across]
    List of ints should be added at end of each line
Plan: Create triangle and row lists, append
      1. If end: add 1 and append (first because can sum properly)
      2. If beginning: add 1
      3. Else: add sum of diag and above
"""


def pascal_triangle(n):
    """ Creates list of lists of representation of Pascal's triangle """
    triangle = []
    if n <= 0:
        return triangle
    for down in range(n):
        row = []
        for across in range(down + 1):
            if down == across:
                """ 1 at end """
                row.append(1)
                """ Add row list to triangle list """
                triangle.append(row)
            elif across == 0:
                """ 1 at beginning """
                row.append(1)
            else:
                """ Number from diagonal right """
                diag = triangle[down - 1][across - 1]
                """ Number from directly above (would be diagonal left) """
                above = triangle[down - 1][across]
                """ Add number from diag and above to row """
                row.append(diag + above)
    return triangle
