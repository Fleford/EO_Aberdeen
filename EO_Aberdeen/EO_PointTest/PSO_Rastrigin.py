import math
import numpy as np
from pyswarm import pso
import matplotlib.pyplot as plt

def rastrigin(x, a=10):
    # # Prep variables for best
    # global best_fitness
    # global list_of_best_fitness

    x = np.asarray(x)
    x = np.clip(x, -5.12, 5.12)
    n = len(x)

    # Minimum when inputs are 0
    def rastrigin_sum_term(xi):
        return xi ** 2 - a * np.cos(2 * math.pi * xi)

    totalfitness = a * n + sum(rastrigin_sum_term(x))

    # # Save best
    # if totalfitness < best_fitness:
    #     best_fitness = totalfitness
    # # print(best_fitness)
    # list_of_best_fitness.append(best_fitness)
    print(totalfitness)

    return totalfitness


n_points = 10
lb = -5.12*np.ones(n_points*2)
ub = 5.12*np.ones(n_points*2)
solution = np.zeros(n_points*2)

for runs in range(1):
    best_fitness = 1000
    list_of_best_fitness = []
    xopt, fopt = pso(rastrigin, lb, ub, maxiter=200, swarmsize=10)
    print("DONE! xopt:{} ,fopt:{}".format(xopt, fopt))
    print(list_of_best_fitness)
    print(len(list_of_best_fitness))

    # # Save the list of best fitness to a text file
    # print(len(list_of_best_fitness))
    # with open("list_of_bests_PSO_rastrigin.tsv", "a+") as write_f:
    #     for value in list_of_best_fitness:
    #         s = str(value)
    #         # Just write without the decimals
    #         write_f.write(s[:s.index('.')] + "\t")
    #     write_f.write("\n")

# Prepare the final result for plotting
final_solution = xopt
final_solution = final_solution.reshape(-1, 2)
np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/PSO_Rastrigin1.txt", final_solution)
print(final_solution)

# Prepare contour map
X = np.linspace(-5.12, 5.12, 1000)
Y = np.linspace(-5.12, 5.12, 1000)
X, Y = np.meshgrid(X, Y)
Z = rastrigin([X.reshape(-1), Y.reshape(-1)], a=10)
Z = Z.reshape(X.shape)

fig, ax = plt.subplots()

# CS = ax.contourf(X, Y, Z, 20, alpha=1, cmap="jet")
CS = ax.pcolormesh(X, Y, Z, cmap="bone")
fig.colorbar(CS)
ax.set_title('PSO Total fitness: {}'.format(int(fopt)))
ax.plot(final_solution[:, 0], final_solution[:, 1], "g^", label="PSO", markeredgecolor="white", markersize=8)
ax.plot(1, 1, "r^", label="DE", markeredgecolor="white", markersize=8)
ax.plot(1, -1, "b^", label="EOWPP", markeredgecolor="white", markersize=8)
ax.legend(loc=2)
plt.show()
