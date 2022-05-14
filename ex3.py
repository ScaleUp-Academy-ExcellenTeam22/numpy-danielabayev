import numpy as np


def matrix_size(matrix) -> list[int, int]:
    """
    A NumPy program to find the number of rows and columns of a given matrix.
    :param matrix: the matrix to check.
    :return: the number of rows and cols.
    """
    return matrix.shape


if __name__ == '__main__':
    print(matrix_size(np.arange(10, 22).reshape((2, 6))))

