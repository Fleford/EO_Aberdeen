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
scale = 100

best_fitness = 1000
list_of_best_fitness = []

sol1 = EOWPP.EO(n_rows=n_points, maximize=False, x_min=min*scale, x_max=max*scale, y_min=min*scale, y_max=max*scale,
             min_dist=1)
print(sol1.solution)
print(sol1.fitness_ready)
print()

# sol1.update_fitness(calculate_fitness(sol1, scale))
# sol1.update_best()
# print(sol1.best_solution.total_fitness())

print("Update fitness")
sol1.update_fitness(calculate_fitness(sol1, scale))
print(sol1.solution)
print(sol1.total_fitness())
print("Fitness ready?", sol1.fitness_ready)
print(sol1.eval_count)
print()

print("Best Sol")
sol1.update_best()
print(sol1.best_solution.solution)
print(sol1.best_solution.total_fitness())
print(sol1.best_solution.fitness_ready)
print()

print("remove_weakest")
sol1.remove_weakest()
print(sol1.solution)
print("Replaced row_index: ", sol1.replaced_row_index)
print("Replaced row_parameter: ", sol1.replaced_row_parameter)
print()

print("generate_row")
row = sol1.generate_row()
print(row)
print()

print("append_row")
sol1.append_row(row)
print(sol1.solution)
print(sol1.fitness_ready)
print(sol1.total_fitness())
print()

print("Update fitness")
sol1.update_fitness(calculate_fitness(sol1, scale))
print(sol1.solution)
print(sol1.total_fitness())
print(sol1.fitness_ready)
print(sol1.eval_count)
print()

print("Best Sol")
sol1.update_best()
print(sol1.best_solution.solution)
print(sol1.best_solution.total_fitness())
print(sol1.best_solution.fitness_ready)
print()

# for iteration in range(10):
#     sol1.remove_weakest()
#     sol1.append_row(sol1.generate_row())
#     sol1.update_fitness(calculate_fitness(sol1, scale))
#     sol1.update_best()
#     list_of_best_fitness.append(sol1.best_solution.total_fitness())
#     print(sol1.best_solution.total_fitness())