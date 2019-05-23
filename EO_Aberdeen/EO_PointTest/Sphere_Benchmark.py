import numpy as np


def sphere_2d(x, y):
    return x ** 2 + y ** 2


def sphere_multi_2d_total(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    result = sum(sphere_2d(x_array[:, 0], x_array[:, 1]))

    return result


def sphere_multi_2d_array(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    result = sphere_2d(x_array[:, 0], x_array[:, 1])
    result = result.reshape(-1, 1)

    return result


# Test with one vector
x1 = [1, 1, 1, 1, 1, 1]
print(sphere_multi_2d_array(x1))
print(sphere_multi_2d_total(x1))

