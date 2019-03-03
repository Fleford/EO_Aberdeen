import math
import numpy as np
from pyswarm import pso


def rastrigin(x, a=10):
    # Prep variables for best
    global best_fitness
    global list_of_best_fitness

    x = np.asarray(x)
    x = np.clip(x, -5.12, 5.12)
    n = len(x)

    # Minimum when inputs are 0
    def rastrigin_sum_term(xi):
        return xi ** 2 - a * np.cos(2 * math.pi * xi)

    totalfitness = a * n + sum(rastrigin_sum_term(x))

    # Save best
    if totalfitness < best_fitness:
        best_fitness = totalfitness
    # print(best_fitness)
    list_of_best_fitness.append(best_fitness)

    return totalfitness


n_points = 10
lb = -5.12*np.ones(n_points*2)
ub = 5.12*np.ones(n_points*2)
solution = np.zeros(n_points*2)

for runs in range(100):
    best_fitness = 1000
    list_of_best_fitness = []
    xopt, fopt = pso(rastrigin, lb, ub, maxiter=200, swarmsize=10)
    print("DONE! xopt:{} ,fopt:{}".format(xopt, fopt))

    # Save the list of best fitness to a text file
    print(len(list_of_best_fitness))
    with open("list_of_bests_PSO_rastrigin.tsv", "a+") as write_f:
        for value in list_of_best_fitness:
            s = str(value)
            # Just write without the decimals
            write_f.write(s[:s.index('.')] + "\t")
        write_f.write("\n")
