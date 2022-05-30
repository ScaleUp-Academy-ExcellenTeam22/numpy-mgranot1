import numpy as np


def create_vector()->np.array:
    """
    :return: A vector in range 0- 20.
    """
    my_vector = np.arange(21)
    my_vector[(my_vector >= 9) & (my_vector <= 15)] *= -1
    return my_vector
