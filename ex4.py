import numpy as np


def border_matrix():
    """
    This function creates a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
    """
    vector = np.ones((10, 10))
    vector[1:-1, -1:1] = 0
    print(vector)


if __name__ == '__main__':
    border_matrix()
