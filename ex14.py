import numpy
import numpy as np


def combine_dimension(matrix1: numpy.ndarray, matrix2: numpy.ndarray):
    """
    A NumPy program to combine a one and a two-dimensional array together and display their elements.
    :param matrix1: one-dimensional array
    :param matrix2: two-dimensional array
    """
    for first_matrix_number, second_matrix_number in np.nditer([matrix1, matrix2]):
        print(first_matrix_number, ":", second_matrix_number)


if __name__ == '__main__':
    array1 = np.random.randint(100, size=4).reshape(1, 4)
    array2 = np.random.randint(100, size=8).reshape(2, 4)
    combine_dimension(array1, array2)
