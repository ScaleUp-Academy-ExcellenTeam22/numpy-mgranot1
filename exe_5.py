import numpy as np


def add_vector_to_matrix(vector:np, matrix:np)->np:
    """
    :param vector: Vector to add to all columns in the matrix.
    :param matrix: Some Matrix.
    :return: matrix with the addition of a vector to each row of the matrix.
    """
    return np.array([matrix[i, :] + vector for i in range(4)])


"""
m = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 1, 0])

print(add_vector_to_matrix(v,m))
"""
