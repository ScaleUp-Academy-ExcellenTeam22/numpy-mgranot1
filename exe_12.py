import numpy as np


def removing_single_dimensional_entries(array:np.ndarray)->np.ndarray:
    """

    :param array: Some array.
    :return: An array where removing single-dimensional entries from a specified shape.
    """
    return np.squeeze(array).shape

