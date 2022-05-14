import numpy
import numpy as np


def add_vector_to_matrix(matrix: numpy.ndarray, vector:numpy.ndarray) -> numpy.ndarray:
    """
    This function adds a vector to each row of a given matrix.
    :param matrix:
    :param vector:
    :return: the new matrix.
    """
    row_size, col_size = matrix.shape
    result_matrix = np.empty_like(matrix)
    for row in range(row_size):
        result_matrix[row:] = matrix[row:] + vector
    return result_matrix


if __name__ == '__main__':
    matrix_for_check = np.arange(10, 22).reshape((4, 3))
    vector_for_check = np.array([1, 1, 0])
    print(add_vector_to_matrix(matrix_for_check, vector_for_check))
