import numpy as np


def distance_2d(x, y, a=1, b=100):
    return np.sqrt(x ** 2 + y ** 2)


def distance_multi_2d_total(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    result = sum(distance_2d(x_array[:, 0], x_array[:, 1]))

    return result


def distance_multi_2d_array(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    result = distance_2d(x_array[:, 0], x_array[:, 1])
    result = result.reshape(-1, 1)

    return result


# Test with one vector
x1 = [1, 1, 1, 1, 1, 1]
print(distance_multi_2d_array(x1))
print(distance_multi_2d_total(x1))

