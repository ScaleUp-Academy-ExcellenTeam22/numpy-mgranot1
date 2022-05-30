import numpy as np


def combine_arrays(vector:int, array: np.ndarray):
    """
    :param vector: Some vector.
    :param array: Some array.
    combining a one and a two-dimensional array together and displaying their elements.
    """
    for a, b in np.nditer([vector, array]):
        print(a, " : ", b)
