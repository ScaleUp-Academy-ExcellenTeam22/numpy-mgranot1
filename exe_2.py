import numpy as np


def evenly_distributed()->np:
    """
    :return: A vector of length 10 with values evenly distributed  between 5 and 50.
    """
    return np.linspace(5, 50, num=10, endpoint=True, retstep=False, dtype=None, axis=0)


