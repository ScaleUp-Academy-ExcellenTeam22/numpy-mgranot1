import numpy as np


def my_dstack(array1: np, araay2: np) -> np:
    """
    :param array1: 2-D array.
    :param araay2: 2-D array.
    :return: An array where converting (in sequence depth wise (along the third axis)) two 1-D arrays into a 2-D array.
    """
    return np.dstack((array1, araay2))
