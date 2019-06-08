import math
import numpy as np
from EO_Aberdeen.EO_PointTest import EOWPP
import sys


def wedge_2d(x, y):
    point = np.array([x, y]).T
    center_point1 = np.array([-50, -50])
    center_point2 = np.array([50, 50])
    fitness_1 = np.linalg.norm(point - center_point1, axis=1)
    fitness_2 = np.linalg.norm(point - center_point2, axis=1)
    fitness = (fitness_1 + fitness_2)

    return fitness


def calculate_fitness(self, sf):
    # Parse out parameter matrix
    parameters = self.parameters()/sf

    # Generate new fitness vector
    fitness = wedge_2d(parameters[:, 0], parameters[:, 1])
    # print()
    # print("fitness")
    # print(fitness)

    return fitness


n_points = 10
min = -100
max = 100
# Note that coordinates are scaled to increase resolution
# scale = 10000
scale = 1000

# To prevent recursion depth problem
sys.setrecursionlimit(2500)

for runs in range(100):
    print()
    print("Run: " + str(runs))
    list_of_best_fitness = []
    sol1 = EOWPP.EO(n_rows=n_points, maximize=False, x_min=min*scale, x_max=max*scale, y_min=min*scale, y_max=max*scale,
                 min_dist=1)

    sol1.update_fitness(calculate_fitness(sol1, scale))
    sol1.update_best()
    list_of_best_fitness.append(sol1.best_solution.total_fitness())
    # print(sol1.best_solution.total_fitness())
    # print(sol1.best_solution.parameters() / scale)

    for iteration in range(500):
        sol1.remove_weakest()
        sol1.append_row(sol1.generate_row())
        sol1.update_fitness(calculate_fitness(sol1, scale))
        sol1.update_best()
        list_of_best_fitness.append(sol1.best_solution.total_fitness())
        # print(sol1.best_solution.total_fitness())
        # print(sol1.best_solution.parameters()/scale)

    print("Final total fitness and parameters: ")
    print(sol1.best_solution.total_fitness())
    print(sol1.best_solution.parameters() / scale)

    # Save the list of best fitness to a text file
    # print(len(list_of_best_fitness))
    with open("list_of_bests_EOWPP_wedge.tsv", "a+") as write_f:
        for value in list_of_best_fitness:
            s = str(value)
            # # Just write without the decimals
            # write_f.write(s[:s.index('.')] + "\t")
            write_f.write(s + "\t")
        write_f.write("\n")
# np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/EOWPP_Rastrigin1.txt", sol1.best_solution.parameters()/scale)
