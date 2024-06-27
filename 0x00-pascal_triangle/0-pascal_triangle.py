#!/usr/bin/python3
"""Method for pascal's triangle"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []
    if n < 1 or not isinstance(n, int):
        return triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif i > 0 and j > 0:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
