#!/usr/bin/python3
"""matrix_divided"""


def matrix_divided(matrix, div):
    """divider for matrix.

    Args:
        matrix: Matrix
        div: the num

    Raises:
        TypeError: if not a list of int or floats
        TypeError: if rows are not same size
        TypeError: if the div num is not int or float
        ZeroDivisionError: if div num is equal to zero

    Returns:
        new matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " +
                "of integers/floats")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                "of integers/floats")
    elif not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                "of integers/floats")
        for xx in matrix:
            if len(xx) == 0:
                raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
                for x in xx:
                    if type(x) is not int and type(x) is not float:
                        raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
                        len_rows = []
    for xx in matrix:
        len_rows.append(len(xx))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in xx] for xx in matrix]
    return new_matrix
