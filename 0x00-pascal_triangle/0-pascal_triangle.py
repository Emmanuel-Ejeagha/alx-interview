#!/usr/bin/python3
"""
This module implements the pascals triangle
"""


def pascal_triangle(n):

    """
    Returns a pascal triangle  , using list
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for id in range(n - 1):
        row = triangle[-1]
        list_sqr = [1]
        for idx, current in enumerate(row):
            try:
                next = row[idx + 1]
                list_sqr.append(current + next)
            except Exception:
                list_sqr.append(1)
        triangle.append(list_sqr)
    return triangle