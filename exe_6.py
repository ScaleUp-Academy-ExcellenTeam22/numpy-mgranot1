import numpy as np
import matplotlib.pyplot as plt


def computing_coordinates():
    """
    computing the x and y coordinates for points on a sine curve and plotting the points using matplotlib.
    """
    x = np.arange(0, 3 * np.pi, 0.2)
    y = np.sin(x)
    print("Plot thepoints  using matplotlib:")
    plt.plot(x, y)
    plt.show()
