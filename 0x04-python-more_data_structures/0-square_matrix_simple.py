#!/usr/bin/env python3

def square_matrix_simple(matrix=[]):
    xmatrix = []
    row = []
    for x in matrix:
        row = []
        for i in x:
            row.append(i**2)
        xmatrix.append(row)
    return xmatrix
