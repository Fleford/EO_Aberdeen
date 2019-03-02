import numpy as np


def rosensbrock_multi_2d(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    def rosenbrock_2d(x, y, a=1, b=100):
        # Minimum at
        return (a - x) ** 2 + b * (y - x ** 2) ** 2

    return sum(rosenbrock_2d(x_array[:, 0], x_array[:, 1]))


xl = [1, 1, 1, 1]
print(rosensbrock_multi_2d(xl))
