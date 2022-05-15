import numpy as np


def diagonal(size:int)->np:
    """
    :param size: Size of array.
    :return: A array with ones on a diagonal and zeros elsewhere.
    """
    return np.eye(size)

