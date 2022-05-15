import numpy as np


def number_of_rows_and_columns(matrix:np)->tuple:
    """
    :param matrix: Two-dimensional matrix.
    :return: the number of rows and columns of the matrix.
    """
    rows = len(matrix[:])
    collumn = len(matrix[:][0])
    return (rows, collumn)


