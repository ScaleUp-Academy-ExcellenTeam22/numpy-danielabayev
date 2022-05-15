import numpy as np
import numpy


def mul_value(matrix1: numpy.ndarray, matrix2: numpy.ndarray) -> numpy.ndarray:
    """
    A NumPy program that multiplies two given arrays of same size element-by-element
    :param matrix1: matrix at the same size as matrix2.
    :param matrix2: matrix at the same size as matrix1.
    :return: the multiply result.
    """
    return np.multiply(matrix1, matrix2)


if __name__ == '__main__':
    mat1 = array = np.random.randint(10, size=16).reshape(4, 4)
    mat2 = array = np.random.randint(10, size=16).reshape(4, 4)
    print(mat1)
    print(mat2)
    print(mul_value(mat1, mat2))
