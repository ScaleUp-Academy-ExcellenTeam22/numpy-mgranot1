import numpy as np


def add_vector_to_matrix(vector: np.array, matrix: np.ndarray) -> np.ndarray:
    """
    :param vector: Vector to add to all columns in the matrix.
    :param matrix: Some Matrix.
    :return: matrix with the addition of a vector to each row of the matrix.
    """
    return matrix[:, np.newaxis] + vector


