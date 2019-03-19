import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def rosensbrock_multi_2d(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    def rosenbrock_2d(x, y, a=1, b=100):
        # Minimum at
        return (a - x) ** 2 + b * (y - x ** 2) ** 2

    return sum(rosenbrock_2d(x_array[:, 0], x_array[:, 1]))


# Test with one vector
xl = [1, 1, 1, 1, 1, 1]
print(rosensbrock_multi_2d(xl))

# Prepare contour map
X = np.linspace(-2, 4, 1000)
Y = np.linspace(-2, 4, 1000)
X, Y = np.meshgrid(X, Y)
print(np.stack([X.reshape(-1), Y.reshape(-1)]).T)
pairs = np.stack([X.reshape(-1), Y.reshape(-1)]).T
Z = rosensbrock_multi_2d(np.stack([X.reshape(-1), Y.reshape(-1)]).T)
Z = np.asarray([rosensbrock_multi_2d(x) for x in pairs])
print(Z)
Z = Z.reshape(X.shape)

fig, ax = plt.subplots()

# CS = ax.contourf(X, Y, Z, 20, alpha=1, cmap="jet")
CS = ax.pcolormesh(X, Y, Z, norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()), cmap="gnuplot2")
fig.colorbar(CS)
# ax.set_title('PSO Total fitness: {}'.format(int(fopt)))
ax.plot(-1, 1, "g^", label="PSO", markeredgecolor="white", markersize=8)
ax.plot(1, 1, "r^", label="DE", markeredgecolor="white", markersize=8)
ax.plot(1, -1, "b^", label="EOWPP", markeredgecolor="white", markersize=8)
ax.legend(loc=2)
plt.show()
