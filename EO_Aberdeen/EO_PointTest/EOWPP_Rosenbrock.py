import numpy as np
from EO_Aberdeen.EO_PointTest import EO


def rosenbrock_2d(x, y, a=1, b=100):
    # Minimum at
    return (a - x) ** 2 + b * (y - x ** 2) ** 2


def calculate_fitness(self, sf):
    # Parse out parameter matrix
    parameters = self.parameters()/sf

    # Generate new fitness vector
    fitness = rosenbrock_2d(parameters[:, 0], parameters[:, 1])

    return fitness


n_points = 10
min = -2
max = 4
# Note that coordinates are scaled to increase resolution
scale = 1000

for runs in range(1):
    print("Run: " + str(runs))
    best_fitness = 1000
    list_of_best_fitness = []
    sol1 = EO.EO(n_rows=n_points, maximize=False, x_min=min*scale, x_max=max*scale, y_min=min*scale, y_max=max*scale,
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

    # # Save the list of best fitness to a text file
    # print(list_of_best_fitness)
    # print(list_of_best_fitness[-1])
    # print(len(list_of_best_fitness))
    # with open("list_of_bests_EOWPP_rosenbrock.tsv", "a+") as write_f:
    #     for value in list_of_best_fitness:
    #         s = str(value)
    #         # Just write without the decimals
    #         write_f.write(s[:s.index('.')] + "\t")
    #     write_f.write("\n")

np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/EOWPP_Rosenbrock1.txt", sol1.best_solution.parameters()/scale)
