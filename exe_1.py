import numpy as np


def create_vector()->np:
    """
    :return: A vector in range 0- 20 with negative and positive valeus.
    """
    return [index * -1 if index >= 9 and index <= 15 else index for index in np.arange(21)]
