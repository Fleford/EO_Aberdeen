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


# # Test with one vector
# xl = [1, 1, 1, 1, 1, 1]
# print(rosensbrock_multi_2d(xl))

# Prepare solutions
DE_solution = np.loadtxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/DE_Rosenbrock.txt")
DE_fitness = rosensbrock_multi_2d(DE_solution.reshape(-1))
DE_string = f"DE (Total fitness = {DE_fitness:.0f})"

PSO_solution = np.loadtxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/PSO_Rosenbrock.txt")
PSO_fitness = rosensbrock_multi_2d(PSO_solution.reshape(-1))
PSO_string = f"PSO (Total fitness = {PSO_fitness:.0f})"

EOWPP_solution = np.loadtxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/EOWPP_Rosenbrock.txt")
EOWPP_fitness = rosensbrock_multi_2d(EOWPP_solution.reshape(-1))
EOWPP_string = f"EOWPP (Total fitness = {EOWPP_fitness:.2f})"

# Prepare contour map
X = np.linspace(-2, 4, 1000)
Y = np.linspace(-2, 4, 1000)
X, Y = np.meshgrid(X, Y)
pairs = np.stack([X.reshape(-1), Y.reshape(-1)]).T
Z = rosensbrock_multi_2d(np.stack([X.reshape(-1), Y.reshape(-1)]).T)
Z = np.asarray([rosensbrock_multi_2d(x) for x in pairs])
Z = Z.reshape(X.shape)

fig, ax = plt.subplots()

# CS = ax.contourf(X, Y, Z, 20, alpha=1, cmap="jet")
CS = ax.pcolormesh(X, Y, Z, norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()), cmap="gnuplot2")
fig.colorbar(CS)
# ax.set_title('PSO Total fitness: {}'.format(int(fopt)))
ax.plot(DE_solution[:, 0], DE_solution[:, 1], "r^", label=DE_string, markeredgecolor="white", markersize=8)
ax.plot(PSO_solution[:, 0], PSO_solution[:, 1], "g^", label=PSO_string, markeredgecolor="white", markersize=8)
ax.plot(EOWPP_solution[:, 0], EOWPP_solution[:, 1], "b^", label=EOWPP_string, markeredgecolor="white", markersize=8)
ax.legend(loc=4)
plt.show()
