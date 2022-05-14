import numpy as np
import matplotlib.pyplot as pyplot


def sine_curve():
    """
    A NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib
    """
    x = np.arange(0, 5 * np.pi, 0.001)
    y = np.sin(x)
    pyplot.plot(x, y)
    pyplot.show()


if __name__ == '__main__':
    sine_curve()
