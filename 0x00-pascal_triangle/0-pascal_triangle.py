#!/usr/bin/python3
"""
A module that implement the pascals triangle
"""


def pascal_triangle(n):

    """
    The pascal triangle implementation , using list
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for id in range(n - 1):
        dat = triangle[-1]
        lit_sqr = [1]
        for idx, current in enumerate(dat):
            try:
                next = dat[idx + 1]
                lit_sqr.append(current + next)
            except Exception:
                lit_sqr.append(1)
        triangle.append(lit_sqr)
    return triangle