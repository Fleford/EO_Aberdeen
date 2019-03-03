import math
import numpy as np
from EO_Aberdeen.EO_PointTest import EO


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
min = -5.12
max = 5.12
# Note that coordinates are scaled to increase resolution
scale = 100

best_fitness = 1000
list_of_best_fitness = []

# Note that coordinates are multiplied by a factor of 100 to compensate for
sol1 = EO.EO(n_rows=n_points, maximize=False, x_min=min*scale, x_max=max*scale, y_min=min*scale, y_max=max*scale,
             min_dist=1)
print(sol1.solution)
print(sol1.fitness_ready)
print()