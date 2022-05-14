import numpy as np


def ex2() -> list:
    """
    NumPy program which creates a vector of length 10 with values evenly distributed between 5 and 50.
    :return: vector of the numbers.
    """
    vector = np.linspace(5, 49, 10)
    return vector


if __name__ == '__main__':
    print(ex2())
