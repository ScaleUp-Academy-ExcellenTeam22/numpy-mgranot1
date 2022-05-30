import numpy as np


def replace_values(array: np.array, num1: int, num2: int, operator: str) -> np.ndarray:
    """
    :param array: Given array.
    :param num1: Numbers are exchanged according to it.
    :param num2: Exchanging certain numbers to it.
    :param operator: Replacement operator according to.
    :return: An array with numbers determined according to num1 is replaced by num2.
    """
    if operator == "==":
        return np.where(array == num1, num2, array)
    if operator == "<":
        return np.where(array < num1, num2, array)
    if operator == ">":
        return np.where(array > num1, num2, array)


