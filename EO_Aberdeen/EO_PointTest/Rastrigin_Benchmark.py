import math
import numpy as np
import matplotlib.pyplot as plt


def rastrigin(x, a=10):
    x = np.asarray(x)
    x = np.clip(x, -5.12, 5.12)
    n = len(x)

    def rastrigin_sum_term(xi):
        return xi ** 2 - a * np.cos(2 * math.pi * xi)

    return a*n + sum(rastrigin_sum_term(x))


# Test function for one point
xl = [4.03, -0.8]
print(rastrigin(xl))

# Test plotting contour surface
X = np.linspace(-5.12, 5.12, 200)
Y = np.linspace(-5.12, 5.12, 200)
X, Y = np.meshgrid(X, Y)
Z = rastrigin([X, Y], a=10)

fig, ax = plt.subplots()

CS = ax.contourf(X, Y, Z, 20)
fig.colorbar(CS)
ax.set_title('Simplest default with labels')

solution = np.array([[0.984, 0.018],
                     [0.995, -0.022],
                     [1.009,  0.016],
                     [0.977,  0.004],
                     [0.995,  0.016],
                     [0.987, -0.006],
                     [0.985,  0.000],
                     [0.998, -0.009],
                     [0.990, -0.002],
                     [0.998,  0.004]])
ax.plot(solution[:, 0], solution[:, 0], "r.")
plt.show()
