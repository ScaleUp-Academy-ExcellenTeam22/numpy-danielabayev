import numpy
import numpy as np


def three_dimension() -> numpy.ndarray:
    """
    A NumPy program to create a three-dimension array with shape (300,400,5) and set to a variable. Fill the
    array elements with values using unsigned integer (0 to 255).
    :return: the array.
    """
    np.random.seed(32)
    array = np.random.randint(0, 256, size=(300, 400, 5), dtype=np.uint8)
    return array


if __name__ == '__main__':
    print(three_dimension())
