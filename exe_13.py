import numpy as np


def my_dstack(array1: np.ndarray, araay2: np.ndarray) -> np.ndarray:
    """
    :param array1: Given array.
    :param araay2: Given array.
    :return: An array where converting (in sequence depth wise (along the third axis)) two 1-D arrays into a 2-D array.
    """
    return np.dstack((array1, araay2))
