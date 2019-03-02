import math
import numpy as np


def rosenbrock_2d(x, y, a, b):
    return (a - x)**2 + b(y - x**2)**2


xl = [0, 0]
print(rastrigin(xl, 10))