import math
import numpy as np
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt


def rastrigin(x, a=10):
    # # Prep variables for best (Don't forget to uncomment)
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
    # if totalfitness.astype(float) < best_fitness:
    #     best_fitness = totalfitness
    # # print(best_fitness)
    # list_of_best_fitness.append(best_fitness)

    return totalfitness


n_points = 10
model_bounds = [(-5.12, 5.12) for x in range(n_points*2)]
solution = np.zeros(n_points*2)

for runs in range(1):
    print("Run: " + str(runs))

    best_fitness = 1000
    list_of_best_fitness = []

    result = differential_evolution(rastrigin, model_bounds, disp=False, maxiter=10, polish=False, popsize=10)
    print("DONE! result.x:{} ,result.fun:{}".format(result.x, result.fun))
    # print(list_of_best_fitness)
    # print(len(list_of_best_fitness))

    # # Save the list of best fitness to a text file
    # print(len(list_of_best_fitness))
    # with open("list_of_bests_DE_rastrigin.tsv", "a+") as write_f:
    #     for value in list_of_best_fitness:
    #         s = str(value)
    #         # Just write without the decimals
    #         write_f.write(s[:s.index('.')] + "\t")
    #     write_f.write("\n")

# Prepare the final result for plotting
final_solution = result.x
final_solution = final_solution.reshape(-1, 2)
np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/DE_Rastrigin.txt", final_solution)
print(final_solution)

# Prepare contour map
X = np.linspace(-5.12, 5.12, 200)
Y = np.linspace(-5.12, 5.12, 200)
X, Y = np.meshgrid(X, Y)
Z = rastrigin([X.reshape(-1), Y.reshape(-1)], a=10)
Z = Z.reshape(X.shape)

fig, ax = plt.subplots()

CS = ax.contourf(X, Y, Z, 20)
fig.colorbar(CS)
ax.set_title('DE Total fitness: {}'.format(int(result.fun)))
ax.plot(final_solution[:, 0], final_solution[:, 1], "r.")
plt.show()
