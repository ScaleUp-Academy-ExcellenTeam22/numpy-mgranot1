import numpy as np


def make_matrix(size:int=4)->np:
    """

    :param size: Size of matrix.
    :return: Array with random values, and swapping first and last rows.
    """
    matrix = np.random.rand(size, size)
    new_matrix = np.copy(matrix)
    new_matrix[0] = matrix[-1]
    new_matrix[-1] = matrix[0]
    return new_matrix


"""

print(make_matrix())

"""
