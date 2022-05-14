import numpy
import numpy as np


def convert_matrix(matrix1: numpy.ndarray, matrix2: numpy.ndarray) -> numpy.ndarray:
    """
    A NumPy program to convert (in sequence depth wise (along with the third axis)) two 1-D arrays into a 2-D array.
    :param matrix1:
    :param matrix2:
    :return: the converted matrix.
    """
    return np.dstack((matrix1, matrix2))


if __name__ == '__main__':
    array1 = (10, 20, 30)
    array2 = (40, 50, 60)
    print(convert_matrix(array1, array2))
