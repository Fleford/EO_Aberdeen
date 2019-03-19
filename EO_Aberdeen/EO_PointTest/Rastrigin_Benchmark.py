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


# # Test function for one point
# xl = [4.03, -0.8]
# print(rastrigin(xl))

# Prepare solutions
PSO_solution = np.loadtxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/PSO_Rastrigin.txt")
PSO_fitness = rastrigin(PSO_solution.reshape(-1))
PSO_string = f"PSO (Total fitness = {PSO_fitness:.0f})"

DE_solution = np.loadtxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/DE_Rastrigin.txt")
DE_fitness = rastrigin(DE_solution.reshape(-1))
DE_string = f"DE (Total fitness = {DE_fitness:.0f})"

EOWPP_solution = np.loadtxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/EOWPP_Rastrigin.txt")
EOWPP_fitness = rastrigin(EOWPP_solution.reshape(-1))
EOWPP_string = f"EOWPP (Total fitness = {EOWPP_fitness:.0f})"

# Prepare background map
X = np.linspace(-5.12, 5.12, 700)
Y = np.linspace(-5.12, 5.12, 700)
X, Y = np.meshgrid(X, Y)
Z = rastrigin([X.reshape(-1), Y.reshape(-1)], a=10)
Z = Z.reshape(X.shape)

fig, ax = plt.subplots()

# CS = ax.contourf(X, Y, Z, 20, alpha=1, cmap="jet")
CS = ax.pcolormesh(X, Y, Z, cmap="gnuplot2")
fig.colorbar(CS)
ax.plot(DE_solution[:, 0], DE_solution[:, 1], "r^", label=DE_string, markeredgecolor="white", markersize=8)
ax.plot(PSO_solution[:, 0], PSO_solution[:, 1], "g^", label=PSO_string, markeredgecolor="white", markersize=8)
ax.plot(EOWPP_solution[:, 0], EOWPP_solution[:, 1], "b^", label=EOWPP_string, markeredgecolor="white", markersize=8)
ax.legend(loc=2)
plt.show()
