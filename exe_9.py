import numpy as np


def mul_arrays(array1:np, array2:np)->np:
    """

    :param array1: First array for multiplication.
    :param array2: Second array for multiplication.
    :return: Multiplication of array1 and array2.
    """
    return np.multiply(array1, array2)


"""
nums1 = np.array([[2, 5, 2],
              [1, 5, 5]])
nums2 = np.array([[5, 3, 4],
              [3, 2, 5]])
print("Array1:")
print(nums1)
print("Array2:")
print(nums2)
print("\nMultiply said arrays of same size element-by-element:")
print(mul_arrays(nums1, nums2))"""
