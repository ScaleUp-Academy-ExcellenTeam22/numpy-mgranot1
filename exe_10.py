import numpy as np


def sort_axis(array: np.ndarray, axis1: int) -> np.ndarray:
    """
    :param array: Some array
    :param axis1: Sets the sort.
    :return: array who sorted along the first, last axis of an array.
    """
    return np.sort(array, axis=axis1)


