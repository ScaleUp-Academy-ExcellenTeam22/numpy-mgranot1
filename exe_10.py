import numpy as np


def sort_axis(array:np, axis1:int)->np:
    """
    :param array: Some array
    :param axis1: Sets the sort.
    :return: array who sorted along the first, last axis of an array.
    """
    print(np.sort(array, axis=axis1))
    return np.sort(array, axis=axis1)


