import numpy as np


def remove_dimension(matrix):
    """
    A NumPy program to remove single-dimensional entries from a specified shape.
    :param matrix:
    :return: the matrix without the single-dimensional entries
    """
    return np.squeeze(matrix).shape


if __name__ == "__main__":
    print(remove_dimension([3, 1, 4]))
