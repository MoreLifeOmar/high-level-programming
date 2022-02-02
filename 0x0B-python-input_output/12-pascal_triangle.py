#!/usr/bin/python3
"""
pascal triangle module
"""


def pascal_triangle(n):
    """
    returns a list of lists of
    integers representing the Pascal's
    triangle of n
    """
    if n <= 0:
        return []
    res = []
    l = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(l[j] + l[j - 1])
        l = row
        res.append(row)
    return res
