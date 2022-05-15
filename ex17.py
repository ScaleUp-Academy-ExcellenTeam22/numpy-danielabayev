import numpy
import numpy as np


def calculate_median(matrix: numpy.ndarray):
    """
    A NumPy program to compute the median of flattened given array.
    :param matrix: the matrix to calculate its median.
    """
    print(np.median(matrix))


if __name__ == '__main__':
    array = np.random.randint(100, size=16).reshape(4, 4)
    calculate_median(array)
