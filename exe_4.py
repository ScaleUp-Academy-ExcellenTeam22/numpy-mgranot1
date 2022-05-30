import numpy as np


def zero_and_one_matrix(size:int)-> np.ndarray:
    """

    :param size: Matrix size.
    :return: The matrix in which the elements on the borders will be equal to 1, and inside 0.
    """
    matrix = np.ones((size, size))
    matrix[1:-1, 1:-1] = 0
    return matrix
