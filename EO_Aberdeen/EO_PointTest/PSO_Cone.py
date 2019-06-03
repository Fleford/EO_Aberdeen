import numpy as np
from pyswarm import pso


def cone_2d(x, y):
    # It's basically the Euclidean distance from the origin
    return np.sqrt(x ** 2 + y ** 2)


def cone_multi_2d_total(x_array):
    # Prep variables for best
    global best_fitness
    global list_of_best_fitness

    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    result = sum(cone_2d(x_array[:, 0], x_array[:, 1]))

    # Save best
    if result < best_fitness:
        best_fitness = result
    # print(best_fitness)
    list_of_best_fitness.append(best_fitness)

    return result


def rosenbrock_multi_2d(x_array):
    # Prep variables for best
    global best_fitness
    global list_of_best_fitness

    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    def rosenbrock_2d(x, y, a=1, b=100):
        # Minimum at
        return (a - x) ** 2 + b * (y - x ** 2) ** 2

    result = sum(rosenbrock_2d(x_array[:, 0], x_array[:, 1]))

    # Save best
    if result < best_fitness:
        best_fitness = result
    # print(best_fitness)
    list_of_best_fitness.append(best_fitness)

    return result


n_points = 10
lb = -100*np.ones(n_points*2)
ub = 100*np.ones(n_points*2)
solution = np.ones(n_points*2)

for runs in range(100):
    best_fitness = np.inf
    list_of_best_fitness = []
    xopt, fopt = pso(cone_multi_2d_total, lb, ub, maxiter=200, swarmsize=20)
    print("DONE! xopt:{} ,fopt:{}".format(xopt, fopt))
    print(list_of_best_fitness)
    print(len(list_of_best_fitness))

    # Save the list of best fitness to a text file
    with open("list_of_bests_PSO_cone.tsv", "a+") as write_f:
        for value in list_of_best_fitness:
            s = str(value)
            # Just write without the decimals
            write_f.write(s[:s.index('.')] + "\t")
        write_f.write("\n")

# # Prepare the final result for plotting
# final_solution = xopt
# final_solution = final_solution.reshape(-1, 2)
# np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/PSO_Rosenbrock1.txt", final_solution)
# print(final_solution)
