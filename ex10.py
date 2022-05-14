import numpy
import numpy as np


def sort_along(matrix: numpy.ndarray):
    """
    A NumPy program to sort along with the first, and last axis of an array.
    :param matrix: matrix to sort.
    """
    # first axis
    print(np.sort(matrix, axis=0))
    # last axis - the default
    print(np.sort(matrix))


if __name__ == '__main__':
    array = np.random.randint(100, size=16).reshape(4, 4)
    sort_along(array)
