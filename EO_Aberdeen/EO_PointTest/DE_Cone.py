import numpy as np
from scipy.optimize import differential_evolution


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


n_points = 10
model_bounds = [(-100, 100) for x in range(n_points*2)]
solution = np.ones(n_points*2)

for runs in range(1):
    print("Run: " + str(runs))

    best_fitness = np.inf
    list_of_best_fitness = []

    result = differential_evolution(cone_multi_2d_total, model_bounds, disp=False, maxiter=10,
                                    polish=False, popsize=10)
    print("DONE! result.x: {} ,result.fun: {}".format(result.x, result.fun))
    print(list_of_best_fitness)
    print(len(list_of_best_fitness))

    # Save the list of best fitness to a text file
    with open("list_of_bests_DE_Cone.tsv", "a+") as write_f:
        for value in list_of_best_fitness:
            s = str(value)
            # Just write without the decimals
            write_f.write(s[:s.index('.')] + "\t")
        write_f.write("\n")

# # Prepare the final result for plotting
# final_solution = result.x
# final_solution = final_solution.reshape(-1, 2)
# np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/DE_Cone.txt", final_solution)
# print(final_solution)
