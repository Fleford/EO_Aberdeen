import math
import numpy as np
from EO_Aberdeen.EO_PointTest import EOWPP


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

    return totalfitness


def calculate_fitness(self, sf):
    # Parse out parameter matrix
    parameters = self.parameters()/sf

    # Generate new fitness vector
    fitness = rastrigin([parameters[:, 0], parameters[:, 1]])

    return fitness


n_points = 10
min = -5.12
max = 5.12
# Note that coordinates are scaled to increase resolution
scale = 1000

for runs in range(100):
    print("Run: " + str(runs))
    best_fitness = 1000
    list_of_best_fitness = []
    sol1 = EOWPP.EO(n_rows=n_points, maximize=False, x_min=min*scale, x_max=max*scale, y_min=min*scale, y_max=max*scale,
                 min_dist=1)

    sol1.update_fitness(calculate_fitness(sol1, scale))
    sol1.update_best()
    list_of_best_fitness.append(sol1.best_solution.total_fitness())
    # print(sol1.best_solution.total_fitness())

    for iteration in range(400):
        sol1.remove_weakest()
        sol1.append_row(sol1.generate_row())
        sol1.update_fitness(calculate_fitness(sol1, scale))
        sol1.update_best()
        list_of_best_fitness.append(sol1.best_solution.total_fitness())
        # print(sol1.best_solution.total_fitness())

    # Save the list of best fitness to a text file
    # print(len(list_of_best_fitness))
    with open("list_of_bests_EOWPP_rastrigin.tsv", "a+") as write_f:
        for value in list_of_best_fitness:
            s = str(value)
            # Just write without the decimals
            write_f.write(s[:s.index('.')] + "\t")
        write_f.write("\n")
