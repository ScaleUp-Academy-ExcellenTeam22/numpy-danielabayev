import numpy
import numpy as np


def replace_number(matrix: numpy.ndarray, number: int, sign: chr) -> numpy.ndarray:
    """
    A NumPy program replaces all numbers in a given array that is equal, less, and greater to a given number.
    :param matrix: the matrix to change its numbers.
    :param number: the number to check.
    :param sign:
    """
    if sign == "=":
        print(np.where(matrix == number, 1500, matrix))
    elif sign == "<":
        print(np.where(matrix < number, 1000, matrix))
    elif sign == ">":
        print(np.where(matrix > number, -500, matrix))


if __name__ == '__main__':
    array = np.random.randint(1000, size=16).reshape(4, 4)
    number_to_compare = 500
    replace_number(array, number_to_compare, "=")
    replace_number(array, number_to_compare, "<")
    replace_number(array, number_to_compare, ">")
