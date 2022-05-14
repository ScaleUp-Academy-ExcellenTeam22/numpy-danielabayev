import numpy
import numpy as np


def create_matrix_4_on_4() -> numpy.ndarray:
    """
    A NumPy program that creates a 4x4 array with random values, then creates a new array from the said array
    swapping first and last rows.
     :return: the new array.
    """
    array = np.random.randint(1000, size=16).reshape(4, 4)
    print(array)
    new_array = array[::-1]
    return new_array


if __name__ == '__main__':
    print(create_matrix_4_on_4())
