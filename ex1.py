import numpy


def create_vector() -> list:
    """
    This function makes a vector of numbers between 0 to 20 and changes the sign of the number in the range 9 to 15.
    :return: vector of the numbers.
    """
    vector = numpy.arange(20)
    vector[(vector > 9) & (vector < 15)] *= -1
    return vector


if __name__ == '__main__':
    print(create_vector())
